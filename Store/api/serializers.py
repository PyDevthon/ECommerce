from rest_framework import serializers
from ..models import Contact


class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        exclude = ('id',)

    def validate_phone(self, data):
        if data == '1234567890':
            raise serializers.ValidationError("Please enter correct phone number")
        return data
