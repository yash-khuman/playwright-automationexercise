from pages.homepage import HomePage

def test_verify_subscription_in_home_page(page_fixture):
    home_page = HomePage(page_fixture)

    home_page.navigate_to_homepage()
    home_page.assert_navigation_to_homepage()

    home_page.subscribe_with_email()