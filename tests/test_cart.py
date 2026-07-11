from pages.homepage import HomePage

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
    
