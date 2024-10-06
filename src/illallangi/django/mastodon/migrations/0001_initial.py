# Generated by Django 5.1.1 on 2024-10-06 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.URLField(unique=True)),
                ('content', models.TextField()),
                ('datetime', models.DateTimeField()),
            ],
        ),
    ]
