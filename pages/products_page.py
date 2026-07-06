from playwright.sync_api import Page,expect,Locator
from utils.helpers import Helper

class ProductPage:
    
    def __init__(self, page : Page):
        self.page = page
        self.all_products_heading = page.get_by_role("heading", name="All Products")
        self.products = page.locator(".product-image-wrapper")
        self._search_textbox = page.get_by_role("textbox", name="Search Product")
        self._search_button = page.locator("#submit_search")


    def verify_all_products_headings(self):
        expect(self.all_products_heading).to_be_visible()

    def search_products_by_value(self, search_value : str) -> None:
        self._search_textbox.fill(search_value)
        self._search_button.click()
        Helper.close_ads(self.page)
        self.page.wait_for_load_state()

    def product_by_index(self, index : int) -> "ProductCard":

        count = self.products.count()
        if index < 1 or index > count:
            raise ValueError(f"product index must be between 1 and {count}")
        
        product_locator = self.products.nth(index-1)

        return ProductCard(product_locator=product_locator,page=self.page)
    
    def get_all_products(self) -> list["ProductCard"]:

        all_products = []
        for i in range(self.products.count()):
            all_products.append(ProductCard(product_locator=self.products.nth(i),page=self.page))

        return all_products




class ProductCard:

    def __init__(self, product_locator : Locator,page : Page):
        self.root = product_locator

        self._page = page
        self._view_product_link = self.root.locator(".choose").get_by_role("link",name="View Product")
        self._overlay_add_to_cart_link = self.root.locator(".product-overlay").get_by_role("link",name="Add to cart")
        self._add_to_cart_link = self.root.locator(".productinfo.text-center").get_by_role("link",name="Add to cart")
        self._price = self.root.locator(".productinfo.text-center h2")
        self._name = self.root.locator(".productinfo.text-center p")


    def add_to_cart(self):
        self.root.hover()
        self._overlay_add_to_cart_link.click()

    def view_product(self) -> "ProductDetails":
        self._view_product_link.click()
        Helper.close_ads(self._page)
        self._page.wait_for_load_state('domcontentloaded')

        return ProductDetails(self._page)

    @property
    def name(self) -> str:
        return self._name.inner_text()
    
    @property
    def price(self) -> str:
        return self._price.inner_text()
    
    def verify_name(self, expected_name : str) -> None:
        expect(self._name).to_have_text(expected_name)


class ProductDetails:

    def __init__(self,page : Page):
        self.page = page
        self._root = page.locator(".product-information")
        self._name = self._root.locator("h2")
        self._category = self._root.locator("p").filter(has_text="Category:")
        self._availability = self._root.locator("p").filter(has_text="Availability:")
        self._brand = self._root.locator("p").filter(has_text="Brand:")
        self._condition = self._root.locator("p").filter(has_text="Condition:")
        self._price = self._root.locator("span").locator("span")

    @property
    def name(self) -> str:
        return self._name.inner_text()

    def verify_product_details_is_visible(self) ->None:
        expect(self._name).to_be_visible()
        expect(self._category).to_be_visible()
        expect(self._availability).to_be_visible()
        expect(self._condition).to_be_visible()
        expect(self._price).to_be_visible()
        expect(self._brand).to_be_visible()

    





    
        
