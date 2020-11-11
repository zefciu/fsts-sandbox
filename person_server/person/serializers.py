from rest_framework.serializers import ModelSerializer
from person.models import Person


class PersonSerializer(ModelSerializer):

    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'gender', 'birthdate']
