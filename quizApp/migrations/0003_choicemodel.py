# Generated by Django 4.2.1 on 2023-06-11 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizApp', '0002_rename_topicsmodel_topicmodel_questionmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChoiceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.TextField()),
                ('correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='quizApp.questionmodel')),
            ],
        ),
    ]