from django.test import TestCase

#from django.urls import reverse


class UserRegistrationTest(TestCase):

    def test_registration_url_uses_correct_template(self):
        resp = self.client.get('/signup/')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'authorization/register.html')

    def test_login_url_uses_correct_template(self):
        resp = self.client.get('/login/')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'authorization/login.html')
