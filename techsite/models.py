# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class NewsArticle(models.Model):
    title = models.CharField(_("Заголовок"), max_length=200)
    content = models.TextField(_("Контент"))
    description = models.TextField(_("Описание"))
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = _("Статья")
        verbose_name_plural = _("Статьи")

