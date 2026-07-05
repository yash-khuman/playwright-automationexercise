from pages.homepage import HomePage

def test_verify_test_cases_page(page_fixture):
    home_page = HomePage(page_fixture)

    home_page.navigate_to_homepage()
    home_page.assert_navigation_to_homepage()
    test_cases_page = home_page.navigate_to_test_cases_page()

    test_cases_page.verify_test_cases_headings()