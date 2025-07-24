"""
Script Name: TODOs_task.py
Author: Omar Mohsen
Date: 2025-07-24
Purpose: Automate task Creation, Editing, Completion, and Deletion in EvilTester’s Simple To-Do List Application
Dependencies: functions.py, config.py, Time
Comments: time.sleep(1) is added for visibility
"""
import functions
import config
import time

# time sleep wait for visibility
wait = 1

if __name__ == "__main__":

    # Initialization and launch of chrome and Opening the web application
    driver = functions.setup_and_launch_chrome(config.Implicit_wait,config.baseurl)
    try:
        time.sleep(wait)
        # 1 - Add a new to-do item
        # Finding Input field by class name
        functions.class_name_finder(driver,"new-todo-list",config.task_name)
        time.sleep(wait)
        # 2 - Mark it as completed
        # First Hover to task edit page, add a new sub-task to be able to see task edit options,
        # Mark the sub tasks as complete

        # Hovering to [use] hyperlink for Task edit page by using the website task handler along with task name
        functions.css_selector_clicker(driver,f"a[href='{config.use_hyperlink}']")
        time.sleep(wait)
        # Finding Input field by Its Css Selector
        functions.css_selector_finder(driver,"body > section > header > input",config.subtask_name)
        time.sleep(wait)
        # Find Mark-All-As-Complete button by its class name
        functions.class_name_clicker(driver,"toggle-all")
        time.sleep(wait)

        # 3 - Delete the item

        # Delete sub-task then go back to Homepage and delete the Task
        functions.class_name_clicker(driver,"destroy")
        time.sleep(wait)
        # Go back to HomePage
        driver.get(config.baseurl)
        time.sleep(wait)
        # find delete button of our task by going to lists 'li' & search by attribute data-id then
        # > div > reach button with class destroy
        functions.css_selector_clicker(driver,f"li[data-id='{config.task_name}'] > div > button.destroy")
        time.sleep(wait)
        # accept alert when pops
        functions.accept_alert(driver)
        time.sleep(wait)

    finally:
        # clean Closure
        driver.quit()
