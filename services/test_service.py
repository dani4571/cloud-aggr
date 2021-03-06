from globals import *
from keystoneclient.v3 import client


def create_trust(trustor_name, trustor_pass, trustor_tenant):
    aggr_creds = config['keystone']
    auth_urls = aggr_creds['auth_urls']
    trustor_keystones = []
    for url in auth_urls:
        keystone = client.Client(username=trustor_name, 
                                 password=trustor_pass, 
                                 project_name=trustor_tenant, 
                                 auth_url=url)
        trustor_keystones.append(keystone)

    print dir(trustor_keystones[0])
    
    #keystone.project.list()
