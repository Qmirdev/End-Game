# End Game: Peace of Mind for Your Secrets 💀

## Overview
Ever thought, “What will happen to my *Top Secret* folder after I disappear into the cosmos?” Worry no more! With this script, you can ensure that your digital secrets vanish into thin air.

## 🎯 What is End Game?
End Game is a simple Python script designed for who want to make sure their top secret files are deleted automatically when the clock strikes *delete-o’clock*. Whether you're venturing to the moon, the bottom of the ocean, or to another dimension, End Game will ensure your digital footprint is wiped clean!

<div align=left height=200>
    <img src="https://i.ibb.co/pQrCHSq/dead.jpg">
</div>

## ✨ Features

- 🗑️ Automatic Deletion: Specify a date, and poof!—your folder will be gone forever!
- 🕒 Scheduled Execution: Set it up to run on startup, so even when you are not physically present, the cleanup happens.
- 🔒 Secrets Erased: Rest easy knowing that no prying eyes will discover what you’ve left behind.
- 📜 Logging: Keep track of the script's activities with fine-tuned logging so you’ll know if the folder was deleted or if things went sideways.

## 🛠 Requirements

- Python 3.x
- Basic command line knowledge
- A sense of humor (optional, but recommended)

## 🤓 Installation Steps

1. **Clone the Repository** *(if you haven't already)*:
   ```bash
   git clone https://github.com/Qmirdev/End-Game.git
   cd End-Game
2. **Install the Requirements:**
   ```bash
   pip3 install -r requirements.txt
3. **Edit the Script:** Open oblivion.py in your favorite text editor, and configure:
   - `task_name`: Give it a friendly name (e.g., "Secret Folder Delete").
   - `log_file`: Adjust this to the path of the folder you want to save the log file to.
   - `target_path`: Adjust this to the path of the folder you want deleted.
   - `delete_date`: Pick a date in the future when you want the folder to disappear automatically.
4. **Set Up for Auto-Run:**
   - **Windows:** Use Task Scheduler to add a new task that runs the script at startup.
   - **MacOS/Linux:** Add the script to your `crontab` or as a Startup Application (optional, you can use any other method to run the script at startup).

## ⚙️ Usage
1. **Run the Script:** You can start the script manually to ensure everything's working:
   ```bash
   python3 oblivion.py
**The script will:**

    1. Check if the current date is on or after the specified delete date.
    2. If true, it attempts to delete the specified folder and logs the outcome.
    3. If the specified folder does not exist, it logs that information instead.

2. **Ensure Logging:** A log file will be created in the `log_file` path directory to keep track of actions taken by the script.

## 💬 Disclaimer
- This script is **not** responsible for any oversight or accidental deletions. Use it wisely and ensure you are deleting what you truly want gone!
- Only delete folders that currently hold secrets you don’t want retrieved. No regrets!

## 🤖 Conclusion
Now you can embark on your one-way journey with the peace of mind that your secrets are safe and set to evaporate on a date of your choosing!

For the curious souls out there, feel free to contribute, request features!

Stay adventurous and keep your secrets close— unless you’ve got End Game. 😉
<div align=left height=200>
    <img src="https://i.ibb.co/LCrNwdT/respect.png">
</div>

## License
This project is licensed under the MIT License.