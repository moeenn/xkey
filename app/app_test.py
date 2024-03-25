
from unittest import TestCase
from app import Application


class TestApp(TestCase):
    app = Application()

    def test_random_number(self) -> None:
        result = self.app.random_number()
        self.assertEqual(result, 42)
		
