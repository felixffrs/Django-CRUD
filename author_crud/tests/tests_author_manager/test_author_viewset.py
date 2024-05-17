from rest_framework import status
from ..factories.author_manager.author_factories import AuthorFactory
from ..test_setup import TestSetUp

class AuthorTestCase(TestSetUp):
    url = "/api/v1/authors"

    def test_get_author_by_id(self):
        author = AuthorFactory().create_author()
        response = self.client.get(
            path = f"{self.url}/{author.id}/",
            headers = self.headers,
            format = "json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_authors(self):
        authors = [AuthorFactory().create_author()]
        response = self.client.get(
            path = f"{self.url}/",
            headers = self.headers,
            format = "json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), len(authors))

    def test_create_author(self):
        author = AuthorFactory().build_author_JSON()
        response = self.client.post(
            path = f"{self.url}/",
            headers = self.headers,
            data = author,
            format = "json"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], author["name"])
        self.assertEqual(response.data["biography"], author["biography"])
