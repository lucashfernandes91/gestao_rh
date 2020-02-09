# Generated by Django 2.2.6 on 2020-02-04 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0002_documento_pertence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='pertence',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='funcionarios.Funcionario'),
            preserve_default=False,
        ),
    ]
