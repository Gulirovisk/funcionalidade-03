# Generated by Django 5.1.2 on 2024-10-31 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_animal_foto_animal_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='foto',
            field=models.ImageField(blank=True, default='bois/default-boi.jpg', null=True, upload_to='bois/', verbose_name='Foto'),
        ),
    ]
