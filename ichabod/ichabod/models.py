import datetime
import time

import transaction

from sqlalchemy import (
    Column,
    ForeignKey,
    Index,
    Integer,
    Text,
    Unicode,
    DateTime,
    )

from sqlalchemy.ext.declarative import declarative_base

import sqlalchemy

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    relationship,
    backref,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension(),expire_on_commit=False))

# borrowed from:
#     http://pieceofpy.com/blog/2011/08/01/pyramid-and-traversal-with-a-restful-interface/
class IchabodBase(object):

    def __init__():
        print 'IchabodBase.__init__()'
 
    @classmethod
    def __getitem__(cls, k):
        try:
        #if True:
            print 'query'
            result =  DBSession().query(cls).filter_by(id=k).one()
            result.__parent__ = result
            result.__name__ = str(k)
            return result
        except:
            print 'error'
            raise KeyError
    @classmethod
    def __len__(cls):
        return DBSession().query(cls).count()    
    @classmethod
    def __iter__(cls):
        return (x for x in DBSession().query(cls))
    @classmethod
    def get_all(cls):
        return (x for x in DBSession().query(cls))

Base = declarative_base(cls=IchabodBase)

'''
class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    value = Column(Integer)

Index('my_index', MyModel.name, unique=True, mysql_length=255)
'''

class Root(dict):

    __name__ = ''
    __parent__ = None

    def __init__(self, request):
        pass

    def __getitem__(self, key):
        print "Root.__getitem__(), Key: {0}".format(key)
        if key == 'customers':
            print "Root.__getitem__(), Returning Customers(key)"
            return Customers()
        raise KeyError

class CreationMixin():

    @classmethod
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @classmethod
    def add(cls, session, **kwargs):
        with transaction.manager:
            thing = cls(**kwargs)
            session.add(thing)
        return thing

    @classmethod
    def get_all(cls, session):
        print 'CreationMixin().get_all()'
        with transaction.manager:
            things = session.query(
                cls,
            ).all()
            retThings = []
            for t in things:
                retThings.append(t.to_dict())
            print 'CreationMixin().get_all(), retThings: {0}'.format(retThings)
        return retThings

    @classmethod
    def get_by_id(cls, session, id):
        with transaction.manager:
            thing = session.query(
                cls,
            ).filter(
                cls.id == id,
            ).first()
        return thing

    @classmethod
    def delete_by_id(cls, session, id):
        with transaction.manager:
            thing = cls.get_by_id(id)
            session.delete(thing)
            transaction.commit()
        return thing

    @classmethod
    def update_by_id(cls, session, id, *args, **kargs):
        with transaction.manager:
             thing = cls.get_by_id(id)
             
             # TODO: magic
             
             session.add()
             transaction.commit()
        return thing

    # taken from:
    #     https://gist.github.com/pjenvey/3808830
    def __json__(self, request):
        """
        Converts all the properties of the object into a dict for use in json.
        You can define the following in your class

        _json_eager_load :
            list of which child classes need to be eagerly loaded. This applies
            to one-to-many relationships defined in SQLAlchemy classes.

        _base_blacklist :
            top level blacklist list of which properties not to include in JSON

        _json_blacklist :
            blacklist list of which properties not to include in JSON

        :param request: Pyramid Request object
        :type request: <Request>
        :return: dictionary ready to be jsonified
        :rtype: <dict>
        """
 
        props = {}
 
        # grab the json_eager_load set, if it exists
        # use set for easy 'in' lookups
        json_eager_load = set(getattr(self, '_json_eager_load', []))
        # now load the property if it exists
        # (does this issue too many SQL statements?)
        for prop in json_eager_load:
            getattr(self, prop, None)
 
        # we make a copy because the dict will change if the database
        # is updated / flushed
        options = self.__dict__.copy()
 
        # setup the blacklist
        # use set for easy 'in' lookups
        blacklist = set(getattr(self, '_base_blacklist', []))
        # extend the base blacklist with the json blacklist
        blacklist.update(getattr(self, '_json_blacklist', []))
 
        for key in options:
            # skip blacklisted, private and SQLAlchemy properties
            if key in blacklist or key.startswith(('__', '_sa_')):
                continue
 
            # format and date/datetime/time properties to isoformat
            obj = getattr(self, key)
            if isinstance(obj, datetime.datetime):
                props[key] = obj.isoformat()
            else:
                # get the class property value
                attr = getattr(self, key)
                # let see if we need to eagerly load it
                if key in json_eager_load:
                    # this is for SQLAlchemy foreign key fields that
                    # indicate with one-to-many relationships
                    if not hasattr(attr, 'pk') and attr:
                        # jsonify all child objects
                        attr = [x.__json__(request) for x in attr]
                else:
                    # convert all non integer strings to string or if
                    # string conversion is not possible, convert it to
                    # Unicode
                    if attr and not isinstance(attr, (int, float)):
                        try:
                            attr = str(attr)
                        except UnicodeEncodeError:
                            attr = unicode(attr)  # .encode('utf-8')
 
                props[key] = attr
 
        return props

