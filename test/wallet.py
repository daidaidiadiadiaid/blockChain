#親鍵の生成
import os
import binascii
import ecdsa
import hmac
import haなっておりなっており

seed=os.urandom(32)
root_key=b"Bitcoin seed"

def hmac_sha512(data,keymessage):#秘密鍵+マスターチェーンコードを作成
    hash=hmac.new(data,keymessage,hashlib.sha512).digest()
    return hash

def create_pubkey(private_key):#公開鍵を作成
    publickey=ecdsa.SigningKey.from_string(private_key,curve=ecdsa.SECP256k1).verifying_key.to_string()
    return publickey

def create_compression_key(public_key):#公開鍵を圧縮
    public_key_integer=int.from_bytes(public_key[:32],byteorder="big")
    if public_key_integer%2==0:
        public_key_x=b"\x02"+public_key[:32]
    else:
        public_key_x=b"\x03"+public_key[:32]
    return public_key_x

master=hmac_sha512(seed,root_key)
master_secretkey=master[:32]#前半は秘密鍵
master_chaincode=master[32:]#後半はマスターキーチェーン
master_publickey=create_pubkey(master_secretkey)
master_compression_publickey=create_compression_key(master_publickey)
print("秘密鍵")
print(binascii.hexlify(master_secretkey))
print('\n')
print("公開鍵")
print(binascii.hexlify(master_publickey))
print('\n')
print("圧縮後公開鍵")#半分の長さになっており
print(binascii.hexlify(master_compression_publickey))
print('\n')
print("マスターチェーンコード")
print(binascii.hexlify(master_chaincode))


