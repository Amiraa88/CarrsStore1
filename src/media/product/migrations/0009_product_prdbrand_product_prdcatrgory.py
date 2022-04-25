# Generated by Django 4.0.2 on 2022-02-17 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_variant'),
        ('product', '0008_alter_category_catdesc_alter_category_catimg_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='PRDBrand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='settings.brand', verbose_name='Brand'),
        ),
        migrations.AddField(
            model_name='product',
            name='PRDCatrgory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category', verbose_name='Category'),
        ),
    ]