from django.db import models
from wagtail.core.models import Page

# Create your models here.


class FlexPage(Page):

    class Meta:
        verbose_name = "Flex (misc) Page"
        verbose_name_plural = "Flex (misc) pages"