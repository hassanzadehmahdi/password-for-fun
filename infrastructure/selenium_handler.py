from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class SeleniumHandler:
    def __init__(self, url):
        self.driver = webdriver.Chrome()  # Or any other WebDriver
        self.driver.get(url)
        time.sleep(3)  # Allow page to load

    def handle_consent_dialog(self):
        """Handle the consent dialog by clicking the 'Consent' button."""
        try:
            # Wait for the consent button to appear and be clickable
            consent_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "fc-cta-consent"))
            )
            consent_button.click()
            print("Consent accepted.")
            time.sleep(1)  # Allow the page to update
        except Exception as e:
            print("Consent dialog not found or already handled.")

    def start_game(self, initial_character="a"):
        """Enter an initial character to start the game."""
        try:
            password_box = self.driver.find_element(By.CLASS_NAME, "password-box")
            prose_mirror = password_box.find_element(By.CLASS_NAME, "ProseMirror")
            prose_mirror.send_keys(initial_character)
            time.sleep(1)  # Allow rules to load
        except Exception as e:
            print(f"Error starting the game: {e}")

    def get_current_password(self):
        """Fetch the current password from the password box."""
        try:
            password_box = self.driver.find_element(By.CLASS_NAME, "password-box")
            prose_mirror = password_box.find_element(By.CLASS_NAME, "ProseMirror")
            password_paragraph = prose_mirror.find_element(By.TAG_NAME, "p")
            return password_paragraph.text.strip()
        except Exception as e:
            print(f"Error fetching password: {e}")
            return ""

    def get_all_rules(self):
        """Fetch all current rules and organize messages in a dictionary."""
        try:
            # Locate all rule-inner elements
            rule_inners = self.driver.find_elements(By.CLASS_NAME, "rule-inner")

            # Initialize the dictionary
            rules_dict = {"true_messages": [], "false_messages": []}

            for rule_inner in rule_inners:
                # Locate the image within rule-top
                img_element = rule_inner.find_element(By.CLASS_NAME, "rule-top").find_element(By.TAG_NAME, "img")
                img_src = img_element.get_attribute("src")

                # Determine the rule status based on the image src
                rule_status = True if "checkmark.svg" in img_src else False

                # Get the rule description text
                rule_desc = rule_inner.find_element(By.CLASS_NAME, "rule-desc").text.strip()

                # Append the message to the appropriate list in the dictionary
                if rule_status:
                    rules_dict["true_messages"].append(rule_desc)
                else:
                    rules_dict["false_messages"].append(rule_desc)

            return rules_dict
        except Exception as e:
            print(f"Error fetching rules: {e}")
            return {"true_messages": [], "false_messages": []}

    def update_password(self, new_password):
        """Update the password by appending a new character or text."""
        try:
            password_box = self.driver.find_element(By.CLASS_NAME, "password-box")
            prose_mirror = password_box.find_element(By.CLASS_NAME, "ProseMirror")

            # Select all existing text and clear it
            prose_mirror.send_keys(Keys.CONTROL + 'a')  # For Windows/Linux
            prose_mirror.send_keys(Keys.DELETE)  # Delete all text

            prose_mirror.send_keys(new_password)
            time.sleep(1)  # Allow UI to process
        except Exception as e:
            print(f"Error updating password: {e}")

    def close(self):
        self.driver.quit()


if __name__ == "__main__":
    selenium_handler = SeleniumHandler("https://neal.fun/password-game/")
    selenium_handler.handle_consent_dialog()
    selenium_handler.start_game()
    print(selenium_handler.get_current_password())
    print(selenium_handler.get_all_rules())
    selenium_handler.update_password("123456")
    print(selenium_handler.get_current_password())
    print(selenium_handler.get_all_rules())
    time.sleep(5)
    selenium_handler.close()
