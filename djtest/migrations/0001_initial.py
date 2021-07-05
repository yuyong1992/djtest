# Generated by Django 3.2.4 on 2021-06-05 00:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, unique=True, verbose_name='模块名称')),
                ('sequence', models.IntegerField(default=0, verbose_name='显示顺序')),
            ],
            options={
                'ordering': ['sequence'],
            },
        ),
        migrations.CreateModel(
            name='Api',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, verbose_name='接口名称')),
                ('method', models.CharField(default='GET', max_length=45, verbose_name='请求方法')),
                ('protocol', models.CharField(default='HTTP', max_length=10, verbose_name='请求协议')),
                ('url', models.CharField(default='', max_length=256, verbose_name='接口地址')),
                ('params', models.JSONField(default=dict, max_length=256, verbose_name='查询参数')),
                ('header', models.JSONField(default=dict, max_length=256, verbose_name='请求头信息')),
                ('body', models.JSONField(max_length=1024, null=True, verbose_name='表单字段及描述信息')),
                ('bodytype', models.CharField(choices=[('none', 'none'), ('multipart/form-data', 'mutipart/form-data'), ('x-www-form-urlencoded', 'x-www-form-urlencoded'), ('application/json', 'application/json'), ('binary', 'binary')], default='none', max_length=30, verbose_name='消息体类型')),
                ('status', models.CharField(choices=[('1', '启用'), ('2', '禁用'), ('3', '废弃')], default='启用', max_length=4, verbose_name='接口状态')),
                ('ceratetime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updatetime', models.DateTimeField(verbose_name='更新时间')),
                ('isbase', models.CharField(choices=[('1', '是'), ('2', '否')], default='否', max_length=4, verbose_name='是否基线化')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djtest.module', verbose_name='所属模块')),
            ],
            options={
                'ordering': ['updatetime'],
            },
        ),
    ]
