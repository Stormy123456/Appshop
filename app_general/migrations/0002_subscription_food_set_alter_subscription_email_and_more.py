# Generated by Django 4.0.3 on 2022-04-15 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_foods', '0001_initial'),
        ('app_general', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='food_set',
            field=models.ManyToManyField(to='app_foods.food'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='status',
            field=models.CharField(choices=[('unapproved', 'Unapproved'), ('banned', 'Banned'), ('approved', 'Approved')], default='unapproved', max_length=15),
        ),
    ]
