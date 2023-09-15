
import random
from django.utils.text import slugify

'''
 this method will be used with image field on UserProfile model
   '''
def path_file_name(instance, filename):
    return '/'.join(filter(None, (str(random.randint(300_000,500_000)), filename)))

import random
from django.utils.text import slugify

def generate_slugify_for_instance(instance, field_values,save=False, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(''.join(field_values))
    Klass = instance.__class__
    qs = Klass.objects.filter(slug=slug).exclude(id=instance.id)
    if qs.exists():
        # auto generate new slug
        rand_int = random.randint(300_000, 500_000)
        slug = f"{slug}-{rand_int}"
        return generate_slugify_for_instance(instance, field_values,save=save, new_slug=slug)
    instance.slug = slug
    if save:
        instance.save()
    return instance

