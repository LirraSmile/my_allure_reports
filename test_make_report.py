import random

link = "http://selenium1py.pythonanywhere.com"



class TestGuestCanRegister():
        def test_guest_can_go_to_login_page(self, browser):

            new_user_email = 'Tester{}'.format(random.randint(1,1000000))
            new_user_pass = 'abc{}'.format(random.randint(1,100000))

            page = ProductPage(browser, link)
            page.open()
            page.should_be_login_link()
            page.go_to_login_page()
            login_page = LoginPage(browser, browser.current_url)
            login_page.register_new_user(new_user_email, new_user_pass)