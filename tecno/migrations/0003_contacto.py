# Generated by Django 5.0.6 on 2024-06-04 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tecno', '0002_producto_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('tipo_consulta', models.IntegerField(choices=[(0, 'consulta'), (1, 'reclamo'), (2, 'sugerencia'), (3, 'felicitaciones')])),
                ('mensage', models.TextField()),
                ('avisos', models.BooleanField()),
            ],
        ),
    ]
