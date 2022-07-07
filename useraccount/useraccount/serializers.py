from rest_framework import serializers
from .models import Useraccount
class UseraccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Useraccount
        fields = ['accountid', 'accountname', 'email']
