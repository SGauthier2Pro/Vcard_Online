import pytest

from users.models.customuser import CustomUser
import pytest


class TestModelCustomUser:

    @pytest.mark.django_db
    def test_create_user(self):

        # check if db is empty
        assert CustomUser.objects.count() == 0

        # create a new CustoUser
        user = CustomUser.objects.create(
            username='newuser',
            first_name='new',
            last_name='user',
            email="new.user@test.net",
            password='P@s$4TestAp1'
        )

        # check if number of customuser in db has been increased
        assert CustomUser.objects.count() == 1

        # check if user is well created
        assert str(user) == user.username

# Create your tests here.
