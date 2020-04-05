from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Message
from .serializer import MessageSerializer


class MessageView(APIView):
	
	def get(self, request):
		messages = Message.objects.order_by('pub_date')
		serializer = MessageSerializer(messages, many=True)
		return Response(serializer.data)
