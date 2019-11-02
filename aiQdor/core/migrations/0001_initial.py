# Generated by Django 2.2.1 on 2019-06-17 22:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dentista',
            fields=[
                ('CRO', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=40)),
                ('especialidade', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Procedimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('descricao', models.CharField(max_length=40)),
                ('preco', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('hora', models.TimeField()),
                ('descricao', models.TextField(max_length=40)),
                ('statusPagamento', models.CharField(choices=[('PC', 'Confirmado'), ('NP', 'Não Pago'), ('DV', 'Devendo'), ('EA', 'Em andamento')], max_length=15)),
                ('statusConsulta', models.CharField(choices=[('RE', 'Realizada'), ('EA', 'Á ser realizada'), ('CA', 'Cancelada'), ('AD', 'Adiada')], max_length=15)),
                ('dentistaCRO', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Dentista')),
                ('pacienteCPF', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('procedimentos', models.ManyToManyField(to='core.Procedimento')),
            ],
        ),
    ]