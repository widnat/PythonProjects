# Generated by Django 4.1.4 on 2022-12-25 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangoApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=350)),
                ('complete', models.BooleanField(default=False)),
            ],
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='title',
            new_name='name',
        ),
        migrations.AddField(
            model_name='todo',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='djangoApp.category'),
        ),
    ]
