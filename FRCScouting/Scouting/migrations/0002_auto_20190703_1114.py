# Generated by Django 2.2.2 on 2019-07-03 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Scouting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stronghold_match',
            name='alliance_colour',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='stronghold_match',
            name='author',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='stronghold_match',
            name='blue_score',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='stronghold_match',
            name='challenge',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='stronghold_match',
            name='comments',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='stronghold_match',
            name='cross_Chevel_de_frise',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='stronghold_match',
            name='cross_Drawbridge',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='stronghold_match',
            name='cross_Lowbar',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='stronghold_match',
            name='cross_Moat',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='stronghold_match',
            name='cross_Portcullis',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='stronghold_match',
            name='cross_Ramparts',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='stronghold_match',
            name='cross_Rock_wall',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='stronghold_match',
            name='cross_Rough_terrain',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='stronghold_match',
            name='driver_rating',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='stronghold_match',
            name='match_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='stronghold_match',
            name='red_score',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='stronghold_match',
            name='robot_dead',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='stronghold_match',
            name='scale',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='stronghold_match',
            name='team_name',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='stronghold_match',
            name='team_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='stronghold_match',
            name='time_created',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]