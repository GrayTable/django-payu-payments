# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payu', '0004_valid_to_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='pay_url',
            field=models.TextField('PayU URL', editable=True, null=True, blank=True),
        ),
    ]
