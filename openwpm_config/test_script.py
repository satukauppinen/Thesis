import os
from pathlib import Path
from typing import Literal

# Importing OpenWPM components
from openwpm.browser_manager import BrowserManager
from openwpm.commands.browser_commands import GetCommand
from openwpm.config import BrowserParams, ManagerParams
from openwpm.storage.sql_provider import SQLiteStorageProvider
from openwpm.task_manager import TaskManager
from openwpm.command_sequence import CommandSequence

# The config

FIREFOX_BINARY_PATH = os.path.join(os.getcwd(), 'firefox-bin', 'firefox')

os.environ['FIREFOX_BINARY'] = FIREFOX_BINARY_PATH

TEST_SITES = [
    "http://example.com",
    "https://www.mozilla.org",
    "https://www.google.com"
]

# Number of browsers to run concurrently. Start with 1 for debugging.
NUM_BROWSERS = 1

# Display mode for the browser: "headless" (no GUI), "xvfb" (virtual display), or "native" (actual GUI, usually not in WSL)
# "headless" is generally recommended for server environments like WSL.
display_mode: Literal["native", "headless", "xvfb"] = "headless"

# Define output directory and database file
OUTPUT_DIR = Path("./test_output_data/")
DATABASE_FILE = OUTPUT_DIR / "crawl-data.sqlite"
LOG_FILE = OUTPUT_DIR / "openwpm.log"
GECKODRIVER_LOG = OUTPUT_DIR / "geckodriver.log" # Geckodriver logs are crucial for debugging browser issues

# Manager and Browser Parameters Setup 

# Manager parameters
manager_params = ManagerParams(
    num_browsers=NUM_BROWSERS,
    data_directory=OUTPUT_DIR,
    log_path=LOG_FILE,
    
)

# BrowserParameters
browser_params = []
for _ in range(NUM_BROWSERS):
    browser_param = BrowserParams(
        display_mode=display_mode,
        http_instrument=True,
        cookie_instrument=True,
        navigation_instrument=True,
        js_instrument=True,
        dns_instrument=True,
        maximum_profile_size=50 * (1024**2) # 50 MB (using 1024 for binary MB)
    )
    browser_params.append(browser_param)

# This Is The Main Crawl Logic

def main():
    # Ensuring the output directory exists
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Starting crawl. Output will be saved to: {OUTPUT_DIR.resolve()}")
    print(f"Firefox binary location set to: {FIREFOX_BINARY_PATH} (via os.environ['FIREFOX_BINARY'])")

    # Initializing the TaskManager
    try:
        with TaskManager(
            manager_params,
            browser_params,
            SQLiteStorageProvider(DATABASE_FILE),
            None, 
        ) as manager:
            
            for index, site in enumerate(TEST_SITES):
                def callback(success: bool, val: str = site) -> None:
                    print(
                        f"CommandSequence for {val} ran {'successfully' if success else 'unsuccessfully'}"
                    )

                command_sequence = CommandSequence(
                    site,
                    site_rank=index,
                    callback=callback,
                )

                command_sequence.append_command(GetCommand(url=site, sleep=3), timeout=60)
                

                manager.execute_command_sequence(command_sequence)

            
            print("Crawl finished successfully!")

    except Exception as e:
        print(f"An error occurred during the crawl: {e}")
        print("Please check the OpenWPM logs and geckodriver.log for more details.")

if __name__ == "__main__":
    main()

