
import models

class Resource(dict):
    def __init__(self, name, parent):
        self.__name__ = name
        self.__parent__ = parent

class Root(Resource):

    def add_resource(self, name, orm_class):
        self[name] = ORMContainer(name, self, self.request, orm_class)

    def __init__(self, request):
        self.request = request
        self.add_resource('customers', models.Customers)
        self.add_resource('accounts', models.Accounts)
        self.add_resource('contacts', models.Contacts)
        self.add_resource('leads', models.Leads)
        self.add_resource('oppertunities', models.Oppertunities)
        self.add_resource('jobs', models.Jobs)
        self.add_resource('projects', models.Projects)
        self.add_resource('collections', models.Collections)
        self.add_resource('files', models.Files)

root_factory = Root

class ORMContainer(dict):
    
    def __init__(self, name, parent, request, orm_class):
        self.__name__  = name
        self.__parent__ = parent
        self.request = request
        self.orm_class = orm_class

    def __getitem__(self, key):
        try:
            key = int(key)
        except ValueError:
            raise KeyError(key)
        obj = models.DBSession.query(self.orm_class).get(key)
        if obj is None:
            raise KeyError(key)
        obj.__name__ = key
        obj.__parent__ = self
        return obj

    def to_dict(self):
        resp = {
            self.__name__ : [c.to_dict() for c in self.orm_class.get_all()],
        }
        return resp
