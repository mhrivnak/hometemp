from datetime import datetime
import time

from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.http import require_GET
from gviz_api import DataTable

import models


SCHEMA = [
    ('datetime', 'datetime', 'Date/Time'),
    ('home', 'number', 'Inside'),
    ('target', 'number', 'Target'),
    ('outside', 'number', 'Outside'),
]

@require_GET
def graph(request):
    # TODO finish this
    try:
        start = datetime.fromtimestamp(float(request.REQUEST['start']))
    except KeyError:
        return HttpResponseBadRequest('Must provide a start value')
    end = datetime.fromtimestamp(request.REQUEST.get('end', time.time()))

    data = models.Record.objects.filter(datetime__gt=start, datetime__lt=end).order_by('datetime')
    table = DataTable(SCHEMA, (r.to_gviz_row() for r in data))
    return HttpResponse(table.ToJSon())

