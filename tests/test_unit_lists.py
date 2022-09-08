import pytest
from pytest_django.asserts import assertTemplateUsed

from django.urls import resolve
from django.http import HttpRequest, HttpResponse

from django.template.loader import render_to_string

from django.test import Client

from lists.views import home_page

class Tests_HomePage:

    def test_root_url_resolves_to_home_page_views(self):
        found = resolve('/')

        assert found.func == home_page

    def test_home_page_returns_correct_html_v1(self):
        request = HttpRequest()
        response:HttpResponse = home_page(request)
        html = response.content.decode('utf8')
        
        assert html.startswith('<html>') == True

        assert "<title>To-Do lists</title>" in html

        assert html.strip().endswith('</html>') == True
    
    def test_home_page_returns_correct_html_v2(self): # Uses render_to_string
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        expected_html = render_to_string('lists/home.html')

        assert html == expected_html

    def test_home_page_returns_correct_html_v3(self): # Uses Django.test's Client()
        response:HttpResponse = Client().get('/')

        html = response.content.decode('utf8')
        
        assert html.startswith('<html>') == True
        assert '<title>To-Do lists</title>' in html
        assert html.strip().endswith('</html>') == True

        assertTemplateUsed(response, 'lists/home.html')

        