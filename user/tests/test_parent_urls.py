# from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from ..models import *


# Api testing for Parent user
class ParentAPITests(APITestCase):

    # Setting up parent user
    def setUp(self):
        self.parent = Parent.objects.create(
            first_name="Saif",
            last_name="Newaz",
            street="Bou Baazar",
            city="Dhaka",
            state="Dhaka",
            zip_code=1206
        )

    # Get List of Parent Users
    def test_get_parents_list(self):
        response = self.client.get(reverse('parent-user-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Create a Parent User
    def test_parent_user_create(self):
        data = {
            "first_name": "Saif",
            "last_name": "Newaz",
            "street": "Bou Baazar",
            "city": "Dhaka",
            "state": "Dhaka",
            "zip_code": 1206
        }

        response = self.client.post(reverse('parent-user-create'), data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Upadate a Parent User by id(pk)

    def test_parent_user_update(self):

        data = {
            "first_name": "Saif",
            "last_name": "Newaz",
            "street": "House no 177, North Vashantek",
            "city": "Dhaka",
            "state": "Dhaka",
            "zip_code": 1206
        }

        self.parent.refresh_from_db()
        response = self.client.put(
            reverse('parent-user-update', kwargs={'id': self.parent.id}), data)

        self.assertEqual(response.status_code,
                         status.HTTP_200_OK)

    # Delete a Parent User by id(pk)
    def test_parent_user_delete(self):

        self.parent.refresh_from_db()
        response = self.client.delete(
            reverse('parent-user-delete', kwargs={'id': self.parent.id}))
        self.assertEqual(response.status_code,
                         status.HTTP_204_NO_CONTENT)
