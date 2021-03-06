# Generated by Django 4.0.2 on 2022-02-06 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PRDName', models.CharField(max_length=400)),
                ('Catrgory', models.CharField(max_length=200)),
                ('PRDDesc', models.TextField()),
                ('PRDPrice', models.DecimalField(decimal_places=4, max_digits=12)),
                ('PRDCost', models.DecimalField(decimal_places=4, max_digits=12)),
                ('PRDCreated', models.DateTimeField()),
            ],
        ),
    ]
