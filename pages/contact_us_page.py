from playwright.sync_api import Page,expect
from test_data.users import fake,main_user
from utils.helpers import Helper

class ContactUs:

    def __init__(self, page : Page):
        self.page = page
        self.contact_us_heading = page.get_by_role("heading", name="Contact Us")
        self.get_in_touch_heading = page.get_by_role("heading", name="Get In Touch")
        self.name = page.get_by_role("textbox", name="Name")
        self.email = page.get_by_role("textbox", name="Email", exact=True)
        self.subject = page.get_by_role("textbox", name="Subject")
        self.message = page.get_by_role("textbox", name="Your Message Here")
        self.choose_file_button = page.get_by_role("button", name="Choose File")
        self.submit_button = page.get_by_role("button", name="Submit")
        self.home_button = page.get_by_role("link", name=" Home")
        self.your_details_have_submitted_successfully = page.locator("#contact-page").get_by_text("Success! Your details have")

    def verify_contact_us_headings(self):
        
        expect(self.get_in_touch_heading).to_be_visible(timeout=30000)
        expect(self.contact_us_heading).to_be_visible(timeout=10000)
        
    def upload_file(self,file_name : str):
        with self.page.expect_file_chooser() as fc_info:
            self.choose_file_button.click()
        
        file_chooser = fc_info.value
        file_chooser.set_files(Helper.get_test_file(file_name))


    def fill_details_and_submit_form(
        self,
        name : str = main_user.username,
        email : str = main_user.email,
        subject : str = "test_subject",
        message : str = "test_message",
        file_name : str = "boat.png"
    ):
        
        self.name.fill(name)
        self.email.fill(email)
        self.subject.fill(subject)
        self.message.fill(message)

        self.upload_file(file_name=file_name)

        self.page.once("dialog", lambda dialog: dialog.accept())
        self.submit_button.click()

        self.page.wait_for_load_state()

    def verify_details_submitted_successfully_and_return_to_homepage(self):
        from pages.homepage import HomePage

        expect(self.your_details_have_submitted_successfully).to_be_visible()

        self.home_button.click()
        Helper.close_ads(self.page)
        self.page.wait_for_load_state('domcontentloaded')

        return HomePage(self.page)

    
