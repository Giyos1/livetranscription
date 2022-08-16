from rest_framework import serializers


class AudioSerializers(serializers.Serializer):
    audio_file = serializers.FileField()
