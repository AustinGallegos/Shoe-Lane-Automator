import handlers as h
from webdrivers import chrome_driver as c


def main():
    eligible = h.get_eligible()
    h.write_output(eligible)

    driver = c.setup_webdriver()
    h.control_tower(eligible, driver)
    driver.quit()


if __name__ == "__main__":
    main()
