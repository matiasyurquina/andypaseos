# Generated by Django 5.0.3 on 2024-04-17 10:36

import django.contrib.auth.models
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('idLocality', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('locality', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('idPerson', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(db_column='phone', max_length=15, unique=True)),
                ('is_staff', models.BooleanField(db_column='isClient', default=False)),
                ('isAdmin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(db_column='active', default=False)),
                ('email', models.CharField()),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('idLocality', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='person.locality')),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('idInterview', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('quotas', models.PositiveSmallIntegerField(default=0)),
                ('idPerson', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
