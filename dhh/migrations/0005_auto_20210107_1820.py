# Generated by Django 3.1.5 on 2021-01-07 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dhh', '0004_auto_20210107_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='released_in',
            field=models.DateField(blank=True, null=True),
        ),
    ]
