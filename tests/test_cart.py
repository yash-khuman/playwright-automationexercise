from pages.homepage import HomePage

def test_verify_subscription_in_cart_page(page_fixture):
    home_page = HomePage(page_fixture)

    home_page.navigate_to_homepage()
    home_page.assert_navigation_to_homepage()
    cart_page = home_page.navigate_to_cart_page()

    cart_page.verify_cart_heading()
    cart_page.subscribe_with_email()