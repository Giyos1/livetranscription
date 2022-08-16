from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AudioSerializers
from .utils import get_audio


# Create your views here.

class AudioView(APIView):
    def post(self, request):
        audio = request.data["audio"]
        text = get_audio(audio)
        return Response(data={'txt': text})
