# Generated by Django 4.0.2 on 2022-07-30 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matrixapp', '0009_alter_addplot_plot_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addplot',
            name='plot_rate',
        ),
    ]
