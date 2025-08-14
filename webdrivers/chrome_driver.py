from selenium import webdriver


def setup_webdriver():
    """Sets up the Selenium WebDriver with required options."""
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--disable-notifications")
    return webdriver.Chrome(options=chrome_options)
