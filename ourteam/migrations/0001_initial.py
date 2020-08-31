# Generated by Django 3.1 on 2020-08-29 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OurTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=55)),
                ('team_designation', models.CharField(max_length=55)),
                ('team_description', models.TextField()),
                ('team_image', models.ImageField(upload_to='team_img/')),
                ('team_facebook', models.URLField()),
                ('team_twitter', models.URLField()),
                ('team_linkedIn', models.URLField()),
                ('team_instagram', models.URLField()),
                ('team_youtube', models.URLField()),
                ('team_created_date', models.DateTimeField(auto_now_add=True)),
                ('team_updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
