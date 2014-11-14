import logging
import os

import glanceclient.v2.client as glclient
import keystoneclient.v2_0.client as ksclient
from neutronclient.v2_0 import client as neutronclient
import novaclient.v1_1.client as nvclient

logging.basicConfig(level=logging.DEBUG)


def __get_keystone_credentials():
    d = {}
    d['username'] = os.environ['OS_USERNAME']
    d['password'] = os.environ['OS_PASSWORD']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['tenant_name'] = os.environ['OS_TENANT_NAME']
    d['endpoint_type'] = 'public'
    return d


def __get_nova_credentials():
    d = {}
    d['username'] = os.environ['OS_USERNAME']
    d['api_key'] = os.environ['OS_PASSWORD']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['project_id'] = os.environ['OS_TENANT_NAME']
    return d


def get_nova_client():
    return nvclient.Client(**__get_nova_credentials())


def get_keystone_client():
    return ksclient.Client(**__get_keystone_credentials())


def get_neutron_client():
    keystone = get_keystone_client()
    endpoint_url = keystone.service_catalog.url_for(service_type='network',
                                                    endpoint_type='internal')
    token = keystone.auth_token
    return neutronclient.Client(endpoint_url=endpoint_url, token=token)


def get_glance_client():
    keystone = get_keystone_client()
    glance_endpoint = keystone.service_catalog.url_for(
        service_type='image',
        endpoint_type='internal')
    return glclient.Client(glance_endpoint, token=keystone.auth_token)
