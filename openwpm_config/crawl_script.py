import os
from pathlib import Path
from typing import Literal

from openwpm.task_manager import TaskManager
from openwpm.config import ManagerParams, BrowserParams
from openwpm.command_sequence import CommandSequence
import csv

# --- Configuration ---

FIREFOX_BINARY_PATH = os.path.join(os.getcwd(), 'firefox-bin', 'firefox')

os.environ['FIREFOX_BINARY'] = FIREFOX_BINARY_PATH

with open("websitelist.csv", "r") as f:
    sites = [line.strip() for line in f.readlines() if line.strip()]