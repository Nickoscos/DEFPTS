# Generated by Django 4.1.7 on 2023-03-08 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_automatechaudiere_delete_choice_delete_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chaufferie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nbChaudiere', models.IntegerField(max_length=1)),
            ],
        ),
        migrations.DeleteModel(
            name='AutomateChaudiere',
        ),
    ]
