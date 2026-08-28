# add_product_images.py
#
# HOW TO USE:
# 1. Name each image file after the product's slug, e.g.:
#      sony-65-4k-oled-smart-tv.jpg
#      iphone-15-pro-max.png
#    Product.slug is auto-generated from the name via slugify() in your
#    model's save() method, so check the admin panel or shell to confirm
#    the exact slug for each product if you're unsure.
# 2. Put all the image files in one folder, e.g. ~/Desktop/AMAZON/product_images/
# 3. Update IMAGE_FOLDER below to that path.
# 4. Run: python add_product_images.py

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amazon.settings')
django.setup()

from django.core.files import File
from catalog.models import Product

IMAGE_FOLDER = r"C:\Users\Dell\Desktop\AMAZON\amazon\zgigantic"  # <-- change this
VALID_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.webp')


def add_images():
    if not os.path.isdir(IMAGE_FOLDER):
        print(f"Folder not found: {IMAGE_FOLDER}")
        return

    matched = 0
    unmatched_files = []
    products_without_images = []

    image_files = [
        f for f in os.listdir(IMAGE_FOLDER)
        if f.lower().endswith(VALID_EXTENSIONS)
    ]

    print(f"Found {len(image_files)} image files in {IMAGE_FOLDER}")
    print("=" * 50)

    for filename in image_files:
        slug = os.path.splitext(filename)[0]

        try:
            product = Product.objects.get(slug=slug)
        except Product.DoesNotExist:
            unmatched_files.append(filename)
            continue
        except Product.MultipleObjectsReturned:
            print(f"  [WARNING] Multiple products match slug '{slug}', skipping")
            continue

        filepath = os.path.join(IMAGE_FOLDER, filename)
        with open(filepath, 'rb') as f:
            product.image.save(filename, File(f), save=True)

        print(f"  assigned: {filename} -> {product.name}")
        matched += 1

    for product in Product.objects.filter(image=''):
        products_without_images.append(product.name)

    print("\n" + "=" * 50)
    print(f"Done. {matched} images assigned.")

    if unmatched_files:
        print(f"\n{len(unmatched_files)} image file(s) didn't match any product slug:")
        for f in unmatched_files:
            print(f"  - {f}")

    if products_without_images:
        print(f"\n{len(products_without_images)} product(s) still have no image:")
        for name in products_without_images:
            print(f"  - {name}")


if __name__ == '__main__':
    add_images()
