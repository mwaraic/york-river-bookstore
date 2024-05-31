from django.db import models


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
    name = models.CharField(max_length=20, null=True)
    city = models.CharField(max_length=15, null=True)

    class Meta:

        db_table = 'yrb_customer'


class YrbMember(models.Model):
    club = models.OneToOneField(
        YrbClub, models.DO_NOTHING, db_column='club', primary_key=True)
    cid = models.ForeignKey(YrbCustomer, models.DO_NOTHING, db_column='cid')

    class Meta:

        db_table = 'yrb_member'
        unique_together = (('club', 'cid'),)


class YrbOffer(models.Model):
    club = models.ForeignKey(YrbClub, models.DO_NOTHING, db_column='club')
    title = models.ForeignKey(YrbBook, models.DO_NOTHING, db_column='title')
    year = models.SmallIntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    offerid = models.SmallIntegerField(primary_key=True)

    class Meta:

        db_table = 'yrb_offer'
        unique_together = (('club', 'title', 'year', 'offerid'),)


class YrbPurchase(models.Model):
    id = models.AutoField(primary_key=True)
    cid = models.SmallIntegerField()
    club = models.CharField(max_length=15)
    title = models.CharField(max_length=25)
    year = models.SmallIntegerField()
    whenp = models.DateTimeField()
    qnty = models.SmallIntegerField()
    offerid = models.ForeignKey(
        YrbOffer, models.DO_NOTHING, db_column='offerid')

    class Meta:

        db_table = 'yrb_purchase'
        unique_together = (('id', 'club', 'title', 'year',
                           'whenp', 'offerid', 'cid'),)


class YrbShipping(models.Model):
    weight = models.SmallIntegerField(primary_key=True)
    cost = models.DecimalField(unique=True, max_digits=5, decimal_places=2)

    class Meta:

        db_table = 'yrb_shipping'
        unique_together = (('weight', 'cost'),)