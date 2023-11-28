from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from Data26 import data
from Locator26 import locator

class Imdb_Search:

    def __init__(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 40)
        self.action = ActionChains(self.driver)
        self.locator = locator.Imdb_Locator()



    def access_data(self):
        try:
            self.driver.maximize_window()
            self.driver.get(data.Imdb_Data().url)

            # Scroll the expand element into view and click it
            expand = self.wait.until(EC.presence_of_element_located((By.XPATH, locator.Imdb_Locator().expan_xpath)))
            self.driver.execute_script("arguments[0].scrollIntoView();", expand)
            self.driver.execute_script("arguments[0].click();", expand)

            Name = self.wait.until(EC.visibility_of_element_located((By.ID, locator.Imdb_Locator().name_id)))
            self.driver.execute_script("arguments[0].scrollIntoView();", Name)
            Name.send_keys(data.Imdb_Data().name_da)

            # Fill in the Birth Min field
            Birth_min = self.wait.until(EC.visibility_of_element_located((By.ID, locator.Imdb_Locator().bd_min_id)))
            Birth_min.send_keys(data.Imdb_Data().bd_min_da)

            # Fill in the Birth Max field
            Birth_max = self.wait.until(EC.visibility_of_element_located((By.ID, locator.Imdb_Locator().bd_max_id)))
            Birth_max.send_keys(data.Imdb_Data().bd_max_da)

            # Fill in the Birth Day field
            Birth_day = self.wait.until(EC.visibility_of_element_located((By.ID, locator.Imdb_Locator().bd_day_id)))
            Birth_day.send_keys(data.Imdb_Data().bd_day)

            # Click the Apply/Refresh button
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Imdb_Locator().aw_re_path))).click()


            # # Use Select class to select the value in the dropdown
            # sear_top = self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Imdb_Locator().sear_top_xpath)))
            # self.driver.execute_script("arguments[0].scrollIntoView(true);", sear_top)
            # drop = Select(sear_top)
            # drop.select_by_visible_text(locator.Imdb_Locator().sear_opt_value)


            # Click the Gender button
            Gen_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Imdb_Locator().gen_path)))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", Gen_button)
            Gen_button.click()


            # Click the Add Name Filter checkbox
            check = self.wait.until(EC.element_to_be_clickable((By.ID, locator.Imdb_Locator().ad_name_ch_id)))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", check)
            check.click()
            # Click the Search button
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Imdb_Locator().search_path))).click()
            print("searched")

        except TimeoutException as e:
            print(f"Timeout Exception: {e}")
        except NoSuchElementException as e:
            print(f"No Such Element Exception: {e}")
        except Exception as e:
            print(f"Other Exception: {e}")
        finally:
            self.driver.quit()



# Instantiate and run the script
re = Imdb_Search()
re.access_data()
