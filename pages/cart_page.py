from playwright.sync_api import Page,expect,Locator
from test_data.users import main_user


class Cart:

    def __init__(self, page : Page):
        self.page = page
        self._subscription_heading = page.get_by_role("heading", name="Subscription")
        self._subscription_email = page.get_by_role("textbox", name="Your email address")
        self._subscribe_arrow = page.locator("#subscribe")
        self._subscription_success_message = page.get_by_text("You have been successfully")

        self.items = page.locator("#cart_info_table tbody > tr")

        self.signup_login_link = page.get_by_role("link", name=" Signup / Login")

        self.cart_heading = page.get_by_text("Shopping Cart")



    
    def navigate_to_loginpage(self):
        from pages.loginpage import LoginPage
        self.signup_login_link.click()
        self.page.wait_for_load_state('domcontentloaded')

        return LoginPage(self.page)

    def cartitem_by_index(self, index : int) -> "CartItem":

        count = self.items.count()
        #print(count)
        if index < 1 or index > count:
            raise ValueError(f"product index must be between 1 and {count}")
        
        cartitem_locator = self.items.nth(index-1)

        return CartItem(row_locator=cartitem_locator,page=self.page)

    def verify_cart_heading(self):
        expect(self.cart_heading).to_be_visible()


    def subscribe_with_email(self,email : str = main_user.email) -> None:
        expect(self._subscription_heading).to_be_visible()
        self._subscription_email.fill(email)
        self._subscribe_arrow.click()
        expect(self._subscription_success_message).to_be_visible(timeout=30000)

    
    def get_all_items(self) -> list["CartItem"]:

        all_items = []
        for i in range(self.items.count()):
            all_items.append(CartItem(row_locator=self.items.nth(i),page=self.page))

        return all_items



class CartItem:

    def __init__(self, row_locator : Locator, page : Page):
        self._page = page
        self._root = row_locator
        self._category = self._root.locator(".cart_description p")
        self._price = self._root.locator(".cart_price p")
        self._quantity = self._root.locator(".cart_quantity button")
        self._total = self._root.locator(".cart_total .cart_total_price")
        self._delete_button = self._root.locator(".cart_quantity_delete")
        self._name = self._root.locator(".cart_description h4")

    @property
    def product_id(self) -> str:
        return self._delete_button.get_attribute("data-product-id")

    @property
    def name(self) -> str:
        return " ".join(self._name.inner_text().split())
    
    def remove_item(self) -> None:
        self._delete_button.click()
        self._root.wait_for(state="detached")
        
    
    @property
    def price(self) -> str:
        return self._price.inner_text()
    
    def verify_name(self, expected_name : str) -> None:
        expect(self._name).to_have_text(expected_name)

    @property
    def quantity(self) -> str:
        return self._quantity.inner_text()
    
    @property
    def total(self) -> str:
        return self._total.inner_text()
    
    
        
        