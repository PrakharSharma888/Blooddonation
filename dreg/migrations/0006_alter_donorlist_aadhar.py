# Generated by Django 3.2.4 on 2021-12-06 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dreg', '0005_donorlist_aadhar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donorlist',
            name='aadhar',
            field=models.ImageField(default='logo/searchlogo.jpg', upload_to=''),
        ),
    ]