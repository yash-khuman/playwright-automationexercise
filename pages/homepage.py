from playwright.sync_api import Page,expect
from utils.helpers import Helper

class HomePage:

    def __init__(self, page : Page):
        self.page = page
        self.homepage_heading = page.get_by_role("heading", name="AutomationExercise")
        self.signup_login_link = page.get_by_role("link", name=" Signup / Login")
        self.delete_account_button = page.get_by_role("link", name=" Delete Account")
        self.logout_link = page.get_by_role("link", name=" Logout")
        self.contact_us_link = page.get_by_role("link", name=" Contact us")

        self.test_cases_link = page.get_by_role("link", name=" Test Cases")

        self.products_link = page.get_by_role("link", name=" Products")

    def navigate_to_products_page(self):
        from pages.products_page import ProductPage

        self.products_link.click()
        Helper.close_ads(self.page)
        self.page.wait_for_load_state('domcontentloaded')

        return ProductPage(self.page)


    def navigate_to_test_cases_page(self):
        from pages.testcases_page import TestCases

        self.test_cases_link.click()
        Helper.close_ads(self.page)
        self.page.wait_for_load_state('domcontentloaded')

        return TestCases(self.page)

    def navigate_to_contact_us_page(self):
        from pages.contact_us_page import ContactUs

        self.contact_us_link.click()
        self.page.wait_for_load_state('domcontentloaded')
        Helper.close_ads(self.page)
        

        return ContactUs(self.page)



    def logout(self):
        from pages.loginpage import LoginPage

        self.logout_link.click()
        self.page.wait_for_load_state('domcontentloaded')

        return LoginPage(self.page)
    

    def navigate_to_homepage(self):
        self.page.goto("https://automationexercise.com/")
        self.page.wait_for_load_state('domcontentloaded',timeout=50000)

    def identify_current_username(self,expected_username : str):
        expect(self.page.get_by_text(f"Logged in as {expected_username}")).to_be_visible()

    def delete_account(self):
        from pages.account_deletedpage import AccountDeletedPage
        from utils.helpers import Helper

        self.delete_account_button.click()
        Helper.close_ads(self.page)
        self.page.wait_for_load_state('domcontentloaded')

        return AccountDeletedPage(self.page)


    def assert_navigation_to_homepage(self):
        expect(self.homepage_heading).to_be_visible(timeout=20000)

    def navigate_to_loginpage(self):
        from pages.loginpage import LoginPage
        self.signup_login_link.click()
        self.page.wait_for_load_state('domcontentloaded')

        return LoginPage(self.page)