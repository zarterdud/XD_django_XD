from django.test import TestCase, Client


class HomepageTests(TestCase):
    def set_up(self):
        pass

    def test_somename(self):
        pass


class Static(TestCase):
    def test_homepage_endpoint(self):
        response = Client().get('/')
        self.assertEqual(response.status_code, 200)
