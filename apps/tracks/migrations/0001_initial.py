# Generated by Django 4.0.4 on 2022-07-15 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tracks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=35)),
                ('image', models.ImageField(upload_to='albums/')),
                ('plays_count', models.PositiveBigIntegerField(default=0)),
                ('file', models.FileField(upload_to='music_files/')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album', to='albums.albums')),
            ],
            options={
                'verbose_name': 'Song',
                'verbose_name_plural': 'Songs',
            },
        ),
    ]