from django.test import TestCase
from django.shortcuts import reverse

# Create your tests here.
class LandingPageTest(TestCase):
    def test_status_code(self):
        #TODO some sort of test
        response = self.client.get(reverse("landing-page"))
        print(response.content)
        print("\n")
        print(response.cookies)
        print("\n")
        print(response.client)
        print("\n")
        print(response.context)
        print("\n")
        print(response.status_code)
        print("\n")
        print(response.request)
        print("\n")
        print(response.wsgi_request)

    def test_template_name(self):
        #TODO some sort of test
        pass
