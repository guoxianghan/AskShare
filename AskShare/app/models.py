#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Definition of models.
"""
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Article(models.Model):
    aid = models.IntegerField(primary_key=True)
    title = models.TextField()  # This field type is a guess.
    content = models.TextField()  # This field type is a guess.
    tags = models.TextField()  # This field type is a guess.
    createtime = models.DateTimeField()
    status = models.IntegerField()
    upvote = models.IntegerField()
    downvote = models.IntegerField()
    questionstatus = models.IntegerField()
    isdeleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'article'


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    username = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Comment(models.Model):
    cid = models.IntegerField(primary_key=True)
    articleid = models.IntegerField()
    uid = models.IntegerField()
    atuid = models.IntegerField()
    content = models.TextField()  # This field type is a guess.
    createtime = models.IntegerField()
    isdeleted = models.IntegerField()
    accepted = models.IntegerField()
    deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'comment'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class LoginHistory(models.Model):
    lid = models.IntegerField(primary_key=True)
    uid = models.IntegerField()
    ip = models.TextField()  # This field type is a guess.
    createtime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'login_history'


class Tags(models.Model):
    tid = models.IntegerField()
    tag = models.TextField()  # This field type is a guess.
    createtime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tags'


class Transaction(models.Model):
    tran_id = models.IntegerField()
    uid = models.IntegerField()
    transactionuid = models.IntegerField()
    transaction_plat = models.IntegerField()
    createtime = models.DateTimeField()
    memo = models.TextField()  # This field type is a guess.
    transaction_status = models.IntegerField()
    money = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'transaction'


class TransactionDetails(models.Model):
    trandetail_id = models.IntegerField()
    uid = models.IntegerField()
    tid = models.IntegerField()
    operation = models.IntegerField()
    createtime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'transaction_details'


class User(models.Model):
    uid = models.IntegerField()
    login_plat_type = models.IntegerField()
    name = models.TextField()  # This field type is a guess.
    email = models.TextField(db_column='Email')  # Field name made lowercase. This field type is a guess.
    qq = models.IntegerField(db_column='QQ')  # Field name made lowercase.
    weichat = models.TextField(db_column='WeiChat')  # Field name made lowercase. This field type is a guess.
    sina = models.TextField(db_column='Sina')  # Field name made lowercase. This field type is a guess.
    alipay = models.TextField()  # This field type is a guess.
    createtime = models.DateTimeField()
    logintime = models.DateTimeField()
    status = models.IntegerField()
    guid = models.TextField()  # This field type is a guess.
    phone = models.TextField()  # This field type is a guess.
    pwd = models.TextField()  # This field type is a guess.
    designation = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'user'
