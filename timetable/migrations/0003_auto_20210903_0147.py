# Generated by Django 3.2.4 on 2021-09-02 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0002_auto_20210903_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='fri_10_11',
            field=models.CharField(default='', max_length=41, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='fri_11_12',
            field=models.CharField(default='', max_length=41, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='fri_12_1',
            field=models.CharField(default='', max_length=41, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='fri_2_3',
            field=models.CharField(default='', max_length=41, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='fri_3_4',
            field=models.CharField(default='', max_length=41, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='fri_4_5',
            field=models.CharField(default='', max_length=41, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='fri_8_9',
            field=models.CharField(default='', max_length=41, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='fri_9_10',
            field=models.CharField(default='', max_length=41, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='mon_10_11',
            field=models.CharField(default='', max_length=41, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='mon_11_12',
            field=models.CharField(default='', max_length=41, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='mon_12_1',
            field=models.CharField(default='', max_length=41, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='mon_2_3',
            field=models.CharField(default='', max_length=41, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='mon_3_4',
            field=models.CharField(default='', max_length=41, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='mon_4_5',
            field=models.CharField(default='', max_length=41, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='mon_8_9',
            field=models.CharField(default='', max_length=41, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='mon_9_10',
            field=models.CharField(default='', max_length=41, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='thur_10_11',
            field=models.CharField(default='', max_length=41, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='thur_11_12',
            field=models.CharField(default='', max_length=41, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='thur_12_1',
            field=models.CharField(default='', max_length=41, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='thur_2_3',
            field=models.CharField(default='', max_length=41, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='thur_3_4',
            field=models.CharField(default='', max_length=41, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='thur_4_5',
            field=models.CharField(default='', max_length=41, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='thur_8_9',
            field=models.CharField(default='', max_length=41, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='thur_9_10',
            field=models.CharField(default='', max_length=41, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='tue_10_11',
            field=models.CharField(default='', max_length=41, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='tue_11_12',
            field=models.CharField(default='', max_length=41, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='tue_12_1',
            field=models.CharField(default='', max_length=41, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='tue_2_3',
            field=models.CharField(default='', max_length=41, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='tue_3_4',
            field=models.CharField(default='', max_length=41, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='tue_4_5',
            field=models.CharField(default='', max_length=41, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='tue_8_9',
            field=models.CharField(default='', max_length=41, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='tue_9_10',
            field=models.CharField(default='', max_length=41, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='wed_10_11',
            field=models.CharField(default='', max_length=41, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='wed_11_12',
            field=models.CharField(default='', max_length=41, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='wed_12_1',
            field=models.CharField(default='', max_length=41, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='wed_2_3',
            field=models.CharField(default='', max_length=41, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='wed_3_4',
            field=models.CharField(default='', max_length=41, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='wed_4_5',
            field=models.CharField(default='', max_length=41, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='wed_8_9',
            field=models.CharField(default='', max_length=41, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='wed_9_10',
            field=models.CharField(default='', max_length=41, null=True),
        ),
    ]
