from simple_settings import settings
import os
import sys

file_name = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(file_name))




##https://test.bigchaindb.com/api/v1/
##we going to use the bigchaindb testnet for the time being, Till the time we create our own 
##testnet, There is no point suffering from Servers cost till then.

from bigchaindb_driver import BigchainDB
tokens = {}
tokens['app_id'] = settings.bigchaindb_app_id
tokens['app_key'] = settings.bigchaindb_app_key 
bdb = BigchainDB(settings.bigchaindb_testnet_url, headers=tokens)
print (settings.bigchaindb_app_id)


#class Transactions(object):


