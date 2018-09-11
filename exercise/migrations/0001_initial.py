# Generated by Django 2.0.5 on 2018-09-13 13:48

from django.db import migrations, models
import django.db.models.deletion
import picklefield.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('introduction', models.TextField(blank=True, null=True)),
                ('afterword', models.TextField(blank=True, null=True)),
                ('length_minutes', models.IntegerField()),
                ('email_reveal_times', picklefield.fields.PickledObjectField(editable=False, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseAttachment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('filename', models.CharField(blank=True, max_length=250, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseEmail',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('subject', models.CharField(blank=True, max_length=250, null=True)),
                ('from_address', models.CharField(blank=True, max_length=250, null=True)),
                ('from_name', models.CharField(blank=True, max_length=250, null=True)),
                ('to_address', models.CharField(blank=True, max_length=250, null=True)),
                ('to_name', models.CharField(blank=True, max_length=250, null=True)),
                ('phish_type', models.IntegerField(choices=[(0, 'phishing'), (1, 'regular'), (1, 'etray')])),
                ('content', models.TextField(blank=True, null=True)),
                ('attachments', models.ManyToManyField(blank=True, to='exercise.ExerciseAttachment')),
                ('belongs_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='exercise.ExerciseEmail')),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseEmailReply',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('reply_type', models.IntegerField(choices=[(0, 'reply'), (1, 'forward')], null=True)),
                ('message', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseKey',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.IntegerField(choices=[(0, 'number'), (1, 'text')])),
                ('key', models.CharField(blank=True, max_length=180, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('exercise', models.ManyToManyField(to='exercise.Exercise')),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseURL',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('subject', models.CharField(blank=True, max_length=250, null=True)),
                ('actual_url', models.CharField(blank=True, max_length=250, null=True)),
                ('real_url', models.CharField(blank=True, max_length=250, null=True)),
                ('type', models.IntegerField(choices=[(0, 'phishing'), (1, 'regular'), (1, 'etray')])),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseWebPages',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('subject', models.CharField(blank=True, max_length=250, null=True)),
                ('url', models.CharField(blank=True, max_length=250, null=True)),
                ('type', models.IntegerField(choices=[(0, 'phishing'), (1, 'regular'), (1, 'etray')])),
                ('content', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='exerciseurl',
            name='web_page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercise.ExerciseWebPages'),
        ),
        migrations.AddField(
            model_name='exerciseemail',
            name='replies',
            field=models.ManyToManyField(blank=True, to='exercise.ExerciseEmailReply'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='emails',
            field=models.ManyToManyField(blank=True, to='exercise.ExerciseEmail'),
        ),
    ]
