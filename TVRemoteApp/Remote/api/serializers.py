from rest_framework.serializers import ModelSerializer
from Remote.models import Show


class ListSerializersChannel(ModelSerializer):
	class Meta:
		model=Show
		fields=[
			'S_id',
			'S_name',
			'Monday',
		]
