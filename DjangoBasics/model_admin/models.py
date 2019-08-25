from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from .managers import ContentManager

SOURCE_TYPE = (
    ('edx', 'Edx'),
    ('connect', 'Connect'),
)


class MXCatalog(models.Model):
    """
    Base Class for this app's models.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Source(MXCatalog):
    """
    what does model represent?
    """
    name = models.CharField(verbose_name=_("Source name"), max_length=255)
    type = models.CharField(verbose_name=_(
        "Source Type"), choices=SOURCE_TYPE, max_length=255)
    title = models.CharField(verbose_name=_("Source Title"), max_length=255)
    order = models.PositiveIntegerField(
        verbose_name=_("Source order"), default=0)

    created_by = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name=_("source_created_by"))
    modified_by = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name=_("source_modified_by"))

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _("Content Source")
        verbose_name_plural = _("Content Sources")
        unique_together = (("name", "title"), )


# TODO : put in utils
# {media_root}/{instance.id}/example.png
def upload_location(instance, filename):
    return "{}/{}".format(instance.pk, filename)


class Tag(MXCatalog):
    """
    asdadadafd
    """
    name = models.CharField(verbose_name=_("Tag name"), max_length=255)
    is_active = models.BooleanField(
        verbose_name=_("Tag is applicable?"), default=True)


class Content(MXCatalog):
    """
    what does model represent?
    """
    source = models.ForeignKey(to=Source, on_delete=models.CASCADE)
    tags = models.ManyToManyField(to=Tag, null=True, blank=True)

    name = models.CharField(verbose_name=_("Content name"), max_length=255)
    slug = models.SlugField(verbose_name=_("Content Slug"), unique=True)
    icon = models.ImageField(verbose_name=_(
        "Content icon"), max_length=255, blank=True, null=True)
    doc = models.FileField(verbose_name=_("Doc File"),
                           upload_to=upload_location, null=True, blank=True)

    created_by = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name=_("content_created_by"))
    modified_by = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name=_("content_modified_by"))

    objects = ContentManager()

    class Meta:
        verbose_name_plural = _("Content")
        verbose_name = _("Content")
        ordering = ["created_at"]

    @property
    def get_tag_count(self):
        return self.tags.all().count()

    @property()
    def get_name_with_slug(self):
        return "{},{}".format(name, slug)
