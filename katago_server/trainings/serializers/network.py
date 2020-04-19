from rest_framework.serializers import HyperlinkedModelSerializer

from katago_server.trainings.models import Network


class NetworkSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Network
        fields = ("url", "name", "network_size", "nb_parameters", "model_architecture_details", "model_file", "parent_network")


class LimitedNetworkSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Network
        fields = ["url", "name", "model_file"]