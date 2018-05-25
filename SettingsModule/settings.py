##documentation available at https://pypi.org/project/simple-settings/
import motor
import ipfsapi

bigchaindb_app_id = '9f9cbef4'
bigchaindb_app_key = 'c9017b4d69146e5d51d2a3da8a2f1c82'
bigchaindb_testnet_url = 'https://test.bigchaindb.com'
import motor
mongo_ip = "localhost"
mongo_db_name = "feynmen"
#client = motor.motor_tornado.MotorClient('mongodb://localhost:27017')
mongo_db_uri = "mongodb://%s:27017"%(mongo_ip)
mongo_db = motor.motor_tornado.MotorClient(mongo_db_uri)[mongo_db_name]

ipfs_ip = "localhost"
ipfs_port = 5001
ipfs_connection = ipfsapi.connect(ipfs_ip, ipfs_port)

user_collection_name = "users"
jwt_secret = "a"


SIMPLE_SETTINGS = {
    'OVERRIDE_BY_ENV': True,
    'CONFIGURE_LOGGING': True,
 
   #'REQUIRED_SETTINGS': ('API_TOKEN', 'DB_USER'),
   # 'DYNAMIC_SETTINGS': {
   #     'backend': 'redis',
   #     'pattern': 'DYNAMIC_*',
   #     'auto_casting': True,
   #     'prefix': 'MYAPP_'
   # }
}



TIME_ZONE =  'Asia/Kolkata'


def indian_time():
    india  = timezone(TIME_ZONE)
    n_time = datetime.now(india)
    return n_time.strftime("%b %d %Y %H:%M:%S")