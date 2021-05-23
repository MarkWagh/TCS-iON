# Generated by Django 3.0.5 on 2021-05-20 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventmanagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=64)),
                ('last_name', models.CharField(default='', max_length=64)),
                ('phone', models.BigIntegerField()),
                ('username', models.EmailField(default='', max_length=64)),
                ('password1', models.CharField(default='', max_length=20)),
                ('password2', models.CharField(default='', max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=64)),
                ('category', models.CharField(default='', max_length=64)),
                ('maxpeople', models.CharField(default='', max_length=64)),
                ('date', models.DateField(default='')),
                ('time', models.TimeField(default='')),
                ('location1', models.CharField(default='', max_length=64)),
                ('location2', models.CharField(default='', max_length=64)),
                ('city', models.CharField(default='', max_length=64)),
                ('state', models.CharField(default='', max_length=64)),
                ('pincode', models.IntegerField(default='')),
                ('description', models.CharField(default='', max_length=1000)),
                ('eventmanager', models.CharField(default='', max_length=64)),
                ('cost', models.IntegerField(default='')),
                ('count', models.CharField(default='', max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Eventmanager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=64)),
                ('last_name', models.CharField(default='', max_length=64)),
                ('phone', models.BigIntegerField()),
                ('username', models.EmailField(default='', max_length=64)),
                ('password1', models.CharField(default='', max_length=64)),
                ('password2', models.CharField(default='', max_length=64)),
                ('events', models.ManyToManyField(blank=True, related_name='myevents', to='eventmanagement.Event')),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='customer',
            name='events',
            field=models.ManyToManyField(blank=True, related_name='participants', to='eventmanagement.Event'),
        ),
    ]
