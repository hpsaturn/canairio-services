# Generated by Django 3.0.9 on 2020-09-02 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canairio_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='canairiouser',
            name='app_version',
            field=models.CharField(max_length=12),
        ),
    ]