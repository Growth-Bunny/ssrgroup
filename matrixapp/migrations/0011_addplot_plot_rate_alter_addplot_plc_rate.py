# Generated by Django 4.0.2 on 2022-07-30 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrixapp', '0010_remove_addplot_plot_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='addplot',
            name='plot_rate',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='addplot',
            name='plc_rate',
            field=models.IntegerField(default=0),
        ),
    ]
