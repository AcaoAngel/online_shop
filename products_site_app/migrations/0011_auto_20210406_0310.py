# Generated by Django 3.1.7 on 2021-04-06 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_site_app', '0010_auto_20210405_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart_products',
            name='picture',
            field=models.ImageField(blank=True, default='default_img.png', null=True, upload_to='static/media/'),
        ),
    ]
