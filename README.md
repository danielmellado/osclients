OSClients
=========

Collection of [OpenStack] client helpers

In order to help and ease the process of using OpenStack credentials and clients
with [ipython] or any python interpreter, this library allows you to call them
directly using the environment variables from keystonerc files.

# Usage
First, we'll have to export the needed variables to the environment, using the
keystonerc file from the OpenStack installation

```sh
$ source keystonerc
```
That file should be close to this example
```sh
export OS_USERNAME =
export OS_TENANT_NAME =
export OS_PASSWORD =
export OS_AUTH_URL =
export PS1 = '[\u@\h \W(keystone_admin)]\$ '
```

After this just log into your Python interpreter:
```sh
$ ipython
```
import the module
```python
import osclients
```
Now we can just call the clients directly, without having to bother to 
authenticate manually for each one of them:
```python
nc = osclients.get_neutron_client()
networks = nc.list_networks()
```

# Development

Want to contribute? Great! Feel free to fork or add comments / PR !

[ipython]:
    http:
        //ipython.org/
[OpenStack]:
    http:
        //openstack.org/
