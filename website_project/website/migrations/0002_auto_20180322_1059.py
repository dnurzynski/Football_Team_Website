# Generated by Django 2.0.3 on 2018-03-22 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_home', models.PositiveSmallIntegerField()),
                ('score_away', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField()),
                ('name', models.CharField(max_length=32)),
                ('surname', models.CharField(max_length=32)),
                ('position', models.CharField(max_length=32)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appearances', models.PositiveSmallIntegerField(null=True)),
                ('goals', models.PositiveSmallIntegerField(null=True)),
                ('conceded', models.PositiveSmallIntegerField(null=True)),
                ('clean_sheets', models.PositiveSmallIntegerField(null=True)),
                ('assists', models.PositiveSmallIntegerField(null=True)),
                ('yellow_cards', models.PositiveSmallIntegerField(null=True)),
                ('red_cards', models.PositiveSmallIntegerField(null=True)),
                ('minutes', models.PositiveSmallIntegerField(null=True)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Player')),
            ],
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('start_year', models.PositiveSmallIntegerField()),
                ('end_year', models.PositiveSmallIntegerField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.FileField(upload_to='')),
                ('logo_icon', models.FileField(upload_to='')),
                ('name', models.CharField(max_length=64)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='TeamSeason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matches', models.PositiveSmallIntegerField()),
                ('wins', models.PositiveSmallIntegerField()),
                ('draws', models.PositiveSmallIntegerField()),
                ('losts', models.PositiveSmallIntegerField()),
                ('goals_for', models.PositiveSmallIntegerField()),
                ('goals_against', models.PositiveSmallIntegerField()),
                ('points', models.SmallIntegerField()),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Season')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Team')),
            ],
        ),
        migrations.AddField(
            model_name='round',
            name='season',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Season'),
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='round',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Round'),
        ),
        migrations.AddField(
            model_name='match',
            name='team_away',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_away', to='website.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='team_home',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_home', to='website.Team'),
        ),
    ]