# Generated by Django 5.0.3 on 2024-05-17 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hotels',
            options={'verbose_name': 'Hotels', 'verbose_name_plural': 'Hotels'},
        ),
        migrations.AlterModelOptions(
            name='schedule',
            options={'verbose_name': 'Schedule', 'verbose_name_plural': 'Schedule'},
        ),
        migrations.AlterModelOptions(
            name='speakers',
            options={'verbose_name': 'Speakers', 'verbose_name_plural': 'Speakers'},
        ),
        migrations.AlterModelOptions(
            name='tickets',
            options={'verbose_name': 'Tickets', 'verbose_name_plural': 'Tickets'},
        ),
    ]
