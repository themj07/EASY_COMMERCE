# Generated by Django 4.1.6 on 2023-02-08 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('easycommerce', '0025_alter_reply_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
