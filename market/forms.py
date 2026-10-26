from django.contrib.auth.models import User
from django import forms

from market.models import Listing


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ["title", "description", "price", "category", "seller_note"]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        # SECURITY: `is_staff` must NOT be here. It is Django's staff flag and
        # gates the department desk and the admin site, so letting a user set it
        # on their own profile is a privilege-escalation hole. Staff status is
        # assigned by an administrator, never self-served from this form.
        fields = ["first_name", "last_name", "email"]
