from django.utils.crypto import get_random_string
from django.utils.text import slugify


def unique_slug_generator(instance, slug):
    model = instance.__class__
    unique_slug = slugify(slug)

    while model.objects.filter(slug=unique_slug).exists():
        unique_slug = "{slug}-{randstr}".format(
            slug=slug,
            randstr=get_random_string(length=4)
        )
    return unique_slug
