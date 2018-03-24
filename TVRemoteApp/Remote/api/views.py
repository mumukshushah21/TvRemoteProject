from rest_framework.generics import ListAPIView,RetrieveAPIView,UpdateAPIView
from Remote.models import Show
from .serializers import ListSerializersChannel

class Channellist(ListAPIView):
	queryset=Show.objects.all()
	serializer_class=ListSerializersChannel


'''
class BlogDetailList(RetrieveAPIView):
	queryset=Pst.objects.all()
	serializer_class=ListSerializers
	lookup_field='title'



class BlogUpdateList(UpdateAPIView):
	queryset=Pst.objects.all()
	serializer_class=ListSerializers
	lookup_field='title'

'''