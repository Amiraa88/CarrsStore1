# Generated by Django 4.0.2 on 2022-02-15 22:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_delete_productmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Catrgory',
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDCost',
            field=models.DecimalField(decimal_places=4, max_digits=12, verbose_name='Cost'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDCreated',
            field=models.DateTimeField(verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDPrice',
            field=models.DecimalField(decimal_places=4, max_digits=12, verbose_name='Price'),
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PRDIImage', models.ImageField(upload_to='product/', verbose_name='Image')),
                ('PRDIProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='Product Name')),
            ],
        ),
    ]