'''
class Users(Base, CreationMixin):

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)

    first
    last
    email
    pass_salt
    pass_hash

    comments = relationship('Comments', backref='contact')
    labels = relationship('Labels', backref='contact')
'''

class Comments(Base, CreationMixin):

    __name__ = 'comment'
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    
    contents = Column(Unicode(255))
    created = Column(DateTime)
    edited = Column(DateTime, nullable=True)    

    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=True)
    account_id = Column(Integer, ForeignKey('accounts.id'), nullable=True)
    contact_id = Column(Integer, ForeignKey('contacts.id'), nullable=True)
    lead_id = Column(Integer, ForeignKey('leads.id'), nullable=True)
    opertunity_id = Column(Integer, ForeignKey('opertunities.id'), nullable=True)
    job_id = Column(Integer, ForeignKey('jobs.id'), nullable=True)
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=True)
    collection_id = Column(Integer, ForeignKey('collections.id'), nullable=True)
    file_id = Column(Integer, ForeignKey('files.id'), nullable=True)
    issue_id = Column(Integer, ForeignKey('issues.id'), nullable=True)
    issue_priority_id = Column(Integer, ForeignKey('issue_priorities.id'), nullable=True)
    requirement_category_id = Column(Integer, ForeignKey('requirement_categories.id'), nullable=True)
    requirement_id = Column(Integer, ForeignKey('requrements.id'), nullable=True)

    def to_dict(self):
        resp = dict(
            contents = self.contents,
            created = self.created.iso(),
            edited = self.created.iso(),
        )
        print 'Comments.to_dict(), resp: {0}'.format(resp)
        return resp

class Labels(Base, CreationMixin):

    __name__ = 'label'
    __tablename__ = 'labels'
    id = Column(Integer, primary_key=True)

    name = Column(Unicode(255))
    description = Column(Unicode(65535))

    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=True)
    account_id = Column(Integer, ForeignKey('accounts.id'), nullable=True)
    contact_id = Column(Integer, ForeignKey('contacts.id'), nullable=True)
    lead_id = Column(Integer, ForeignKey('leads.id'), nullable=True)
    opertunity_id = Column(Integer, ForeignKey('opertunities.id'), nullable=True)
    job_id = Column(Integer, ForeignKey('jobs.id'), nullable=True)
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=True)
    collection_id = Column(Integer, ForeignKey('collections.id'), nullable=True)
    file_id = Column(Integer, ForeignKey('files.id'), nullable=True)
    issue_id = Column(Integer, ForeignKey('issues.id'), nullable=True)
    issue_priority_id = Column(Integer, ForeignKey('issue_priorities.id'), nullable=True)
    requirement_category_id = Column(Integer, ForeignKey('requirement_categories.id'), nullable=True)
    requirement_id = Column(Integer, ForeignKey('requrements.id'), nullable=True)

    def to_dict(self):
        resp = dict(
            id = self.id,
            name = self.name,
            description = self.description,
        )
        print "Labels.to_dict(), resp: {0}".format(resp)
        return resp

