from playwright.sync_api import Page,expect
from pages.homepage import HomePage

class AccountCreatedPage:
    
    def __init__(self,page : Page):
        self.page = page
        self.account_created = page.get_by_text("Account Created!")
        self.continue_button = page.get_by_role("link", name="Continue")
    
    def check_if_account_create(self):
        expect(self.account_created).to_be_visible()

    def navigate_to_homepage(self) -> HomePage:
        self.continue_button.click()
        self.page.wait_for_load_state()

        return HomePage(self.page)