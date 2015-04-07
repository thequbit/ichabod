from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    #MyModel,
    )

@view_config(route_name='/', renderer='templates/index.mak')
def index(request):

    return {}