class Customers(Base, CreationMixin):

    __name__ = 'customer'
    #__parent__ = Root

    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    
    name = Column(Unicode(255))
    description = Column(Unicode(65535))

    accounts = relationship('Accounts', backref='customer', lazy='joined')
    comments = relationship('Comments', backref='customer', lazy='joined')
    labels = relationship('Labels', backref='customer', lazy='joined')

    def to_dict(self):
        resp = dict(
            id = self.id,
            name = self.name,
            description = self.description,
            accounts = [a.to_dict() for a in self.accounts],
            comments = [c.to_dict() for c in self.comments],
            lables = [l.to_dict() for l in self.labels],
        )
        print 'Customers.to_dict(), resp: {0}'.format(resp)
        return resp

class Accounts(Base, CreationMixin):

    __name__ = 'account'
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True)
    
    customer_id = Column(Integer, ForeignKey('customers.id'))
    
    name = Column(Unicode)
    description = Column(Unicode)

    jobs = relationship('Jobs', backref='account', lazy='joined')
    contacts = relationship('Contacts', backref='account', lazy='joined')
    comments = relationship('Comments', backref='account', lazy='joined')
    labels = relationship('Labels', backref='account', lazy='joined')

    def to_dict(self):
        resp = dict(
            id = self.id,
            #customer = self.customer.to_dict(),
            name = self.name,
            description = self.description,
            jobs = [j.to_dict() for j in self.jobs],
            contacts = [c.to_dict() for c in self.contacts],
            comments = [c.to_dict() for c in self.comments],
            labels = [l.to_dict() for l in self.labels],
        )
        print "Accounts.to_dict(), resp: {0}".format(resp)
        return resp

class Contacts(Base, CreationMixin):

    __name__ = 'contact'
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)

    account_id = Column(Integer, ForeignKey('accounts.id'), nullable=True)
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=True)
    lead_id = Column(Integer, ForeignKey('leads.id'), nullable=True)
    opertunity_id = Column(Integer, ForeignKey('opertunities.id'), nullable=True)
    job_id = Column(Integer, ForeignKey('jobs.id'), nullable=True)
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=True)
    collection_id = Column(Integer, ForeignKey('collections.id'), nullable=True)
    file_id = Column(Integer, ForeignKey('files.id'), nullable=True)
    issue_id = Column(Integer, ForeignKey('issues.id'), nullable=True)

    first = Column(Unicode)
    last = Column(Unicode)
    email = Column(Unicode)
    office_phone = Column(Unicode)
    mobile_phone = Column(Unicode)
    fax = Column(Unicode)

    comments = relationship('Comments', backref='contact', lazy='joined')
    labels = relationship('Labels', backref='contact', lazy='joined')

    def to_dict(self):
        resp = dict(
            id = self.id,
            first = self.first,
            last = self.last,
        )
        print "Contacts.to_dict(), resp: {0}".format(resp)
        return resp 

class Leads(Base, CreationMixin):

    __tablename__ = 'leads'
    id = Column(Integer, primary_key=True)   
 
    account_id = Column(Integer, ForeignKey('accounts.id'))

    name = Column(Unicode)
    description = Column(Unicode)

    contacts = relationship('Contacts', backref='lead')
    comments = relationship('Comments', backref='lead')
    labels = relationship('Labels', backref='lead')

class Oppertunities(Base, CreationMixin):

    __tablename__ = 'opertunities'
    id = Column(Integer, primary_key=True)

    account_id = Column(Integer, ForeignKey('accounts.id'))
    lead_id = Column(Integer, ForeignKey('leads.id'))    

    name = Column(Unicode)
    description = Column(Unicode)

    contacts = relationship('Contacts', backref='opertunity')
    comments = relationship('Comments', backref='opertunity')
    labels = relationship('Labels', backref='opertunity')

