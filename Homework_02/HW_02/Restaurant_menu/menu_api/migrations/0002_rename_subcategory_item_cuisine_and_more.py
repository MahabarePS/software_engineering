# Generated by Django 4.2.5 on 2023-09-09 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='subcategory',
            new_name='cuisine',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='name',
            new_name='cuisine_item',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='category',
            new_name='restaurant',
        ),
        migrations.AddField(
            model_name='item',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='amount',
            field=models.FloatField(),
        ),
    ]
