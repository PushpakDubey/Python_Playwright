# tests/example_page.py

# pages/example_page.py
class ExamplePage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("https://playwright.dev/docs/auth")

    def get_title(self):
        return self.page.title()

    def click_button(self):
        self.page.click("button")

    def get_message(self):
        return self.page.inner_text(".message")

