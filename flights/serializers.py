from rest_framework import serializers
from flights.models import Flight, Booking
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken


class FlightsCreateSerializer(serializers.ModelSerializer):
    passengers = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Booking
        fields = ["id", "date", "flight", "passengers"]


class FlightsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['id', 'destination', 'time', 'price']


class BookingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'date', 'flight', 'passengers']


class BookingUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['date', 'passengers']


User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "password", "first_name", "last_name"]

    def create(self, validated_data):
        username = validated_data["username"]
        password = validated_data["password"]
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()
        return validated_data


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    access = serializers.CharField(read_only=True, allow_blank=True)

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise serializers.ValidationError("This username does not exist")

        if user.check_password(password):

            payload = RefreshToken.for_user(user)
            token = str(payload.access_token)

            data["access"] = token
            return data

        else:
            raise serializers.ValidationError(
                "Incorrect username/password combination!")
