# Generated by Django 4.2.5 on 2023-09-09 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='content',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.AddField(
            model_name='blog',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
        migrations.AddField(
            model_name='post',
            name='blog',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='appname.blog'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
    ]
