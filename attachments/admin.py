from __future__ import unicode_literals

from django.contrib.contenttypes.admin import GenericStackedInline

from .models import Attachment
from .forms import AttachmentForm
from django.utils.translation import ugettext_lazy as _


class AttachmentInlines(GenericStackedInline):
    model = Attachment
    form = AttachmentForm
    exclude = ()
    extra = 1
    verbose_name = _("attachment")
    verbose_name_plural = _("attachment")
