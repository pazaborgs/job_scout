# Generated by Django 4.1.7 on 2025-01-31 00:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0009_alter_company_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='specializations',
        ),
        migrations.RemoveField(
            model_name='company',
            name='technologies',
        ),
        migrations.DeleteModel(
            name='Specializations',
        ),
        migrations.DeleteModel(
            name='Technologies',
        ),
    ]
