import os
import sys
from SettingsModule.settings import bigchaindb_app_id, bigchaindb_app_key, bigchaindb_testnet_url
from bigchaindb_driver import BigchainDB

##https://test.bigchaindb.com/api/v1/
##we going to use the bigchaindb testnet for the time being, Till the time we create our own 
##testnet, There is no point suffering from Servers cost till then.


class BIGchainDBTransactions(object):

    def __init__(self):
        self.tokens = {}
        self.tokens['app_id'] = bigchaindb_app_id
        self.tokens['app_key'] = bigchaindb_app_key 
        self.bdb = BigchainDB(bigchaindb_testnet_url, headers=self.tokens)
        


    def create_identity(self):
        """
        This method will store the adhaar image hash present on IPFS as the identiy on bIGCHaindb as 
        Create transaction
        """


        return 



    def transfer_identity(self, public_key):
        """
        share identity to the public_key created by create_identity
        """


        return 

