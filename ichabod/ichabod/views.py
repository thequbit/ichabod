import json

from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    #MyModel,
    Root,
    #Comments,
    #Labels,
    Customers,
    #Accounts,
    #Contacts,
    #Leads,
    #Oppertunities,
    #Jobs,
    #Projects,
    #Collections,
    #Files,
    #Issues,
    #IssuePriorities,
    #RequirementCategories,
    #Requirements,
    )




@view_config(request_method='GET', route_name='/', renderer='templates/index.mak')
def index(self): 

    return {}

'''
@view_config(request_method='GET', route_name='/customers', renderer='json')
def get_customers(self):

    return {}
'''

@view_config(renderer='json')
def get_customer(request):

    resp = request.context.to_dict() 

    print 'about to return the things ...'
    print resp

    return resp

'''
@view_config(context=Accounts, renderer='json')
def get_customer(request):

    return dict(customer=request.context.to_dict())
'''


'''
@view_config(request_method='GET', route_name='customers', renderer='json')
def get_customers(request):

    return the_customers

@view_config(request_method='GET', route_name='accounts', renderer='json')
def get_customer(request):

    id = request.matchdict['id']

    return the_customers[0]
'''

'''
@view_config(request_method='GET', route_name='', renderer='json')
def get_customer_coments(request):

    id = request.matchdict['id']

    return []

@view_config(request_method='GET', route_name='accounts', renderer='json')
def get_accounts(request):

    return []
'''
