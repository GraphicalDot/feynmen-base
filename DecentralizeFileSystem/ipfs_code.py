
import base64
import ipfsapi
from SettingsModule.settings import ipfs_connection


class StoreDetails(object):
    ##https://github.com/ipfs/py-ipfs-api
    
    
    @staticmethod
    def store_ipfs(data):
        """
        Store the Identity encrypted with Public key 
        and hashes signed by digital signature and store them on blockchainDB.
        TODO: Encrypt this data, with the public key of this user, May be bigchaindb public key of this user
        TODO: You somehow force this file to be stored by atleast three other peers. If one of the peer goes down
            It should stores all the files to some other peers.
        """


        res = ipfs_connection.add_json({"cipher_text": data[0], "signature": data[1]})
        ##res{'Hash': 'QmWxS5aNTFEc9XbMX1ASvLET1zrqEaTssqt33rVZQCQb22', 'Name': 'test.txt'}
        print (res)
        return res
