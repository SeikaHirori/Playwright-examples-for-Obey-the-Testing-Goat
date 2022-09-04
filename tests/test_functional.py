import pytest

import re
from playwright.sync_api import Page, expect

class Tests_homepage:

    def test_title(self, page: Page):
        page.goto("http://localhost:8000")

        expect(page).to_have_title(re.compile("The install worked successfully! Congratulations!"))