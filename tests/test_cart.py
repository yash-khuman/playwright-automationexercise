from pages.homepage import HomePage
from test_data.users import main_user

def test_verify_subscription_in_cart_page(page_fixture):
    home_page = HomePage(page_fixture)

    home_page.navigate_to_homepage()
    home_page.assert_navigation_to_homepage()
    cart_page = home_page.navigate_to_cart_page()

    cart_page.verify_cart_heading()
    cart_page.subscribe_with_email()

    

def test_add_products_in_cart(page_fixture):
    home_page = HomePage(page_fixture)

    home_page.navigate_to_homepage()
    home_page.assert_navigation_to_homepage()

    products_page = home_page.navigate_to_products_page()
    products_page.verify_all_products_headings()

    product1 = products_page.product_by_index(1)
    product1_name = product1.name
    product1_price = product1.price
    add_to_cart_modal = product1.add_to_cart()
    products_page = add_to_cart_modal.continue_shopping()

    product2 = products_page.product_by_index(2)
    product2_name = product2.name
    product2_price = product2.price
    add_to_cart_modal = product2.add_to_cart()
    
    cart_page = add_to_cart_modal.view_cart()
    cart_page.verify_cart_heading()
    cartitem1 = cart_page.cartitem_by_index(1)
    cartitem2 = cart_page.cartitem_by_index(2)

    print(f"product 2 name : {product2_name}")
    print(f"cartitem 2 name : {cartitem2.name}")

    assert cartitem1.name == product1_name
    assert cartitem1.price == product1_price
    assert cartitem2.name == product2_name
    assert cartitem2.price == product2_price
    #because we only added each product one time so quantity will be 1 
    assert cartitem1.total == product1_price
    assert cartitem2.total == product2_price



def test_verify_product_quantity_in_cart(page_fixture):
    home_page = HomePage(page_fixture)

    home_page.navigate_to_homepage()
    home_page.assert_navigation_to_homepage()

    product1 = home_page.product_by_index(1)
    product1_details = product1.view_product()
    
    product1_name = product1_details.name
    product1_details.set_quantity(value="4")

    add_to_cart_modal = product1_details.add_to_cart()
    cart_page = add_to_cart_modal.view_cart()

    cartitem1 = cart_page.cartitem_by_index(1)

    assert cartitem1.name == product1_name
    assert cartitem1.quantity == "4"
    

def test_remove_products_from_cart(page_fixture):
    home_page = HomePage(page_fixture)

    home_page.navigate_to_homepage()
    home_page.assert_navigation_to_homepage()

    product1 = home_page.product_by_index(1)
    add_to_cart_modal = product1.add_to_cart()

    cart_page = add_to_cart_modal.view_cart()
    cartitem1 = cart_page.cartitem_by_index(1)
    cartitem1.remove_item()
    remaining_items = cart_page.get_all_items()

    assert len(remaining_items) == 0


def test_search_products_and_verify_cart_after_login(page_fixture):

    home_page = HomePage(page_fixture)

    home_page.navigate_to_homepage()
    home_page.assert_navigation_to_homepage()

    products_page = home_page.navigate_to_products_page()
    products_page.verify_all_products_headings()

    products_page.search_products_by_value("blue")
    all_products = products_page.get_all_products()

    # Verify all the products related to search are visible
    # Add those products to cart
    product_ids = []
    for product in all_products:
        assert "blue" in product.name.lower()

        product_ids.append(product.product_id)
        add_to_cart_modal = product.add_to_cart()
        add_to_cart_modal.continue_shopping()

    #print(all_products[1]._name.evaluate("e => e.outerHTML"))

    # Click 'Cart' button and verify that products are visible in cart
    cart_page = products_page.navigate_to_cart_page()

    all_cartitems = cart_page.get_all_items()
    for i in range(len(all_cartitems)):
        cart_item = all_cartitems[i]
        #print(f"cartitem name = {cart_item.name} && product name = {product_names[i]}")
        
        assert cart_item.product_id == product_ids[i]

    # Click 'Signup / Login' button and submit login details

    login_page = cart_page.navigate_to_loginpage()
    home_page = login_page.login(email=main_user.email, password=main_user.password)

    # Again, go to Cart page

    cart_page = home_page.navigate_to_cart_page()

    # Verify that those products are visible in cart after login as well

    all_cartitems = cart_page.get_all_items()
    for i in range(len(all_cartitems)):
        cartitem = all_cartitems[i]
        assert cartitem.product_id == product_ids[i]

    

    



