# Generated by Django 4.0.2 on 2022-04-10 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0030_alter_category_catdesc_alter_category_catimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('STYName', models.CharField(max_length=50, verbose_name='Name')),
                ('STYImg', models.ImageField(blank=True, null=True, upload_to='category/', verbose_name='Image')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='PRDStyle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.style', verbose_name='Style'),
        ),
    ]
