# Generated by Django 5.0 on 2024-01-02 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_rename_message_inbox'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='link',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
