def arbitrary_serialize(obj):
    if obj.__class__.__name__ == "a class":
        # from djangobase.apps.api.serializers.thatclass import ThatClassSerializer
        # return ThatClassSerializer(obj).data
        pass
    else:
        raise Exception("Cannot serialize this type: {}".format(obj.__class__.__name____))