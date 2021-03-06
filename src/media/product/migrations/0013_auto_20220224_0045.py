# Generated by Django 3.1.5 on 2022-02-23 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_auto_20220221_0326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='PRDISBestseller',
            field=models.BooleanField(default=False, verbose_name='Best Seller'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDISNew',
            field=models.BooleanField(default=True, verbose_name='New Product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDSlug',
            field=models.SlugField(blank=True, null=True, verbose_name='Product URL'),
        ),
    ]
