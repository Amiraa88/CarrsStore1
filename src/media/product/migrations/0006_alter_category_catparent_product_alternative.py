# Generated by Django 4.0.2 on 2022-02-16 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_category_catparent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='CATParent',
            field=models.ForeignKey(blank=True, limit_choices_to={'CATParent__isnull': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category'),
        ),
        migrations.CreateModel(
            name='Product_Alternative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PALNAlternatives', models.ManyToManyField(related_name='alternatives_product', to='product.Product')),
                ('PALNProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_product', to='product.product')),
            ],
        ),
    ]
