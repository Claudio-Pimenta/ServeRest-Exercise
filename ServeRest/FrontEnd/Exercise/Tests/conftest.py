from BaseTest import BaseTest
import pytest

class conftest(BaseTest):
    @pytest.fixture(scope="session")
    def driver_init(self):
        self.web_driver = self.chrome_driver_init()
        yield self.web_driver
        self.web_driver.close()