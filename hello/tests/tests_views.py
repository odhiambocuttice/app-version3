from django.test import TestCase, Client
from hello.models import Project
from django.urls import reverse
from .views import project_create_views, project_views
import pytest


class TestViews(TestCase):
    def test_create_list_GET(self):
        client = Client()
        response = client.get(reverse("create"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "project/project_create.html")
    def test_create_list(self):
        client = Client()
        response = client.get(reverse("object"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "project/project.html")
   










































