# Generated by Django 3.0.3 on 2020-08-05 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genedata', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gene',
            name='gene_id',
            field=models.CharField(db_index=True, max_length=256),
        ),
    ]
