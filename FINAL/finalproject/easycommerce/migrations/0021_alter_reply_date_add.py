# Generated by Django 4.1.6 on 2023-02-07 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easycommerce', '0020_reply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='date_add',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]