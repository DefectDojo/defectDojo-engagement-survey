# Generated by Django 2.2.1 on 2019-07-17 21:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import sys


class Migration(migrations.Migration):

    sys.stderr.write("\n\ndefectDojo_engagement_survery 0001_initial")
    initial = True
    sys.stderr.write("\nChecking Dependencies")
    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('dojo', '__latest__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('order', models.PositiveIntegerField(default=1, help_text='The render order')),
                ('optional', models.BooleanField(default=False, help_text="If selected, user doesn't have to answer this question")),
                ('text', models.TextField(help_text='The question text')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='TextQuestion',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='defectDojo_engagement_survey.Question')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('defectDojo_engagement_survey.question',),
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('order', models.PositiveIntegerField(default=1)),
                ('label', models.TextField(default='')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='ChoiceQuestion',
            fields=[
                ('multichoice', models.BooleanField(default=False, help_text='Select one or more')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('defectDojo_engagement_survey.question',),
        ),
        migrations.CreateModel(
            name='Engagement_Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Engagement Survey',
                'verbose_name_plural': 'Engagement Surveys',
                'ordering': ('-active', 'name'),
            },
        ),
        migrations.CreateModel(
            name='Answered_Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=False)),
                ('answered_on', models.DateField(null=True)),
            ],
            options={
                'verbose_name': 'Answered Engagement Survey',
                'verbose_name_plural': 'Answered Engagement Surveys',
            },
            bases=('defectDojo_engagement_survey.engagement_surcey',),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('defectDojo_engagement_survey.answered_survey',),
        ),
        migrations.CreateModel(
            name='TextAnswer',
            fields=[
                ('answer', models.TextField(help_text='The answer text')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('defectDojo_engagement_survey.answer',),
        ),
        migrations.CreateModel(
            name='ChoiceAnswer',
            fields=[
                ('answer', models.ManyToManyField(help_text='The selected choices as the answer', to='defectDojo_engagement_survey.Choice')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('defectDojo_engagement_survey.answer',),
        ),
        migrations.AddField(
            model_name='question',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_defectdojo_engagement_survey.question_set+', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='choicequestion',
            name='choices',
            field=models.ManyToManyField(to='defectDojo_engagement_survey.Choice'),
        ),
        migrations.AddField(
            model_name='choicequestion',
            name='question_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='defectDojo_engagement_survey.Question'),
        ),
        migrations.AddField(
            model_name='engagement_survey',
            name='questions',
            field=models.ManyToManyField(to='defectDojo_engagement_survey.Question'),
        ),
        migrations.AddField(
            model_name='answered_survey',
            name='engagement',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='engagement+', to='dojo.Engagement'),
        ),
        migrations.AddField(
            model_name='answered_survey',
            name='responder',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='responder', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answered_survey',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='defectDojo_engagement_survey.Engagement_Survey'),
        ),
        migrations.AddField(
            model_name='answer',
            name='answered_survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='defectDojo_engagement_survey.Answered_Survey'),
        ),
        migrations.AddField(
            model_name='answer',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_defectdojo_engagement_survey.answer_set+', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='defectDojo_engagement_survey.Question'),
        ),
        migrations.AddField(
            model_name='textanswer',
            name='answer_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='defectDojo_engagement_survey.Answer'),
        ),
        migrations.AddField(
            model_name='choiceanswer',
            name='answer_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='defectDojo_engagement_survey.Answer'),
        ),
    ]
