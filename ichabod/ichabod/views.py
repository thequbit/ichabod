import json

from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    #MyModel,
    )

the_customers = [
        {
            "id": 47,
            "name": "General Electric",
            "notes": "General Electric is a great company.  We do a lot of business with them.",
            "lables": [
                {
                    "id": 481,
                    "text": "big-money"
                },
                {
                    "id": 123,
                    "text": "net-120"
                }
            ],
            "accounts": [
                {
                    "id": 34,
                    "name": "Niskayuna",
                    "primary_contact_id": 92,
                    "primary_contact_name": "Jim Smith",
                    "primary_contact_email": "jsmith@ge.com",
                    "primary_contact_phone": "(123)-456-7890",
                    "lead_count": 4,
                    "opertunity_count": 3,
                    "projects": [
                        {
                            "id": 76,
                            "name": "Transponder",
                            "value": 458271
                        },
                        {
                            "id": 89,
                            "name": "Mechatronics",
                            "value": 45913
                        }
                    ]
                },
                {
                    "id": 34,
                    "name": "Oklahoma City",
                    "primary_contact_id": 76,
                    "primary_contact_name": "Martha Stewart",
                    "primary_contact_email": "mstewart@ge.com",
                    "primary_contact_phone": "(987)-654-3210",
                    "lead_count": 12,
                    "opertunity_count": 7,
                    "projects": [
                        {
                            "id": 67,
                            "name": "Doodlething",
                            "value": 7582
                        },
                        {
                            "id": 12,
                            "name": "Bobber",
                            "value": 6614151
                        }
                    ]
                }
            ]
        } 
    ]

@view_config(request_method='GET', route_name='/', renderer='templates/index.mak')
def index(request):

    return {}

@view_config(request_method='GET', route_name='customers', renderer='json')
def customers(request):

    return the_customers

@view_config(request_method='GET', route_name='customer', renderer='json')
def customer(request):

    id = request.matchdict['id']

    return the_customers[0]
