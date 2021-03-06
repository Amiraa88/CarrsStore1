# Generated by Django 4.0.2 on 2022-02-17 00:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_product_accessories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='CATDesc',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='category',
            name='CATImg',
            field=models.ImageField(upload_to='category/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='category',
            name='CATName',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='category',
            name='CATParent',
            field=models.ForeignKey(blank=True, limit_choices_to={'CATParent__isnull': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category', verbose_name='Main Category'),
        ),
        migrations.AlterField(
            model_name='product_accessories',
            name='PACCAccessories',
            field=models.ManyToManyField(related_name='accessories_product', to='product.Product', verbose_name='Accessories'),
        ),
        migrations.AlterField(
            model_name='product_accessories',
            name='PACCProduct',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mainaccessories_product', to='product.product', verbose_name='Product'),
        ),
        migrations.AlterField(
            model_name='product_alternative',
            name='PALNAlternatives',
            field=models.ManyToManyField(related_name='alternatives_product', to='product.Product', verbose_name='Alternatives'),
        ),
        migrations.AlterField(
            model_name='product_alternative',
            name='PALNProduct',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_product', to='product.product', verbose_name='Product'),
        ),
    ]
