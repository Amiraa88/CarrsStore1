# Generated by Django 3.1.5 on 2022-02-21 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_auto_20220221_0235'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='PRDISBestseller',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='PRDISNew',
            field=models.BooleanField(default=True),
        ),
    ]