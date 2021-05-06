from django.test import Client, TestCase
from django.urls import reverse

from.models import Nationality, Player

# Create your tests here.
class BaseTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.test_nationality = Nationality.objects.create(name="Filipino")
        cls.test_player = Player.objects.create(name='Elwin Carlos', nationality='Filipino', favourited_by='No-one')

class TestBasicViews(BaseTestCase):
    client = Client()

    def test_home(self):
        response = self.client.get(reverse('favourites-home'))
        assert "home.html" in [t.name for t in response.templates]

    def test_players(self):
        response = self.client.get(reverse('favourites-players'))
        assert "players" in response.context
        assert response.context["players"].count() == 1
        assert "players.html" in [t.name for t in response.templates]

    def test_show(self):
        response = self.client.get(reverse('favourites-show', arg=[1]))
        assert "player" in response.context
        assert response.context["player"].name == 'Elwin Carlos'
        assert response.context["player"].nationality.name == 'Filipino'