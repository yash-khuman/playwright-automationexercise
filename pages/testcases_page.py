from playwright.sync_api import Page,expect

class TestCases:

    def __init__(self, page : Page):
        self.page = page
        self.test_cases_heading = page.get_by_role("heading", name="Test Cases", exact=True)

    def verify_test_cases_headings(self):
        expect(self.test_cases_heading).to_be_visible()