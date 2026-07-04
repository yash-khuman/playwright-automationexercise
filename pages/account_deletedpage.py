from playwright.sync_api import Page, expect
from pages.homepage import HomePage

class AccountDeletedPage:

    def __init__(self, page : Page):
        self.page = page
        self.account_deleted = page.get_by_text("Account Deleted!")
        self.continue_button = page.get_by_role("link", name="Continue")


    def assert_account_deleted_heading(self):
        expect(self.account_deleted).to_be_visible()

    def navigate_to_homepage(self) -> HomePage:
        self.continue_button.click()
        self.page.wait_for_load_state('domcontentloaded')

        return HomePage(self.page)