# Generated by Django 3.0.8 on 2020-07-05 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UsedBooks', '0005_auto_20200705_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usedproduct',
            name='image',
            field=models.ImageField(default='image_not_found.png', upload_to='products'),
        ),
    ]
