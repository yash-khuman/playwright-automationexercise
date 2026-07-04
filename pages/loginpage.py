from playwright.sync_api import Page,expect
from utils.helpers import Helper



class LoginPage:

    def __init__(self,page : Page):
        self.page = page
        self.new_user_signup_heading = page.get_by_role("heading", name="New User Signup!")
        self.login_to_your_account_heading = page.get_by_role("heading", name="Login to your account")
        self.signup_with_name = page.get_by_role("textbox", name="Name")
        self.signup_with_email = page.locator("form").filter(has_text="Signup").get_by_placeholder("Email Address")
        self.sigup_button = page.get_by_role("button", name="Signup")

        self.enter_account_information_heading = page.get_by_text("Enter Account Information")
        self.MR_radio = page.get_by_role("radio", name="Mr.")
        self.password = page.get_by_role("textbox", name="Password *")
        self.birth_date = page.locator("#days")
        self.birth_month = page.locator("#months")
        self.birth_year = page.locator("#years")
        self.signup_for_our_newsletter_checkbox = page.get_by_role("checkbox", name="Sign up for our newsletter!")
        self.Receive_special_offers_from_checkbox = page.get_by_role("checkbox", name="Receive special offers from")
        self.first_name = page.get_by_role("textbox", name="First name *")
        self.last_name = page.get_by_role("textbox", name="Last name *")
        self.company_name = page.get_by_role("textbox", name="Company", exact=True)
        self.address1 = page.get_by_role("textbox", name="Address * (Street address, P.")
        self.address2 = page.get_by_role("textbox", name="Address 2")
        self.state_name = page.get_by_role("textbox", name="State *")
        self.city_name = page.get_by_role("textbox", name="City * Zipcode *")
        self.zip_code = page.locator("#zipcode")
        self.mobile_number = page.get_by_role("textbox", name="Mobile Number *")
        self.create_account_button = page.get_by_role("button", name="Create Account")
        self.login_button = page.get_by_role("button", name="Login")
        self.login_with_email = page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address")
        self.login_with_password = page.get_by_role("textbox", name="Password")

    def login(self,email : str,password : str):
        from pages.homepage import HomePage
        self.login_with_email.fill(email)
        self.login_with_password.fill(password)
        self.login_button.click()
        self.page.wait_for_load_state('domcontentloaded')
        
        Helper.close_ads(self.page)
        return HomePage(self.page)


    def verify_loginpage_headings(self):
        expect(self.login_to_your_account_heading).to_be_visible(timeout=20000)
        expect(self.new_user_signup_heading).to_be_visible()

    def fill_name_email_and_click_signup(self,name : str,email : str):
        self.signup_with_name.fill(name)
        self.signup_with_email.fill(email)
        self.sigup_button.click()
        self.page.wait_for_load_state('domcontentloaded')

    def verify_enter_account_information_heading(self):
        expect(self.enter_account_information_heading).to_be_visible(timeout=10000)

    def fill_user_information_and_create_account(
    self,
    password : str,
    first_name : str,
    last_name : str,
    company_name : str,
    address1 : str,
    address2 : str,
    mobile_number : str = "0011100",
    zip_code : str = "380060",
    city : str = "ahmedabad",
    state : str = "gujrat",
    is_male : bool = True,
    birth_date : str = "1",
    birth_month : str = "1",
    birth_year : str = "2000",
    sign_up_for_our_newsletter : bool = True,
    receive_special_offers_from : bool = True
    ):
        from pages.account_createdpage import AccountCreatedPage

        if is_male:
            self.MR_radio.check()
        
        self.password.fill(password)
        self.birth_date.select_option(birth_date)
        self.birth_month.select_option(birth_month)
        self.birth_year.select_option(birth_year)

        if sign_up_for_our_newsletter:
            self.signup_for_our_newsletter_checkbox.check()
        if receive_special_offers_from:
            self.Receive_special_offers_from_checkbox.check()

        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.company_name.fill(company_name)
        self.address1.fill(address1)
        self.address2.fill(address2)
        self.state_name.fill(state)
        self.city_name.fill(city)
        self.zip_code.fill(zip_code)
        self.mobile_number.fill(mobile_number)

        self.create_account_button.click()
        self.page.wait_for_load_state('domcontentloaded')

        return AccountCreatedPage(self.page)

        



    

    