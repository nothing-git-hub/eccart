# Generated by Django 3.2.5 on 2021-07-23 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_categ_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categ',
            options={'ordering': ('name',), 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]
