from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """serialize a name field for testing our APIview"""
    name = serializers.CharField(max_length =10)
    