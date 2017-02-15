# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 13:29
from __future__ import unicode_literals

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.ASCIIUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Association',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opened', models.DateField()),
                ('closed', models.DateField(blank=True, null=True)),
                ('association', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caseworkclub.Association')),
            ],
        ),
        migrations.CreateModel(
            name='CaseNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('text', models.TextField()),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caseworkclub.Case')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='CaseworkType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typename', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('facility_time', models.BooleanField(verbose_name=b'Pays into facility time pot')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='JobType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typename', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='NoteType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=20)),
                ('first_names', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', models.CharField(blank=True, max_length=11, validators=[django.core.validators.RegexValidator(message=b'Phonenumber must be 11 digits long and start with 0', regex=b'0[0-9]{10}')])),
                ('mobile', models.CharField(blank=True, max_length=11, validators=[django.core.validators.RegexValidator(message=b'Phonenumber must be 11 digits long and start with 0', regex=b'0[0-9]{10}')])),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('settime', models.DateTimeField(default=django.utils.timezone.now)),
                ('completedtime', models.DateTimeField(blank=True, null=True)),
                ('text', models.TextField()),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caseworkclub.Case')),
            ],
        ),
        migrations.CreateModel(
            name='Workplace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caseworkclub.Employer')),
            ],
        ),
        migrations.CreateModel(
            name='Caseworker',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='caseworkclub.Person')),
                ('association', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caseworkclub.Association')),
            ],
            bases=('caseworkclub.person',),
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='caseworkclub.Person')),
                ('membership_number', models.CharField(max_length=6, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(message=b'NUT Membership Numbers have a capital letter and five digits.', regex=b'[A-Z]\\d{5}')])),
            ],
            bases=('caseworkclub.person',),
        ),
        migrations.AddField(
            model_name='task',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caseworkclub.Person'),
        ),
        migrations.AddField(
            model_name='task',
            name='tasktype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caseworkclub.NoteType'),
        ),
        migrations.AddField(
            model_name='person',
            name='workplace',
            field=models.ManyToManyField(through='caseworkclub.Job', to='caseworkclub.Workplace'),
        ),
        migrations.AddField(
            model_name='job',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caseworkclub.Person'),
        ),
        migrations.AddField(
            model_name='job',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caseworkclub.JobType'),
        ),
        migrations.AddField(
            model_name='job',
            name='workplace',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caseworkclub.Workplace'),
        ),
        migrations.AddField(
            model_name='casenote',
            name='contact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='caseworkclub.Person'),
        ),
        migrations.AddField(
            model_name='casenote',
            name='notetype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caseworkclub.NoteType'),
        ),
        migrations.AddField(
            model_name='case',
            name='caseworktypes',
            field=models.ManyToManyField(to='caseworkclub.CaseworkType'),
        ),
        migrations.AddField(
            model_name='case',
            name='workplace',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caseworkclub.Workplace'),
        ),
        migrations.AddField(
            model_name='user',
            name='association',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caseworkclub.Association'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='case',
            name='caseworker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caseworkclub.Caseworker'),
        ),
        migrations.AddField(
            model_name='case',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caseworkclub.Member'),
        ),
    ]
