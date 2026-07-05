from pages.homepage import HomePage

def test_contact_us_form(page_fixture):
    home_page = HomePage(page_fixture)

    home_page.navigate_to_homepage()
    home_page.assert_navigation_to_homepage()
    contact_us_page = home_page.navigate_to_contact_us_page()

    contact_us_page.verify_contact_us_headings()
    contact_us_page.fill_details_and_submit_form()

    home_page = contact_us_page.verify_details_submitted_successfully_and_return_to_homepage()
    home_page.assert_navigation_to_homepage()