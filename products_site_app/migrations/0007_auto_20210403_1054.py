# Generated by Django 3.1.7 on 2021-04-03 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_site_app', '0006_auto_20210402_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart_products',
            name='picture',
            field=models.ImageField(blank=True, default='default_img.png', null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='cart_products',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='products',
            name='picture',
            field=models.ImageField(blank=True, default='default_img.png', null=True, upload_to='media/'),
        ),
    ]
