# Generated by Django 4.0.6 on 2022-07-07 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='object',
            name='name',
            field=models.CharField(default='Test', max_length=25),
            preserve_default=False,
        ),
    ]