class Jobs(Base, CreationMixin):

    __tablename__ = 'jobs'
    id = Column(Integer, primary_key=True)
    
    account_id = Column(Integer, ForeignKey('accounts.id'))
    
    name = Column(Unicode)

    projects = relationship('Projects', backref='job')
    contacts = relationship('Contacts', backref='job')
    comments = relationship('Comments', backref='job')
    labels = relationship('Labels', backref='job')

    def to_dict(self):
        resp = dict(
            id = self.id,
            name = self.name,
            projects = [p.to_dict() for p in self.projects],
            contacts = [c.to_dict() for c in self.contacts],
            comments = [c.to_dict() for c in self.comments],
            labels = [l.to_dict() for l in self.labels], 
        )
        return resp

class Projects(Base, CreationMixin):

    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True)

    job_id = Column(Integer, ForeignKey('jobs.id'))

    name = Column(Unicode)

    collections = relationship('Collections', backref='project')
    contacts = relationship('Contacts', backref='project')
    comments = relationship('Comments', backref='project')
    labels = relationship('Labels', backref='project')

    def to_dict(self):
        resp = dict(
            name = self.name,
            #collections = [c.to_dict() for c in self.collections],
            contacts = [c.to_dict() for c in self.contacts],
            comments = [c.to_dict() for c in self.comments],
            labels = [l.to_dict() for l in self.labels],
        )
        return resp

class Collections(Base, CreationMixin):

    __tablename__ = 'collections'
    id = Column(Integer, primary_key=True)

    project_id = Column(Integer, ForeignKey('projects.id'))

    name = Column(Unicode)
    description = Column(Unicode)

    files = relationship('Files', backref='collection')
    contacts = relationship('Contacts', backref='collection')
    comments = relationship('Comments', backref='collection')
    labels = relationship('Labels', backref='collection')

class Files(Base, CreationMixin):

    __tablename__ = 'files'
    id = Column(Integer, primary_key=True)

    collection_id = Column(Integer, ForeignKey('collections.id')) 

    name = Column(Unicode)
    description = Column(Unicode)
    location = Column(Text)

    contacts = relationship('Contacts', backref='file')
    comments = relationship('Comments', backref='file')
    labels = relationship('Labels', backref='file')

class Issues(Base, CreationMixin):

    __tablename__ = 'issues'
    id = Column(Integer, primary_key=True)

    issue_priority_id = Column(Integer, ForeignKey('issue_priorities.id'), nullable=True)

    title = Column(Unicode)
    contents = Column(Unicode)

    contacts = relationship('Contacts', backref='issue')
    comments = relationship('Comments', backref='issue')
    labels = relationship('Labels', backref='issue')

class IssuePriorities(Base, CreationMixin):

    __tablename__ = 'issue_priorities'
    id = Column(Integer, primary_key=True)

    contents = Column(Unicode)
    description = Column(Unicode)

    issues = relationship('Issues', backref='issue_priority')
    comments = relationship('Comments', backref='issue_priority')
    labels = relationship('Labels', backref='issue_priority')

class RequirementCategories(Base, CreationMixin):

    __tablename__ = 'requirement_categories'
    id = Column(Integer, primary_key=True)

    project_id = Column(Integer, ForeignKey('projects.id'))

    name = Column(Unicode)
    description = Column(Unicode)

    requirements = relationship('Requirements', backref='requirement_category')
    comments = relationship('Comments', backref='requirement_category')
    labels = relationship('Labels', backref='requirement_category')

class Requirements(Base, CreationMixin):

    __tablename__ = 'requrements'
    id = Column(Integer, primary_key=True)

    #project_id = Column(Integer, ForeignKey('projects.id'))
    requirement_category_id = Column(Integer, ForeignKey('requirement_categories.id'))

    title = Column(Unicode)
    contents = Column(Unicode)

    comments = relationship('Comments', backref='requirement')
    labels = relationship('Labels', backref='requirement')

