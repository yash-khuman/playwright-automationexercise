from pages.homepage import HomePage

def test_verify_all_products_and_product_detail_page(page_fixture):
    home_page = HomePage(page_fixture)

    home_page.navigate_to_homepage()
    home_page.assert_navigation_to_homepage()
    products_page = home_page.navigate_to_products_page()

    products_page.verify_all_products_headings()
    product = products_page.product_by_index(1)

    product_details = product.view_product()

    product_details.verify_product_details_is_visible()


