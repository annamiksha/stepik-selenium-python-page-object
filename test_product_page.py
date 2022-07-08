from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    product_name = page.get_product_name()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.check_appeared_messages()
    page.check_product_name_in_success_message(product_name)
