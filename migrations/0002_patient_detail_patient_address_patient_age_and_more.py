# Generated by Django 5.0.3 on 2024-03-14 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='Detail',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('male', 'MALE'), ('female', 'Female'), ('other', 'Other')], default='male'),
        ),
        migrations.AddField(
            model_name='patient',
            name='medicine_detail',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='mobile',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='next_visit',
            field=models.TextField(default=0),
        ),
        migrations.AddField(
            model_name='patient',
            name='note',
            field=models.TextField(null=True),
        ),
    ]
