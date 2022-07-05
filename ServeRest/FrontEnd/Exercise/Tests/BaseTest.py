import pytest
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

@pytest.mark.usefixtures("driver_init")
class BaseTest:
    
    def chrome_driver_init(
        self, executable_path="../Webdrivers/chromedriver"
    ):
        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-extensions")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--start-maximized")

        desired_capabilities = DesiredCapabilities.CHROME
        desired_capabilities["loggingPrefs"] = {"browser": "ALL"}
        self.driver = webdriver.Chrome(
            options=options,
            desired_capabilities=desired_capabilities,
            executable_path=executable_path,
        )
        self.driver.get("https://front.serverest.dev/login")
        return self.driver
    
    pass
