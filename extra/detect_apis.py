
import pandas as pd

df = pd.read_csv("results/javascript_calls.csv")
fp_apis = [
    "CanvasRenderingContext2D", "WebGLRenderingContext",
    "AudioContext", "MediaDevices", "Navigator", "Screen", "getClientRects"
]

matches = df[df["callee"].str.contains('|'.join(fp_apis), na=False)]
matches.to_csv("results/fingerprint_matches.csv", index=False)

print(f"Found {len(matches)} fingerprinting-related JS calls.")
