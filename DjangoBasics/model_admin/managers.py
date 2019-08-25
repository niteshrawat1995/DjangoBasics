from django.db import models


class ContentManager(models.Manager):
    """
    Manager for content models
    """

    def staff_content(self):
        return self.filter(created_by__is_staff=True)

    def domestic_content(self):
        return self.filter(slug__icontains="edx")
