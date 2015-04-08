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

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    relationship,
    backref,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension(),expire_on_commit=False))
Base = declarative_base()

'''
class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    value = Column(Integer)

Index('my_index', MyModel.name, unique=True, mysql_length=255)
'''

class CreationMixin():

    @classmethod
    def add(cls, session, **kwargs):
        with transaction.manager:
            session.add(cls(**kwargs))

    @classmethod
    def get_all(cls, session):
        with transaction.manager:
            things = session.query(
                cls,
            ).all()
        return things

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

class Comments(Base, CreationMixin):

    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    
    contents = Column(Unicode)
    creation_datetime = Column(DateTime)
    edited_datetime = Column(DateTime, nullable=True)    

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

class Labels(Base, CreationMixin):

    __tablename__ = 'labels'
    id = Column(Integer, primary_key=True)

    name = Column(Unicode)
    description = Column(Unicode)

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

class Customers(Base, CreationMixin):

    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    
    name = Column(Unicode)
    description = Column(Unicode)

    accounts = relationship('Accounts', backref='customer')
    comments = relationship('Comments', backref='customer')
    lables = relationship('Labels', backref='customer')

class Accounts(Base, CreationMixin):

    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True)
    
    customer_id = Column(Integer, ForeignKey('customers.id'))
    
    name = Column(Unicode)
    description = Column(Unicode)

    contacts = relationship('Contacts', backref='account')
    comments = relationship('Comments', backref='account')
    lables = relationship('Labels', backref='account')

class Contacts(Base, CreationMixin):

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

    comments = relationship('Comments', backref='contact')
    lables = relationship('Labels', backref='contact')

class Leads(Base, CreationMixin):

    __tablename__ = 'leads'
    id = Column(Integer, primary_key=True)   
 
    account_id = Column(Integer, ForeignKey('accounts.id'))

    name = Column(Unicode)
    description = Column(Unicode)

    contacts = relationship('Contacts', backref='lead')
    comments = relationship('Comments', backref='lead')
    lables = relationship('Labels', backref='lead')

class Opertunities(Base, CreationMixin):

    __tablename__ = 'opertunities'
    id = Column(Integer, primary_key=True)

    account_id = Column(Integer, ForeignKey('accounts.id'))
    lead_id = Column(Integer, ForeignKey('leads.id'))    

    name = Column(Unicode)
    description = Column(Unicode)

    contacts = relationship('Contacts', backref='opertunity')
    comments = relationship('Comments', backref='opertunity')
    lables = relationship('Labels', backref='opertunity')

class Job(Base, CreationMixin):

    __tablename__ = 'jobs'
    id = Column(Integer, primary_key=True)
    
    account_id = Column(Integer, ForeignKey('accounts.id'))
    
    name = Column(Unicode)

    projects = relationship('Projects', backref='job')
    contacts = relationship('Contacts', backref='job')
    comments = relationship('Comments', backref='job')
    lables = relationship('Labels', backref='job')

class Projects(Base, CreationMixin):

    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True)

    job_id = Column(Integer, ForeignKey('jobs.id'))

    name = Column(Unicode)

    collections = relationship('Collections', backref='project')
    contacts = relationship('Contacts', backref='project')
    comments = relationship('Comments', backref='project')
    lables = relationship('Labels', backref='project')

class Collections(Base, CreationMixin):

    __tablename__ = 'collections'
    id = Column(Integer, primary_key=True)

    project_id = Column(Integer, ForeignKey('projects.id'))

    name = Column(Unicode)
    description = Column(Unicode)

    files = relationship('Files', backref='collection')
    contacts = relationship('Contacts', backref='collection')
    comments = relationship('Comments', backref='collection')
    lables = relationship('Labels', backref='collection')

class Files(Base, CreationMixin):

    __tablename__ = 'files'
    id = Column(Integer, primary_key=True)

    collection_id = Column(Integer, ForeignKey('collections.id')) 

    name = Column(Unicode)
    description = Column(Unicode)
    location = Column(Text)

    contacts = relationship('Contacts', backref='file')
    comments = relationship('Comments', backref='file')
    lables = relationship('Labels', backref='file')

class Issues(Base, CreationMixin):

    __tablename__ = 'issues'
    id = Column(Integer, primary_key=True)

    issue_priority_id = Column(Integer, ForeignKey('issue_priorities.id'), nullable=True)

    title = Column(Unicode)
    contents = Column(Unicode)

    contacts = relationship('Contacts', backref='issue')
    comments = relationship('Comments', backref='issue')
    lables = relationship('Labels', backref='issue')

class IssuePriorities(Base, CreationMixin):

    __tablename__ = 'issue_priorities'
    id = Column(Integer, primary_key=True)

    contents = Column(Unicode)
    description = Column(Unicode)

    issues = relationship('Issues', backref='issue_priority')
    comments = relationship('Comments', backref='issue_priority')
    lables = relationship('Labels', backref='issue_priority')

class RequirementCategories(Base, CreationMixin):

    __tablename__ = 'requirement_categories'
    id = Column(Integer, primary_key=True)

    project_id = Column(Integer, ForeignKey('projects.id'))

    name = Column(Unicode)
    description = Column(Unicode)

    requirements = relationship('Requirements', backref='requirement_category')
    comments = relationship('Comments', backref='requirement_category')
    lables = relationship('Labels', backref='requirement_category')

class Requirements(Base, CreationMixin):

    __tablename__ = 'requrements'
    id = Column(Integer, primary_key=True)

    #project_id = Column(Integer, ForeignKey('projects.id'))
    requirement_category_id = Column(Integer, ForeignKey('requirement_categories.id'))

    title = Column(Unicode)
    contents = Column(Unicode)

    comments = relationship('Comments', backref='requirement')
    lables = relationship('Labels', backref='requirement')

