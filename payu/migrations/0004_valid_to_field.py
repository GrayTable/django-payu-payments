# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payu', '0003_auto_20160601_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='valid_to',
            field=models.DateTimeField(_('validity date'), editable=True),
        ),
    ]
