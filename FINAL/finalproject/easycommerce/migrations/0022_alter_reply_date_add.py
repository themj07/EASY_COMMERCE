# Generated by Django 4.1.6 on 2023-02-07 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easycommerce', '0021_alter_reply_date_add'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='date_add',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
