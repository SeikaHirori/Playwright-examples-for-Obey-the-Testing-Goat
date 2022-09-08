import pytest
from pytest_django import asserts as pydj

from django.urls import resolve
from django.http import HttpRequest, HttpResponse

from lists.views import home_page

class Tests_HomePage:

    def test_root_url_resolves_to_home_page_views(self):
        found = resolve('/')

        assert found.func == home_page

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response:HttpResponse = home_page(request)
        html = response.content.decode('utf8')
        
        assert html.startswith('<html>') == True

        assert "<title>To-Do lists</title>" in html

        assert html.strip().endswith('</html>') == True
    
    