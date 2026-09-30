import json

# Path to your autosave file
input_path = r"C:\Users\jjdom\OneDrive\Route tracker\Route Tracker\Route Tracker\bin\Debug\net8.0-windows\Routes\SavedProgress\AC4 100 % Route - Main Route_AutoSave.json"
output_path = input_path  # Overwrite in place, or change to a new file if you want

with open(input_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Set both flags to false for every entry
fixed = {k: {"IsCompleted": False, "IsSkipped": False} for k in data}

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(fixed, f, indent=2)

print("Done! File rewritten in the correct format.")
