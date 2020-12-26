from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User


class Page(models.Model):
    """ Represents a single wiki page. """
    title = models.CharField(max_length=settings.WIKI_PAGE_TITLE_MAX_LENGTH, unique=True,
                             help_text="Title of your page.")
    author = models.ForeignKey(User, on_delete=models.PROTECT,
                               help_text="The user that posted this article.")
    slug = models.CharField(max_length=settings.WIKI_PAGE_TITLE_MAX_LENGTH, blank=True, editable=False,
                            help_text="Unique URL path to access this page. Generated by the system.")
    content = models.TextField(
        help_text="Write the content of your page here.")
        
    created = models.DateTimeField(auto_now_add=True,
                                   help_text="The date and time this page was created. Automatically generated when the model saves.")
    modified = models.DateTimeField(auto_now=True,
                                    help_text="The date and time this page was updated. Automatically generated when the model updates.")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """ Returns a fully-qualified path for a page (/my-new-wiki-page). """
        path_components = {'slug': self.slug}
        return reverse('wiki-details-page', kwargs=path_components)

    def save(self, *args, **kwargs):
        """ Creates a URL safe slug automatically when a new a page is created. """
        if not self.pk:
            self.slug = slugify(self.title, allow_unicode=True)

        # Call save on the superclass.
        return super(Page, self).save(*args, **kwargs)
