from __future__ import unicode_literals

from collections import OrderedDict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(('GET',))
def api_root(request, format=None):
    """# Djangobase API
    The Djangobase API is a RESTful interface to the following data models. Navigate to
    the route for each to browse individual documentation on each resource.
    Some features of the API require authentication to access. If you do not
    posess a username/password or an authentication token, contact [Brian](mailto:bjacobel@gmail.com).
    ---
    """

    return Response(OrderedDict([
        #('class', reverse("class-list", request=request, format=format)),
    ]))