from django.test import TestCase
from django.urls import reverse

from .models import Category, Product


class SearchSuggestionTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(name="Electronics", icon="tech")
        cls.products = [
            Product.objects.create(
                category=cls.category,
                name=f"Apple Product {number:02d}",
                price="9.99",
                description="Test product",
                quantity=1,
            )
            for number in range(12)
        ]
        Product.objects.create(
            category=cls.category,
            name="Banana Product",
            price="4.99",
            description="Test product",
            quantity=1,
        )
        for name in (
            "Nike Shoes Black",
            "Shoes Brand",
            "Black Snickers Hoodie",
            "Snickers Bar",
            "Black Running Shoes",
        ):
            Product.objects.create(
                category=cls.category,
                name=name,
                price="19.99",
                description="Test product",
                quantity=1,
            )

    def get_suggestions(self, query):
        return self.client.get(reverse("search_suggestions"), {"q": query})

    def test_single_letter_returns_all_case_insensitive_prefix_matches(self):
        response = self.get_suggestions("a")

        self.assertEqual(response.status_code, 200)
        suggestions = response.json()
        self.assertEqual(len(suggestions), 12)
        self.assertTrue(all(item["name"].startswith("Apple") for item in suggestions))

    def test_additional_query_text_narrows_prefix_matches(self):
        response = self.get_suggestions("apple product 1")

        self.assertEqual(
            [item["name"] for item in response.json()],
            ["Apple Product 10", "Apple Product 11"],
        )

    def test_blank_query_returns_no_suggestions(self):
        response = self.get_suggestions("  ")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    def test_single_letter_only_suggests_names_starting_with_that_letter(self):
        response = self.get_suggestions("s")

        self.assertEqual(
            [item["name"] for item in response.json()],
            ["Shoes Brand", "Snickers Bar"],
        )

    def test_prefix_typing_keeps_matches_narrowed_to_the_prefix(self):
        response = self.get_suggestions("sh")

        self.assertEqual(
            [item["name"] for item in response.json()],
            ["Shoes Brand"],
        )

    def test_multiword_query_requires_every_word_when_matches_exist(self):
        response = self.get_suggestions("Black snickers")

        self.assertEqual(
            [item["name"] for item in response.json()],
            ["Black Snickers Hoodie"],
        )

    def test_multiword_query_falls_back_to_related_catalog_items(self):
        response = self.client.get(reverse("search_results"), {"q": "black widgets"})

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context["has_related_results"])
        self.assertEqual(
            [product.name for product in response.context["results"]],
            ["Black Running Shoes", "Black Snickers Hoodie"],
        )
