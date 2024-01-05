from django.urls import reverse
from django.test import Client
from bs4 import BeautifulSoup
import pytest


class TestIndexView:

    client = Client()
    index_url = reverse('index')

    @pytest.mark.django_db
    def test_access_index_with_unauthenticated_user_and_no_access_code(self, get_datas):

        response = self.client.get(self.index_url)

        assert response.status_code == 200
        assert '<title>VP Card Online</title>' in str(response.content)
        assert 'enter ID</a>' in str(response.content)
        assert 'login</a>' in str(response.content)
        assert 'signup</a>' in str(response.content)
        assert '<div class="display col-12">' in str(response.content)
        assert 'Bienvenu sur VP Card Online !<br>' in str(response.content)

        soup = BeautifulSoup(response.content, 'html.parser')

        access_code_link = False
        login_link = False
        signup_link = False

        for li in soup.find_all('li'):
            assert li.find('a', href=True)
            if li.a['href'] == reverse('access_code'):
                access_code_link = True
            elif li.a['href'] == reverse('users:login'):
                login_link = True
            elif li.a['href'] == reverse('users:signup'):
                signup_link = True

        assert access_code_link
        assert login_link
        assert signup_link

    @pytest.mark.django_db
    def test_access_index_with_authenticated_user(self, get_datas):
        user = get_datas['user1']
        self.client.force_login(user)
        response = self.client.get(self.index_url)

        assert response.status_code == 200
        assert f'<title>{user.first_name} {user.last_name}\\\'s Portfolio</title>'\
               in str(response.content)
        assert '<a class="nav-link" href="/portfolio/">Portfolio</a>' in str(response.content)
        assert '<a class="nav-link" href="/project/">Project</a>' in str(response.content)
        assert '<a class="nav-link" href="/skill/">Skills</a>' in str(response.content)
        assert '<a class="nav-link" href="/cv/">Cv</a>' in str(response.content)
        assert '<a class="nav-link" href="/users/profile/">Profile</a>' in str(response.content)
        assert '<a class="nav-link" href="/users/logout/">'\
               in str(response.content)
        assert f'Bienvenu {user.first_name} !' in str(response.content)
