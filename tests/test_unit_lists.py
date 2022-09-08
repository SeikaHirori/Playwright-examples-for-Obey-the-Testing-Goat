import pytest
from pytest_django.asserts import assertTemplateUsed
from pytest_django import asserts

from django.urls import resolve
from django.http import HttpRequest, HttpResponse

from django.template.loader import render_to_string

from django.test import Client

from lists.views import home_page

class Tests_HomePage:

    def test_home_page_returns_correct_html_v3(self): # Uses Django.test's Client()
        response:HttpResponse = Client().get('/')

        ### Directly importing pytest_django's asserts
        assertTemplateUsed(response, 'lists/home.html')

        ### Example of how to call pytest_django's asserts; This easily provides a list of available option
        asserts.assertTemplateUsed(response, 'lists/home.html')


        