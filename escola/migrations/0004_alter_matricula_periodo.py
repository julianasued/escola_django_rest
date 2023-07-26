# Generated by Django 4.2.3 on 2023-07-26 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0003_rename_nivel_matricula_periodo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matricula',
            name='periodo',
            field=models.CharField(choices=[('M', 'Matutino'), ('V', 'Vespertino'), ('N', 'Noturno')], default='M', max_length=1),
        ),
    ]