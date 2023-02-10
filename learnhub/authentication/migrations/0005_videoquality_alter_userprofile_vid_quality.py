# Generated by Django 4.1.6 on 2023-02-10 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_userprofile_vid_quality'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoQuality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quality', models.CharField(choices=[('240p', '240p'), ('360p', '360p'), ('480p', '480p'), ('720p', '720p'), ('1080p', '1080p')], default='240p', max_length=5)),
            ],
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='vid_quality',
            field=models.CharField(max_length=5),
        ),
    ]