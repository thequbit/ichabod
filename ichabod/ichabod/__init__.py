from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import (
    DBSession,
    Base,
    Root,
    )

import resources

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings, root_factory=resources.root_factory)
    config.include('pyramid_chameleon')

    config.add_static_view('static', 'static', cache_max_age=3600)

    config.add_route('/', '/')

    

    #
    # Customers
    #
    #config.add_route('customers','/customers/')
    #config.add_route('customer', '/customer/:{id}')

    '''
    config.add_route('customer/comments', '/customer/:{id}/messages/')
    config.add_route('customer/labels', '/customer/:{id}/labels/')
    config.add_route('customer/accounts', '/customer/:{id}/accounts/')
    config.add_route('customer/contacts', '/customer/:{id}/contacts/')
    config.add_route('customer/leads', '/customer/:{id}/leads/')
    config.add_route('customer/oppertunities', '/customer/:{id}/oppertunities/')
    config.add_route('customer/jobs', '/customer/:{id}/jobs/')
    config.add_route('customer/projects', '/customer/:{id}/')
    config.add_route('customer/collections', '/customer/:{id}/collections/'
    config.add_route('customer/requirement_categories', '/customer/:{id}/requirement_categories/')
    config.add_route('customer/requirements', '/customer/:{id}/requirements/')

    #
    # Accounts
    #
    config.add_route('accounts', '/accounts/')
    config.add_route('account', '/account/:{id}/')
    config.add_route('account/oppertunities', '/account/:{id}/oppertunities/')
    config.add_route('account/comments', '/account/:{id}/comments/')
    config.add_route('account/labels', '/account/:{id}/labels/')
    config.add_route('account/contacts', '/account/:{id}/contacts')
    
    #
    # Contacts
    #
    config.add_route('contacts', '/contacts/')
    config.add_route('contact', '/contact/:{id}/'
    config.add_route('contact/comments', '/contact/:{id}/comments/')
    config.add_route('contact/labels', '/contact/:{id}/labels')

    #
    # Leads
    #
    config.add_route('leads', '/leads/')
    config.add_route('lead', '/lead/:{id}/')
    config.add_route('lead/comments', '/lead/:{id}/comments/')
    config.add_route('lead/labels', '/lead/:{id}/labels/')
    config.add_route('lead/contacts', '/lead/:{id}/contacts/')

    #
    # Opertunities
    #
    config.add_route('oppertunities', '/oppertunities/')
    config.add_route('opportunity','/opertunity/:{id}/comments/')
    config.add_route('opportunity/comments', '/opportunity/:{id}/comments/')
    config.add_route('opportunity/labels', '/opportunity/:{id}/labels/')
    config.add_route('opportunity/contacts', '/opportunity/:{id}/contacts/')

    #
    # Job
    #
    config.add_route('jobs', '/jobs/')
    config.add_route('job', '/job/:{id}/')
    config.add_route('job/comments', '/job/:{id}/comments/')
    config.add_route('job/labels', '/job/:{id}/labels/')
    config.add_route('job/contacts', '/job/:{id}/contacts/')
    config.add_route('job/projects', '/job/:{id}/projects/')

    #
    # Projcets
    #
    config.add_route('projects', '/projects/')
    config.add_route('project', '/project/:{id}/')
    config.add_route('project/comments', '/project/:{id}/comments/')
    config.add_route('project/labels', '/project/:{id}/labels/')
    config.add_route('project/contacts', '/project/:{id}/contacts/')
    config.add_route('project/collections', '/project/:{id}/collections/')
    
    #
    # Collections
    #
    config.add_route('collections', '/collections/')
    config.add_route('collection', '/collection/:{id}/')
    config.add_route('collection/comments', '/collection/:{id}/comments/')
    config.add_route('collection/labels', '/collection/:{id}/labels/')
    config.add_rotue('collection/contacts', '/collection/:{id}/contacts/')
    #config.add_route('collection/files', '/collection/:{id}/files/')

    #
    # Files
    #
    #config.add_route('files', '/files/')
    #config.add_route('file', '/file/:{id}/')

    #
    # Issues
    #
    config.add_route('issues', '/issues/')
    config.add_route('issue', '/issue/:{id}/')
    config.add_rotue('issue/comments', '/issue/:{id}/comments/')
    config.add_rotue('issue/labels', '/issue/:{id}/labels/')
    config.add_rotue('issue/contacts', '/issue/:{id}/contacts/') 
    
    #
    # Issue Priorities
    #
    config.add_route('issue_priorities', '/issue_priorities/')
    config.add_route('issue_priority', '/issue_priority/:{id}/')
    config.add_route('issue_priority/comments', '/issue_priority/:{id}/comments/')
    config.add_route('issue_priority/labels', '/issue_priority/:{id}/labels/')
    config.add_route('issue_priority/issues', '/issue_priority/:{id}/issues/')

    '''

    config.scan()

    return config.make_wsgi_app()
