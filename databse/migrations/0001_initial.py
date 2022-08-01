# Generated by Django 4.0.5 on 2022-07-10 17:53

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidates',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=12)),
                ('email_id', models.EmailField(blank=True, max_length=200)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('createdby_id', models.BigIntegerField(default=100)),
                ('updated_at', models.DateTimeField(default=datetime.datetime.now)),
                ('updatedby_id', models.BigIntegerField(default=100)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=12)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('createdby_id', models.BigIntegerField(default=100)),
                ('updated_at', models.DateTimeField(default=datetime.datetime.now)),
                ('updatedby_id', models.BigIntegerField(default=100)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Indivdual_reports',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('track', models.CharField(max_length=100)),
                ('initial_box', models.CharField(max_length=100)),
                ('letter_text', models.CharField(max_length=100)),
                ('rating_variable', models.CharField(max_length=100)),
                ('pace_text', models.CharField(max_length=100)),
                ('power_word_text', models.CharField(max_length=100)),
                ('volume_and_pitch', models.CharField(max_length=100)),
                ('word_cloud', models.CharField(max_length=100)),
                ('sentiment_analysis', models.CharField(max_length=100)),
                ('gesture_text', models.CharField(max_length=100)),
                ('content_rating', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Interactions',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('candidate_feedback', models.CharField(max_length=100)),
                ('report_sent_to_user', models.BooleanField(default=False)),
                ('channel', models.CharField(choices=[('slack', 'SLACK'), ('whatsapp', 'WHATSAPP'), ('telegram', 'TELEGRAM')], max_length=20)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('createdby_id', models.BigIntegerField(default=100)),
                ('updated_at', models.DateTimeField(default=datetime.datetime.now)),
                ('updatedby_id', models.BigIntegerField(default=100)),
                ('is_active', models.BooleanField(default=True)),
                ('candidate_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='databse.candidates')),
                ('individual_report_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='databse.indivdual_reports')),
            ],
        ),
        migrations.CreateModel(
            name='LeaderBoard_report',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('track', models.CharField(max_length=100)),
                ('initial_box', models.CharField(max_length=100)),
                ('letter_text', models.CharField(max_length=100)),
                ('rating_variable', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigIntegerField(max_length=10, primary_key=True, serialize=False)),
                ('interaction_welcome', models.CharField(max_length=500)),
                ('interaction_instruction', models.CharField(max_length=500)),
                ('interaction_completion_message', models.CharField(max_length=500)),
                ('bot_error_message', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('createdby_id', models.BigIntegerField(default=100)),
                ('updated_at', models.DateTimeField(default=datetime.datetime.now)),
                ('updatedby_id', models.BigIntegerField(default=100)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(choices=[('standard', 'Standard'), ('premium', 'Premium'), ('enterprise', 'Enterprise')], max_length=50)),
                ('interaction_allowed', models.CharField(choices=[('one', 'One'), ('ten', 'Ten'), ('unlimited', 'Unlimited')], max_length=50)),
                ('interaction_type_allowed', models.CharField(choices=[('audio', 'audio'), ('audio_video', 'audio_video'), ('any', 'any')], max_length=50)),
                ('responces', models.CharField(choices=[('unlimited', 'unlimited')], max_length=50)),
                ('time_at', models.CharField(choices=[('one_quarter', 'one_quarter'), ('unlimited', 'unlimited')], max_length=50)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('createdby_id', models.BigIntegerField(default=100)),
                ('updated_at', models.DateTimeField(default=datetime.datetime.now)),
                ('updatedby_id', models.BigIntegerField(default=100)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=500)),
                ('answer_format', models.CharField(choices=[('one_quarter', 'one_quarter'), ('unlimited', 'unlimited')], max_length=50)),
                ('ideal_answer', models.CharField(max_length=500)),
                ('should_rate', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('createdby_id', models.BigIntegerField(default=100)),
                ('updated_at', models.DateTimeField(default=datetime.datetime.now)),
                ('updatedby_id', models.BigIntegerField(default=100)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Scores',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('resume_score', models.IntegerField(default=0, max_length=2)),
                ('pace', models.IntegerField(default=0, max_length=2)),
                ('power_words', models.IntegerField(default=0, max_length=2)),
                ('value_scale', models.IntegerField(default=0, max_length=2)),
                ('pitch_range', models.IntegerField(default=0, max_length=2)),
                ('gesture', models.IntegerField(default=0, max_length=2)),
                ('content_score', models.IntegerField(default=0, max_length=2)),
                ('overall', models.IntegerField(default=0, max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('access_code', models.IntegerField()),
                ('who_can_initiate', models.CharField(choices=[('bot', 'Bot'), ('user', 'User'), ('both', 'Both')], default='bot', max_length=50)),
                ('interview_mode', models.CharField(choices=[('audio', 'Audio'), ('video', 'Video')], default='audio', max_length=50)),
                ('track', models.CharField(choices=[('hire', 'Hire'), ('learn', 'Learn')], default='slack', max_length=50)),
                ('collect_email', models.BooleanField(default=False)),
                ('collect_candidate_email', models.BooleanField(default=False)),
                ('voice_match', models.BooleanField(default=False)),
                ('hiring_email', models.EmailField(max_length=200)),
                ('collect_resume', models.BooleanField(default=False)),
                ('job_code', models.BigIntegerField(default=1111)),
                ('job_title', models.CharField(choices=[('backend', 'Backend'), ('frontend', 'Frontend'), ('fullStack', 'Fullstack'), ('hr', 'Hr')], default='slack', max_length=50)),
                ('job_discription', models.CharField(max_length=500)),
                ('total_question', models.IntegerField(max_length=100)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('createdby_id', models.BigIntegerField(default=100)),
                ('updated_at', models.DateTimeField(default=datetime.datetime.now)),
                ('updatedby_id', models.BigIntegerField(default=100)),
                ('is_active', models.BooleanField(default=True)),
                ('company_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='databse.companies')),
                ('notification_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='databse.notifications')),
            ],
        ),
        migrations.CreateModel(
            name='Score_per_question',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('likebality', models.IntegerField(default=0, max_length=2)),
                ('charm', models.IntegerField(default=0, max_length=2)),
                ('confidence', models.IntegerField(default=0, max_length=2)),
                ('fluency', models.IntegerField(default=0, max_length=2)),
                ('content', models.IntegerField(default=0, max_length=2)),
                ('overall', models.IntegerField(default=0, max_length=2)),
                ('question_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='databse.questions')),
                ('score_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='databse.scores')),
            ],
        ),
        migrations.CreateModel(
            name='Responces',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('response', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('createdby_id', models.BigIntegerField(default=100)),
                ('updated_at', models.DateTimeField(default=datetime.datetime.now)),
                ('updatedby_id', models.BigIntegerField(default=100)),
                ('is_active', models.BooleanField(default=True)),
                ('candidate_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='databse.candidates')),
                ('interaction_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='databse.interactions')),
                ('question_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='databse.questions')),
            ],
        ),
        migrations.AddField(
            model_name='questions',
            name='test_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='databse.test'),
        ),
        migrations.AddField(
            model_name='interactions',
            name='score_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='databse.scores'),
        ),
        migrations.AddField(
            model_name='interactions',
            name='test_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='databse.test'),
        ),
        migrations.AddField(
            model_name='companies',
            name='plan_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='databse.plan'),
        ),
    ]
