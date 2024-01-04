from django.urls import reverse, resolve
from django.test import Client
from bs4 import BeautifulSoup
import pytest


class TestVPCardOnlineUrls:

    def test_vpcardonline_index_url(self):
        url = reverse('index')
        assert resolve(url).view_name == 'index'
        assert resolve(url).url_name == 'index'

    def test_access_code_url(self):
        url = reverse('access_code')
        assert resolve(url).view_name == 'access_code'
        assert resolve(url).url_name == 'access_code'
