# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class TechsiteConfig(AppConfig):
    name = 'techsite'
    verbose_name = _("Сайт")

    def ready(self):
        from . import signals
