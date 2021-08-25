import json

from rest_framework import serializers
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from search.document.car import CarDocument


class CarDocumentSerializer(DocumentSerializer):


    class Meta(object):
        """Meta options."""

        # Specify the correspondent document class
        document = CarDocument

        # List the serializer fields. Note, that the order of the fields
        # is preserved in the ViewSet.
        fields = (
            'id',
            'name',
            'description',
            'type',
        )