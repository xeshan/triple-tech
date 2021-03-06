# Generated by Django 4.0.3 on 2022-03-08 08:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('currency', models.TextField(max_length=3)),
                ('return_percentage', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
    ]
