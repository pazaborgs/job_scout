# Generated by Django 4.1.7 on 2025-01-31 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0010_remove_company_specializations_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='marketing_niche',
            field=models.CharField(choices=[('Marketing', 'Marketing'), ('Tecnologia', 'Tecnologia'), ('Nutrição', 'Nutrição'), ('Design', 'Design')], max_length=20),
        ),
    ]
