# from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from ..models import *


# Api Testing for Child user
class ChildAPITests(APITestCase):
    def setUp(self):
        # Setting up Parent User
        self.parent = Parent.objects.create(
            first_name="Saif",
            last_name="Newaz",
            street="Bou Baazar",
            city="Dhaka",
            state="Dhaka",
            zip_code=1206
        )

        # Setting up Child User
        self.child = Child.objects.create(
            parent=self.parent,
            first_name="Saisha",
            last_name="Newaz",
        )

    # Get List of Child Users

    def test_get_children_list(self):
        response = self.client.get(reverse('child-user-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Create a Child User

    def test_child_user_create(self):
        data = {
            "parent": self.parent.id,
            "first_name": "Saisha2",
            "last_name": "Newaz",
        }

        response = self.client.post(reverse('child-user-create'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Update a Child User by id(pk)
    def test_child_user_update(self):

        data = {
            "parent": self.parent.id,
            "first_name": "Updated",
            "last_name": "Newaz",
        }

        self.child.refresh_from_db()
        response = self.client.put(
            reverse('child-user-update', kwargs={'id': self.child.id}), data)
        self.assertEqual(response.status_code,
                         status.HTTP_200_OK)

    # Delete a Child User by id(pk)
    def test_child_user_delete(self):
        self.child.refresh_from_db()
        response = self.client.delete(
            reverse('child-user-delete', kwargs={'id': self.child.id}))
        self.assertEqual(response.status_code,
                         status.HTTP_204_NO_CONTENT)
