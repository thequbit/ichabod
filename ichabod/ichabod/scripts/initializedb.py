import os
import sys
import transaction

from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pyramid.scripts.common import parse_vars

from ..models import (
    DBSession,
    #MyModel,
    Base,
    Labels,
    Customers,
    Accounts,
    )


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
    #with transaction.manager:
    #    model = MyModel(name='one', value=1)
    #    DBSession.add(model)

    customer = Customers.add(
        session = DBSession,
        name = 'GE',
        description = 'General Eletric Corp.',
    )

    Labels.add(
        session = DBSession,
        customer_id = customer.id,
        name = "Important",
        description = "Max Important!",
    )

    account = Accounts.add(
        session = DBSession,
        customer_id = customer.id,
        name = 'GE Location X',
        description = 'General Electric Location X',
    )

