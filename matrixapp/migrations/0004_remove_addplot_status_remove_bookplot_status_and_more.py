# Generated by Django 4.0.2 on 2022-07-27 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matrixapp', '0003_alter_installment_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addplot',
            name='status',
        ),
        migrations.RemoveField(
            model_name='bookplot',
            name='status',
        ),
        migrations.RemoveField(
            model_name='installment',
            name='status',
        ),
    ]