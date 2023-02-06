# Generated by Django 4.1.5 on 2023-01-25 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easycommerce', '0003_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('commentaire', models.TextField()),
                ('status', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
