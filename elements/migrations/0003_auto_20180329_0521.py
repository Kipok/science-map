# Generated by Django 2.0.3 on 2018-03-29 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elements', '0002_dataset_metric_result'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='dataset',
        ),
        migrations.DeleteModel(
            name='Dataset',
        ),
    ]