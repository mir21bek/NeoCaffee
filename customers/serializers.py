# serializers.py

from rest_framework import serializers
from .models import CustomerUser, CustomerProfile
from order.serializers import OrderSerializer, OrderItemSerializer


class CustomerRegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    phone_number = serializers.CharField(required=True)

    class Meta:
        model = CustomerUser
        fields = ["username", "phone_number", "date_of_birth"]
        extra_kwargs = {
            "date_of_birth": {"format": "%d %m %Y"},
        }

    def save(self):
        phone_number = self.validated_data["phone_number"]
        user = CustomerUser(
            username=self.validated_data["username"],
            phone_number=phone_number,
            date_of_birth=self.validated_data["date_of_birth"],
        )
        user.save()
        return user


class CustomerLoginSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(required=True)

    class Meta:
        model = CustomerUser
        fields = ["phone_number"]


class CustomerCheckOTPSerializer(serializers.ModelSerializer):
    otp = serializers.IntegerField()

    class Meta:
        model = CustomerUser
        fields = ["otp"]


#
#
# class WaiterLoginSerializer(serializers.ModelSerializer):
#     login = serializers.CharField(required=True)
#     password = serializers.CharField(required=True, write_only=True)
#
#     class Meta:
#         model = WaiterUser
#         fields = ["login", "password"]
#
#
# class WaiterCheckOTPSerializer(serializers.ModelSerializer):
#     otp = serializers.IntegerField()
#
#     class Meta:
#         model = WaiterUser
#         fields = ["otp"]
#
#
# class BaristaLoginSerializer(serializers.ModelSerializer):
#     phone_number = serializers.CharField(required=True)
#
#     class Meta:
#         model = BaristaUser
#         fields = ["phone_number"]
#
#
class CustomerProfileSerializer(serializers.ModelSerializer):
    user = CustomerRegistrationSerializer(read_only=True)
    phone_number = serializers.CharField(read_only=True)
    orders = OrderItemSerializer(
        many=True, read_only=True, source="user.get_all_orders"
    )
    bonuses_added = serializers.SerializerMethodField()

    def get_bonuses_added(self, obj):
        return obj.bonuses_added()

    class Meta:
        model = CustomerProfile
        fields = ("id", "user", "phone_number", "bonuses", "orders", "bonuses_added")
