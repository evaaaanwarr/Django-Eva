# Generated by Django 5.0.4 on 2024-05-01 01:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, default='testing.jpeg', upload_to='thumbnail', verbose_name='Picture')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
            },
        ),
    ]
