# Generated by Django 3.1.7 on 2021-04-14 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['-added_on']},
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='added_date',
            new_name='added_on',
        ),
        migrations.AddField(
            model_name='todo',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]