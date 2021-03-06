# Generated by Django 3.1.7 on 2021-04-02 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_site_app', '0005_cart_products_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart_products',
            name='description',
            field=models.TextField(default='no-description', max_length=500),
        ),
        migrations.AddField(
            model_name='cart_products',
            name='picture',
            field=models.ImageField(blank=True, default='default_img.png', null=True, upload_to='static/media/'),
        ),
        migrations.AddField(
            model_name='cart_products',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=11),
        ),
    ]
