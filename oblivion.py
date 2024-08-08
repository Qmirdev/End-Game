import os
from pathlib import Path
from datetime import datetime
import logging

# 1. Task Name: Set a descriptive name for this script to make it clear what its purpose is.
# This name will be used in the log file naming convention.
task_name = "End Game"

# Capture the current timestamp in a specific format for use in the log file name.
# This ensures that each log file is unique and can be easily identified by its creation time.
current_time = datetime.now().strftime("%Y.%m.%d-%H.%M.%S")

# 2. Logging Configuration: Specify the file path where log entries will be saved.
# This helps in tracking the script's execution and any issues that may arise.
# Ensure that the directory structure exists, or the script will not run correctly.
log_file = Path.home() / "Documents" / "End-Game" / "logs" / f"{task_name}_{current_time}.log"
logging.basicConfig(filename=log_file, level=logging.INFO)

# 3. Target Path: Define the specific folder that you intend to delete.
# Modify the path according to your requirements to target the correct directory.
# In this example, the designated folder, named "Test", is located on the Desktop.
target_path = Path.home() / "Desktop" / "Test"

# 4. Delete Date: Set the exact date when the folder should be deleted.
# The script only executes the deletion if the current date is on or after this specified date.
# Modify this date as needed to suit your scheduling requirements for deletion.
delete_date = datetime(2024, 8, 8)

# Check if the current date has reached or surpassed the delete date threshold.
if datetime.now() >= delete_date:
    logging.info(f"Running script at {datetime.now()}")
    # Verify if the target folder exists before attempting deletion.
    if os.path.exists(target_path):
        # Attempt to remove the specified folder.
        try:
            os.rmdir(target_path)
            logging.info(f"Successfully deleted folder: {target_path}")
        except OSError as e:
            # Log an error if the folder cannot be deleted.
            logging.error(f"Error deleting folder {target_path}: {e}")
    else:
        # If the folder does not exist, log this information.
        logging.info(f"Folder {target_path} does not exist, no deletion performed.")
else:
    # If the current date is before the delete date, log that the script will not execute the deletion.
    logging.info(f"Current date {datetime.now()} is before delete date {delete_date}")