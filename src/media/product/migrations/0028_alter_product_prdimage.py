# Generated by Django 4.0.2 on 2022-04-06 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0027_contactus_alter_review_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='PRDImage',
            field=models.ImageField(blank=True, null=True, upload_to='productimage/', verbose_name='Prduct Image'),
        ),
    ]
