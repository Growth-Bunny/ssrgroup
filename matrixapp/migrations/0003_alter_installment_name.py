# Generated by Django 4.0.2 on 2022-07-18 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrixapp', '0002_alter_installment_plot_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='installment',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
