from django.db import transaction
from bookstore.apps.yrb.models import YrbBook, YrbCategory, YrbClub, YrbCustomer, YrbMember, YrbOffer, YrbPurchase, YrbShipping
from django.contrib.auth.models import User

@transaction.atomic
def clean_tables():
    # Delete records in reverse order of dependencies to maintain integrity

    # Delete YrbPurchase records
    YrbPurchase.objects.all().delete()

    # Delete YrbOffer records
    YrbOffer.objects.all().delete()

    # Delete YrbBook records
    YrbBook.objects.all().delete()

    # Delete YrbCategory records
    YrbCategory.objects.all().delete()

    # Delete YrbMember records
    YrbMember.objects.all().delete()

    # Delete YrbCustomer records
    YrbCustomer.objects.all().delete()

    # Delete User records
    User.objects.all().delete()

    # Delete YrbClub records
    YrbClub.objects.all().delete()

    # Delete YrbShipping records
    YrbShipping.objects.all().delete()

    print("Tables cleaned successfully!")

# Call the clean_tables function to perform the cleanup
clean_tables()
