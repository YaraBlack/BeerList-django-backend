from rest_framework import serializers
from .models import Beer


class BeerSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(
        required=True, allow_blank=False, max_length=255
    )
    alcohol = serializers.DecimalField(
        required=False, max_digits=3, decimal_places=1
    )
    ingredients = serializers.CharField(required=False, max_length=255)
    style = serializers.CharField(required=False, max_length=80)
    description = serializers.CharField(required=False, max_length=255)
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Beer
        fields = [
            "id",
            "name",
            "alcohol",
            "ingredients",
            "style",
            "description",
            "created",
            "updated",
        ]

    def create(self, validated_data):
        """
        Create and return a new "Beer" instance, given the validated data.
        """
        return Beer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing "Beer" instance, given the validated data.
        """
        instance.name = validated_data.get("name", instance.name)
        instance.alcohol = validated_data.get("alcohol", instance.alcohol)
        instance.ingredients = validated_data.get(
            "ingredients", instance.ingredients
        )
        instance.description = validated_data.get(
            "description", instance.description
        )
        instance.style = validated_data.get("style", instance.style)
        instance.save()

        return instance
