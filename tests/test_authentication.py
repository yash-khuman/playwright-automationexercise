from playwright.sync_api import expect
from pages.homepage import HomePage
from utils.helpers import Helper
from test_data.users import temp_user,main_user


def test_register_user(page_fixture,worker_id):
    first_name = temp_user.username
    email = temp_user.email

    page_fixture.goto("https://automationexercise.com/")
    home_page = HomePage(page_fixture)

    Helper.close_ads(home_page.page)

    home_page.assert_navigation_to_homepage()
    login_page = home_page.navigate_to_loginpage()
    login_page.verify_loginpage_headings()

    login_page.fill_name_email_and_click_signup(first_name,email)
    login_page.verify_enter_account_information_heading()
    account_created_page = login_page.fill_user_information_and_create_account(
        password = "operation123",
        first_name = first_name,
        last_name = "lala",
        company_name = "heloocomp",
        address1 = "wqee",
        address2 = "wqwq",
        mobile_number = "1092890919",
        zip_code = "234567",
    )

    account_created_page.check_if_account_create()
    home_page = account_created_page.navigate_to_homepage()
    home_page.identify_current_username(first_name)
    account_deleted_page = home_page.delete_account()

    account_deleted_page.assert_account_deleted_heading()
    account_deleted_page.navigate_to_homepage()


def test_login_User_with_correct_email_and_password(page_fixture):

    home_page = HomePage(page_fixture)
    
    home_page.navigate_to_homepage()
    home_page.assert_navigation_to_homepage()
    login_page = home_page.navigate_to_loginpage()

    login_page.verify_loginpage_headings()
    home_page = login_page.login(main_user.email,main_user.password)

    home_page.identify_current_username(main_user.username)
    

def test_login_user_with_incorrect_email_and_password(page_fixture):

    home_page = HomePage(page_fixture)

    home_page.navigate_to_homepage()
    login_page = home_page.navigate_to_loginpage()

    login_page.verify_loginpage_headings()

    login_page.login_with_email.fill(main_user.email)
    login_page.login_with_password.fill("incorrect_password")
    login_page.login_button.click()

    login_page.page.wait_for_load_state()

    expect(login_page.email_or_password_is_incorrect).to_be_visible(timeout=20000)

    login_page.verify_loginpage_headings()
        
