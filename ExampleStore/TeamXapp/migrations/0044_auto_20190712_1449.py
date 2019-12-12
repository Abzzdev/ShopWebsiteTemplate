# Generated by Django 2.2.3 on 2019-07-12 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TeamXapp', '0043_auto_20190712_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allmembers',
            name='scrum_team_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TeamXapp.ScrumTeam', verbose_name='Scrum team: '),
        ),
        migrations.AlterField(
            model_name='allmembers',
            name='scrum_team_roles',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TeamXapp.ScrumTeamRole', verbose_name='Scrum Team Roles: '),
        ),
    ]
