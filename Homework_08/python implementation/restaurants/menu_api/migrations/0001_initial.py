# Generated by Django 4.2.6 on 2023-10-19 03:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('restaurant_name', models.CharField(max_length=225)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('website', models.TextField(null=True)),
                ('food_type', models.CharField(max_length=255)),
                ('food_name', models.CharField(max_length=255)),
                ('quantity', models.PositiveBigIntegerField(default=1)),
                ('amount', models.FloatField(default=0.0)),
                ('categorey', models.CharField(max_length=100, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]