# Generated by Django 4.1.3 on 2022-11-29 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redline', '0006_post_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
