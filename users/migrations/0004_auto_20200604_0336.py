# Generated by Django 3.0.6 on 2020-06-04 01:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
        ('users', '0003_history_vid'),
    ]

    operations = [
        migrations.AddField(
            model_name='savedvideos',
            name='vid',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='videos.Video'),
        ),
        migrations.AlterField(
            model_name='history',
            name='uid',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='users.User'),
        ),
        migrations.AlterField(
            model_name='history',
            name='vid',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='videos.Video'),
        ),
        migrations.AlterField(
            model_name='recommended',
            name='tag',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='recommended',
            name='uid',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='users.User'),
        ),
        migrations.AlterField(
            model_name='savedvideos',
            name='uid',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='users.User'),
        ),
        migrations.AlterField(
            model_name='searchhistory',
            name='qry',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='searchhistory',
            name='uid',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='users.User'),
        ),
    ]