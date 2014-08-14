uWSGI Consul.io integration demo
================================

This is a proof of concept on the usage of the **consul** plugin for **uWSGI**.

This illustrates how simple it can be to create a distributed application running through **uWSGI** which can scale up and down automatically by using **Consul.io** for service discovery.

Prerequisities
==============

* A running `consul` agent : http://www.consul.io/intro/getting-started/install.html
* A `uWSGI` installation with the consul plugin available : https://github.com/unbit/uwsgi-consul
* The `consulate` python library (available via pip)

Run the POC
===========

## Client
Run a `client` which will query the consul agent for the `consul-demo-server` service and list them on the console:

* Open a terminal and run the `client`
```sh
python client.py
```

* At first, there should be no available service
```
no consul-demo-server available
```

## Servers
uWSGI will spawn two `servers` pretending to be listening on port `2001` and port `2002` and register them on the configured consul agent (localhost by default):

* Open a terminal and run `uwsgi` using the provided INI
```sh
uwsgi --ini uwsgi-consul-demo.ini --ini uwsgi-consul-demo.ini:server1 --ini uwsgi-consul-demo.ini:server2
```

## Result
On the `client` terminal, you can see that it discovered the new services automatically. You can CTRL+C and restart the uwsgi servers on the other terminal and watch the show.
```
    consul-demo-server found on node MYHOST (XX.XX.XX.XX) using port 2001
    consul-demo-server found on node MYHOST (XX.XX.XX.XX) using port 2002
```

Congratulations, you've experienced your first automated service discovery application !
