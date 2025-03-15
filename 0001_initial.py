# Generated by Django 5.1.7 on 2025-03-15 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Email', models.EmailField(max_length=200)),
                ('PhoneNumber', models.IntegerField(null=True)),
                ('Course', models.CharField(max_length=20)),
            ],
        ),
    ]
