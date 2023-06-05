from rest_framework.serializers import ModelSerializer

from main.models import Movies


class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movies
        fields = ['title','imdb_id','published_data']
        