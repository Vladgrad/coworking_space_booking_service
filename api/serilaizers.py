from rest_framework import serializers
from api.models import Coworking, Desk, Booking
from django.contrib.auth import get_user_model


User = get_user_model()


class RegisterSerialier(serializers.Serializer):
       email = serializers.EmailField(required=True)
       password = serializers.CharField(required=True, write_only=True)
       
       
       def create(self, validated_data):
              return User.objects.create_user(
                     username=validated_data['email'], 
                     email=validated_data['email'],   
                     password=validated_data['password']
              )
              
              
class LoginSerilaizer(serializers.Serializer):
       email = serializers.EmailField(required=True)
       password = serializers.CharField(required=True)
       
class CoworkingSerilaizer(serializers.ModelSerializer):
       class Meta:
              model = Coworking
              fields = [
                     'id',
                     'title',
                     'city',
                     'address',
              ]
              read_only_fields = ['id']
              
              
class DeskSerializer(serializers.ModelSerializer):
       class Meta:
              model = Desk
              fields = [
                     'desk_id',
                     'coworking',
                     'name',
                     'capacity',
                     'is_active',
                     'created_at',
              ]
              read_only_fields = ['desk_id', 'created_at']
              
              
class BookingSerializer(serializers.ModelSerializer):
       class Meta:
              model = Booking
              fields = [
                     'booking_id',
                     'desk',
                     'client',
                     'date',
                     'slot',
                     'status',
                     'created_at',
              ]
              read_only_fields = ['booking_id', 'created_at']
              

        
                 
       