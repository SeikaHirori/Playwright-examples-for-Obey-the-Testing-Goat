import pytest
from pytest_django import asserts

from django.urls import resolve

from lists.views import home_page

class Tests_HomePage:

    def test_root_url_resolves_to_home_page_views(self):
        found = resolve('/')

        assert found.func == home_page