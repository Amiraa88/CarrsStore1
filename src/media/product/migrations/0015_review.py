# Generated by Django 4.0.2 on 2022-03-06 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_alter_category_id_alter_product_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]