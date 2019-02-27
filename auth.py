
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
import arrow
import json as pjson
import base64

class Key(object):
    '''
    use bytes in this layer
    >>> from views import *
    >>> k = Key()
    >>> key = k.priv_key_create()
    >>> pub_key = k.pub_key_by_priv_key(key)
    >>> k.priv_key_decrypt(key, k.pub_key_encrypt(pub_key, b'123'))
    b'123'
    >>> k.pub_key_verify(pub_key, b'123', k.priv_key_sign(key, b'123'))
    True
    >>> k.sha256(b'123').hex()
    'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3'
    '''

    def priv_key_create(self):
        return RSA.generate(1024).exportKey()

    def pub_key_by_priv_key(self, priv_key):
        priv_key = RSA.importKey(priv_key)
        pub_key = priv_key.publickey()
        return pub_key.exportKey()

    def priv_key_sign(self, priv_key, data):
        priv_key = RSA.importKey(priv_key)
        cipher = pkcs1_15.new(priv_key)
        data_hash = SHA256.new(data=data)
        return cipher.sign(data_hash)

    def priv_key_decrypt(self, priv_key, data):
        priv_key = RSA.importKey(priv_key)
        cipher = PKCS1_OAEP.new(priv_key)
        return cipher.decrypt(data)

    def pub_key_encrypt(self, pub_key, data):
        pub_key = RSA.importKey(pub_key)
        cipher = PKCS1_OAEP.new(pub_key)
        return cipher.encrypt(data)

    def pub_key_verify(self, pub_key, raw_data, sign):
        pub_key = RSA.importKey(pub_key)
        cipher = pkcs1_15.new(pub_key)
        raw_data_hash = SHA256.new(data=raw_data)
        try:
            cipher.verify(raw_data_hash , sign)
            return True
        except ValueError:
            return False

    def sha256(self, data):
        return SHA256.new(data).hexdigest()

class Auth(object):
    '''
    use str in this layer
    >>> from views import *
    >>> from unittest import mock
    >>> with mock.patch.object(Auth, 'priv_key', new_callable=mock.PropertyMock) as m:
    ...     m.return_value = Key().priv_key_create()
    ...     data = {'data': 123}
    ...     auth = Auth(0)
    ...     user_id, expire, sign = auth.server_auth_create(data).split(':')
    ...     auth.server_auth_verify(int(expire), data, sign)
    ...     user_id, expire, sign = auth.client_auth_create(data).split(':')
    ...     auth.client_auth_verify(int(expire), data, sign)
    True
    True
    >>> with mock.patch.object(Auth, 'priv_key', new_callable=mock.PropertyMock) as m:
    ...     m.return_value = Key().priv_key_create()
    ...     data = None
    ...     auth = Auth(0)
    ...     user_id, expire, sign = auth.server_auth_create(data).split(':')
    ...     auth.server_auth_verify(int(expire), data, sign)
    ...     user_id, expire, sign = auth.client_auth_create(data).split(':')
    ...     auth.client_auth_verify(int(expire), data, sign)
    True
    True
    '''
    def __init__(self, user_id, pub_key):
        self.user_id = user_id
        self.server_user_id = 0
        self.pub_key = pub_key

    def server_auth_verify(self, expire, data, sign):
        if arrow.now().timestamp > expire:
            return False
        data_bytes = pjson.dumps(data, sort_keys=True, separators=(',',':')).encode()
        data_sha256 = Key().sha256(data_bytes)
        to_sign = ('%s:%s:%s'%(self.server_user_id, expire, data_sha256)).encode()
        sign = bytes.fromhex(sign)
        return Key().pub_key_verify(self.pub_key, to_sign, sign)

    def client_auth_create(self, data):
        data_bytes = pjson.dumps(data, sort_keys=True, separators=(',',':')).encode()
        data_sha256 = Key().sha256(data_bytes)
        expire = arrow.now().shift(minutes=30).timestamp
        to_sign = ('%s:%s:%s'%(self.user_id, expire, data_sha256)).encode()
        sign = Key().pub_key_encrypt(self.pub_key, to_sign)
        sign = sign.hex()
        return '%s:%s:%s'%(self.user_id, expire, sign)



