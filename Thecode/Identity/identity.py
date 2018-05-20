
from faker import Faker
fake = Faker()
from sawtooth_signing import create_context
from sawtooth_signing import CryptoFactory
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import base64
import ipfsapi
##https://media.readthedocs.org/pdf/python-ipfs-api/latest/python-ipfs-api.pdf


class GenerateKeys(object):


    def __init__(self):
        self.private_key_str = None 
        self.public_key_str = None
        self.private_key = None 
        self.public_key = None

    def generate_keys(self):
        """
        Generate public privatekeys

        https://sawtooth.hyperledger.org/docs/core/releases/1.0/_autogen/sdk_submit_tutorial_python.html
        """

        context = create_context('secp256k1')
        private_key = context.new_random_private_key()
        signer = CryptoFactory(context).new_signer(private_key)

        self.private_key_hex =  private_key.as_hex()
        self.signer_public_key=signer.get_public_key().as_hex(),
        return (private_key_hex, signer_public_key)


        # generate private/public key pair
        self.private_key = rsa.generate_private_key(backend=default_backend(), public_exponent=65537, key_size=2048)

        # get public key in OpenSSH format
        self.public_key = self.private_key.public_key()
        
        
        pem_public = self.public_key.public_bytes(serialization.Encoding.OpenSSH, serialization.PublicFormat.OpenSSH)

        # get private key in PEM container format
        pem = self.private_key.private_bytes(encoding=serialization.Encoding.PEM, 
                        format=serialization.PrivateFormat.TraditionalOpenSSL,
                        encryption_algorithm=serialization.NoEncryption())

        # decode to printable strings
        self.private_key_str = pem.decode('utf-8')
        self.public_key_str = pem_public.decode('utf-8')

        print('Private key = ')
        print(self.private_key_str)
        print('Public key = ')
        print(self.public_key_str)


    def load_public_private_keys(self):
        ##load public and private keys from BIGchainB
        return 

    #https://medium.com/@raul_11817/rsa-with-cryptography-python-library-462b26ce4120
    def encrypt_object(self, message):
        ciphertext = self.public_key.encrypt(
            message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA1()),
                algorithm=hashes.SHA1(),
                label=None
                )
            )

        ciphertext  = str(base64.b64encode(ciphertext), encoding='utf-8')

        data_to_sign = bytes(message, encoding='utf8') if not isinstance(message, bytes) else message

        signer = self.private_key.signer(
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
        hashes.SHA256()
            )

        signer.update(data_to_sign)
        signature = str(
                base64.b64encode(signer.finalize()),
            encoding='utf8'
        )


        return (ciphertext, signature)

    def test_keys(self):
        """
        Test if the encryption and decryption process
        """





class StoreDetails(object):
    ##https://github.com/ipfs/py-ipfs-api
    
    
    @staticmethod
    def storedetails(data):
        """
        Store the Identity encrypted with Public key 
        and hashes signed by digital signature and store them on blockchainDB.
        TODO: Encrypt this data, with the public key of this user, May be bigchaindb public key of this user
        TODO: You somehow force this file to be stored by atleast three other peers. If one of the peer goes down
            It should stores all the files to some other peers.
        """


        api = ipfsapi.connect('127.0.0.1', 5001)
        res = api.add_json({"cipher_text": data["cipher_text"], "signature": data["signature"]})
        ##res{'Hash': 'QmWxS5aNTFEc9XbMX1ASvLET1zrqEaTssqt33rVZQCQb22', 'Name': 'test.txt'}
        print (res)







class GetUserDetails:

    def __init__(self, identity_image, self_image):
        """
        to check if there is a match between the image of the person and get
        the relevant details from the adhaar 

        """
        self.identity_image = identity_image
        self.self_image = self
        
        
        
        
    def adhaar(self):
        """
        If the identity_image is of kind adhaar
        
        TODO: Use any thirdparty of write your own functions for convolution neural nets to get the 
        similirity between the two
        True if there is a match in the identities 
        """


        return (fake.credit_card_number(), fake.address(), fake.name(), True)



if __name__ == "__main__":
    _instance = GenerateKeys()
    _instance.generate_keys()
    (ciphertext, signature) = _instance.encrypt_object("hey now, Dude how are you")
    StoreDetails.storedetails((ciphertext, signature))

