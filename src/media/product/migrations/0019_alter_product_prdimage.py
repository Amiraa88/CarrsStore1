# Generated by Django 4.0.2 on 2022-03-18 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_alter_product_prdimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='PRDImage',
            field=models.ImageField(upload_to='productimage/', verbose_name='Prduct Image'),
        ),
    ]