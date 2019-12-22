from rest_framework.generics import ListAPIView, RetrieveAPIView
from ArhDrama.models import Show
from .serializers import ShowSerializer


class ShowListView(ListAPIView):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer


class ShowDetailView(RetrieveAPIView):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer
