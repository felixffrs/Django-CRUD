from faker import Faker
from author_crud.models.author import Author

faker = Faker()

class AuthorFactory:

    def build_author_JSON(self):
        return {
            "id": faker.random_number(),
            "name": faker.name(),
            "birth_date": faker.date_of_birth(),
            "biography": faker.text()
        }
    
    def create_author(self):
        return Author.objects.create(**self.build_author_JSON())
