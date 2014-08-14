#!/usr/bin/python

import consulate
from time import sleep

session = consulate.Consulate()

while True:
    # find all available demo servers registered on consul
    demo_services = session.catalog.service('consul-demo-server')

    # iterate over them and show what we found
    for service in demo_services:
        print(
            'consul-demo-server found on node {} ({}) using port {}'.format(
                service['Node'],
                service['Address'],
                service['ServicePort']
            )
        )

    if not demo_services:
        print('no consul-demo-server available')
    print('')

    # let's check again soon
    sleep(1)
