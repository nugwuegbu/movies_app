# Generated by Django 4.2.1 on 2023-06-02 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_movies_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]
