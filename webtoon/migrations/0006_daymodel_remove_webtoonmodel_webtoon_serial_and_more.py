# Generated by Django 4.2 on 2023-04-23 04:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webtoon', '0005_serialmodel_remove_webtoonmodel_webtoon_day_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DayModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_name', models.CharField(max_length=3, verbose_name='연재일')),
                ('day_create_time', models.DateTimeField(auto_now_add=True, verbose_name='생성일')),
            ],
            options={
                'verbose_name': '연재일',
                'verbose_name_plural': '연재일 리스트',
            },
        ),
        migrations.RemoveField(
            model_name='webtoonmodel',
            name='webtoon_serial',
        ),
        migrations.DeleteModel(
            name='SerialModel',
        ),
        migrations.AddField(
            model_name='webtoonmodel',
            name='webtoon_day',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='webtoon.daymodel', verbose_name='연재일'),
        ),
    ]