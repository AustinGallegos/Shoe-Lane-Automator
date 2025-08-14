import os
import sys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException


def control_tower(logins, driver, *, process="CR Shoe Process"):
    search_bar = get_search_bar(driver)
    try:
        enter_logins(search_bar, driver, logins, process)
    except NoSuchElementException:
        print(f"Couldn't find {process}, is it named correctly?")


def get_search_bar(driver):
    """Gets and returns the search bar from Control Tower"""
    max_time = sys.maxsize
    wait = WebDriverWait(driver, timeout=max_time)
    driver.get(os.getenv("CT_LINK"))
    driver.maximize_window()
    search_bar = wait.until(ec.presence_of_element_located(
        (By.XPATH, "//input[@placeholder='Search for login, id, etc.']")
    ))
    time.sleep(3)
    return search_bar


def enter_logins(search_bar, driver, logins, process):
    """Enters logins into search bar and gives shoe process qualifications on Control Tower"""
    for login in logins:
        search_bar.send_keys(login)

        try:
            row = driver.find_element(By.XPATH, f"//tr[.//td//span[text()='{login}']]")
        except NoSuchElementException:
            print(f"couldn't find {login}, do they still work here?")
        else:
            check_box = row.find_element(By.TAG_NAME, "svg")
            check_box.click()
            try:
                give_qualification(driver, process)
            except NoSuchElementException:
                raise NoSuchElementException
            else:
                check_box.click()
        finally:
            driver.find_element(By.CSS_SELECTOR, "button[aria-label='Clear search']").click()


def give_qualification(driver, process):
    """Ensures the specified qualifications are assigned to a user by interacting with the web UI."""
    driver.find_element(By.XPATH, "//button[text()='Edit']").click()
    time.sleep(0.5)

    try:
        row = driver.find_element(By.XPATH, f"//tr[.//td//span[text()='{process}']]")

        input_element = row.find_element(By.TAG_NAME, "input")
        is_checked = input_element.get_attribute("aria-checked")
        is_checked = is_checked.lower() == "true"

        if not is_checked:
            row.find_element(By.TAG_NAME, "svg").click()
    except NoSuchElementException:
        raise NoSuchElementException
    finally:
        driver.find_element(By.XPATH, "//span[text()='Save']").click()
        