from keystoneclient.v3 import client


def create_trust(trustor_name, trustor_pass, trustor_tenant):
    keystone_config = globals.config['keystone']
    auth_urls = keystone_config['auth_urls']
    keystone = client.Client(username=keystone_config['username'], 
                             password=keystone_config['password'], 
                             project_name=keystone_config['project_name'], 
                             auth_url=)

    keystone.project.list()