import pytest
from pytest_django.asserts import assertTemplateUsed
from pytest_django import asserts

from django.urls import resolve
from django.http import HttpRequest, HttpResponse

from django.template.loader import render_to_string

from django.test import Client

from lists.views import home_page
from lists.models import Item

from django.db.models import QuerySet

@pytest.mark.django_db # RFER 10
class Tests_ItemModel:

    def test_saving_and_retrieving_items(self):
        first_item:Item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item:Item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items:QuerySet = Item.objects.all()
        assert saved_items.count() == 2

        first_saved_item:Item = saved_items[0]
        second_saved_item:Item = saved_items[1]
        assert first_saved_item.text == 'The first (ever) list item'
        assert second_saved_item.text == 'Item the second'

class Tests_HomePage:

    def test_uses_home_template(self): # Uses Django.test's Client()
        response:HttpResponse = Client().get('/')

        ### Directly importing pytest_django's asserts
        assertTemplateUsed(response, 'lists/home.html')

        ### Example of how to call pytest_django's asserts; This easily provides a list of available option
        asserts.assertTemplateUsed(response, 'lists/home.html')

    def test_can_save_a_POST_request(self):
        response:HttpResponse = Client().post('/', data={'item_text':'A new list item'})

        desired_text = 'A new list item'
        assert desired_text in response.content.decode(), "Item not in list."
        asserts.assertTemplateUsed(response, 'lists/home.html')