# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models

# Create your models here.

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
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
        
class YrbBook(models.Model):
    title = models.CharField(primary_key=True, max_length=25)
    year = models.SmallIntegerField()
    language = models.CharField(max_length=10, blank=True, null=True)
    cat = models.ForeignKey('YrbCategory', models.DO_NOTHING, db_column='cat')
    weight = models.SmallIntegerField()

    class Meta:
        
        db_table = 'yrb_book'
        unique_together = (('title', 'year'),)


class YrbCategory(models.Model):
    cat = models.CharField(primary_key=True, max_length=10)

    class Meta:
        
        db_table = 'yrb_category'


class YrbClub(models.Model):
    club = models.CharField(primary_key=True, max_length=15)
    desp = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        
        db_table = 'yrb_club'


class YrbCustomer(models.Model):
    cid = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        
        db_table = 'yrb_customer'


class YrbMember(models.Model):
    club = models.OneToOneField(YrbClub, models.DO_NOTHING, db_column='club', primary_key=True)
    cid = models.ForeignKey(YrbCustomer, models.DO_NOTHING, db_column='cid')

    class Meta:
        
        db_table = 'yrb_member'
        unique_together = (('club', 'cid'),)


class YrbOffer(models.Model):
    club = models.OneToOneField(YrbClub, models.DO_NOTHING, db_column='club', primary_key=True)
    title = models.ForeignKey(YrbBook, models.DO_NOTHING, db_column='title')
    year = models.SmallIntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        
        db_table = 'yrb_offer'
        unique_together = (('club', 'title', 'year'),)


class YrbPurchase(models.Model):
    cid = models.SmallIntegerField(primary_key=True)
    club = models.ForeignKey(YrbMember, models.DO_NOTHING, db_column='club')
    title = models.CharField(max_length=25)
    year = models.SmallIntegerField()
    whenp = models.DateTimeField()
    qnty = models.SmallIntegerField()

    class Meta:
        
        db_table = 'yrb_purchase'
        unique_together = (('cid', 'club', 'title', 'year', 'whenp'),)


class YrbShipping(models.Model):
    weight = models.SmallIntegerField(primary_key=True)
    cost = models.DecimalField(unique=True, max_digits=5, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'yrb_shipping'
        
class YrbUser(models.Model):
    cid = models.OneToOneField(YrbCustomer, models.DO_NOTHING, db_column='cid', primary_key=True)
    email = models.CharField(max_length=25)
    password_hash = models.CharField(max_length=50)

    class Meta:
        
        db_table = 'yrb_user'
        unique_together = (('cid', 'email', 'password_hash'),)