# Generated by Django 5.0.6 on 2024-05-10 15:50

import django.contrib.postgres.indexes
import django.contrib.postgres.search
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='search_vector',
            field=django.contrib.postgres.search.SearchVectorField(null=True),
        ),
        migrations.AddIndex(
            model_name='shop',
            index=django.contrib.postgres.indexes.GinIndex(fields=['search_vector'],
                                                           name='core_shop_search__c1112d_gin'),
        ),
    ]
