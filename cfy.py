# -*- coding: utf-8 -*-=
from cloudify_rest_client import CloudifyClient

client = CloudifyClient('10.10.1.6')
blueprints = client.blueprints.list()

for blueprint in blueprints:
    print blueprint.id