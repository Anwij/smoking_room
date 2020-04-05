from rest_framework import serializers
from .models import Message
from main.serializer import UserSerializer

class MessageSerializer(serializers.ModelSerializer):
	
	#sender = serializers.SlugRelatedField(slug_field="name", read_only=True)
	#receiver = serializers.SlugRelatedField(slug_field="name", read_only=True)
	
	sender = UserSerializer(read_only=True)
	receiver = UserSerializer(read_only=True)
	
	class Meta:
		model = Message
		fields = ('sender', 'receiver', 'message')

	
