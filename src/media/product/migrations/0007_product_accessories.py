# Generated by Django 4.0.2 on 2022-02-17 00:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_alter_category_catparent_product_alternative'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_accessories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PACCAccessories', models.ManyToManyField(related_name='accessories_product', to='product.Product')),
                ('PACCProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mainaccessories_product', to='product.product')),
            ],
        ),
    ]
