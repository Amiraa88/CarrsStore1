# Generated by Django 4.0.2 on 2022-04-07 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0004_alter_brand_id_alter_variant_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='BDRDesc',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
    ]
