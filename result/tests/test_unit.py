from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_result(self):
        players = ["Rooney", "Beckham", "Cole"]
        teams = ["Arsenal", "Chelsea", "Fulham"]
        result = [b"Rooney will score", b"Rooney will score", b"Rooney will score", 
                    b"Beckham will score", b"Beckham will not score", b"Beckham will score", 
                    b"Cole will not score", b"Cole will not score", b"Cole will score"]
        i = 0
        for player in players:
            for team in teams:
                response=self.client.post(url_for("result"), json={"player" : player, "team" : team})
                self.assertEqual(response.data, result[i])
                i+=1
