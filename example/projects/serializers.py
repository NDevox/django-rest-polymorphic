from rest_framework import serializers

from rest_polymorphic.serializers import PolymorphicSerializer

from .models import Project, ArtProject, ResearchProject


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('topic', )


class ArtProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtProject
        fields = ('topic', 'artist', 'url')
        extra_kwargs = {
            'url': {'view_name': 'project-detail', 'lookup_field': 'pk'},
        }


class ResearchProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchProject
        fields = ('topic', 'supervisor')


class ProjectPolymorphicSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        Project: ProjectSerializer,
        ArtProject: ArtProjectSerializer,
        ResearchProject: ResearchProjectSerializer
    }
