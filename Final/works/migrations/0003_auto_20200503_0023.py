# Generated by Django 3.0.2 on 2020-05-02 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0002_order_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='orders', to='works.Tag'),
        ),
    ]
