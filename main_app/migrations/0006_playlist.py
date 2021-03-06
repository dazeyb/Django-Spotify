# Generated by Django 3.2.2 on 2021-05-12 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_remove_artist_extra_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('songs', models.ManyToManyField(to='main_app.Song')),
            ],
        ),
    ]
