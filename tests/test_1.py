from pages.homepage import HomePage
from utils.helpers import Helper
from test_data.users import temp_user


def test_1(page_fixture,worker_id):
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


