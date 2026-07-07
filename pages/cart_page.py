from playwright.sync_api import Page,expect
from test_data.users import main_user


class Cart:

    def __init__(self, page : Page):
        self.page = page
        self._subscription_heading = page.get_by_role("heading", name="Subscription")
        self._subscription_email = page.get_by_role("textbox", name="Your email address")
        self._subscribe_arrow = page.locator("#subscribe")
        self._subscription_success_message = page.get_by_text("You have been successfully")

        self.cart_heading = page.get_by_text("Shopping Cart")

    def verify_cart_heading(self):
        expect(self.cart_heading).to_be_visible()


    def subscribe_with_email(self,email : str = main_user.email) -> None:
        expect(self._subscription_heading).to_be_visible()
        self._subscription_email.fill(email)
        self._subscribe_arrow.click()
        expect(self._subscription_success_message).to_be_visible(timeout=30000)