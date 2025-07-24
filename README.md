# EvilTester’s To-Do List Automation Testing
This project automates testing of EvilTester’s Simple To-Do List Application using Python and Selenium WebDriver. The scripts validate task creation, editing, completion, and deletion.

# Tools Used

- Python 3.8+: Programming language for scripting automation tests.
- Selenium WebDriver: Browser automation framework to interact with the web application.
- Webdriver_manager: Automatically manages browser drivers.
- Chrome Browser (v138.0): Target browser for testing on Windows 11 at 1920x1080 resolution.

# Steps To Run Automation

1 - Setup Environment :

  Install Python 3.8+ from python.org.
  Install required packages:
  
```bash
pip install selenium webdriver-manager
```

 2 - Prepare files : 
  Ensure TODOs_task.py, functions.py, and config.py are in the same directory.
  Verify config.py has correct values

3 - Run the script : 
  Open a terminal in the project directory.
  ```bash
python TODOs_task.py
```
The script will:
 - Open the web application
 - Add a new to-do item
 - Mark it as completed
 - Delete the item
 - Note : time.sleep(1) for visibility in screen recordings.

4 - Assumptions Made :
  EvilTester’s To-Do List web application was chosen as it's a lightweight To-Do list app built with HTML, JavaScript, and Local Browser Storage. It includes bugs and automation challenges, making it perfect for the required.
