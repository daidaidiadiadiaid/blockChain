import hashlib
hash_hello=hashlib.sha256(b"hello").hexdigest()#ハッシュ化
print(hash_hello)

import os 
import binascii

private_key=os.urandom(32) #秘密鍵の作成
print(private_key)
print(binascii.hexlify(private_key))#32ビットへの変換

import ecdsa
public_key=ecdsa.SigningKey.from_string(private_key,curve=ecdsa.SECP256k1).verifying_key.to_string()#秘密鍵をもとに公開鍵を生成
print(binascii.hexlify(public_key))
public_key_y=int.from_bytes(public_key[32:],"big")

if public_key_y%2==0:
    public_key_compressed=b"\x02"+public_key[:32]
else:
    public_key_compressed=b"\x03"+public_key[:32]
print(binascii.hexlify(public_key_compressed))


#アドレスを生成 みんなが見やすいようにするために



import base58

# ステップ1: プレフィックス(0x04)を公開鍵の先頭に追加
prefix_and_pubkey = b"\x04" + public_key

# ステップ2: プレフィックス付き公開鍵をSHA-256でハッシュ化
intermediate = hashlib.sha256(prefix_and_pubkey).digest()  # 公開鍵をハッシュ化

# ステップ3: RIPEMD-160ハッシュ関数を初期化
ripemd160 = hashlib.new('ripemd160')

# ステップ4: SHA-256ハッシュの結果をRIPEMD-160でハッシュ化
ripemd160.update(intermediate)
hash160 = ripemd160.digest()  # もう一度ハッシュ化

# ステップ5: プレフィックス(0x00)を追加して最終結果を作成
prefix_and_hash160 = b"\x00" + hash160

# ステップ6: ダブルハッシュ (SHA-256を2回適用) を計算
double_hash = hashlib.sha256(hashlib.sha256(prefix_and_hash160).digest()).digest()

# ステップ7: チェックサムはダブルハッシュの最初の4バイト
checksum = double_hash[:4]

# ステップ8: アドレスの前段階はプレフィックスとハッシュ160にチェックサムを追加
pre_address = prefix_and_hash160 + checksum

# ステップ9: base58でエンコードしてアドレスを生成
address = base58.b58encode(pre_address)

# アドレスを表示 (バイト列から文字列にデコード)
print(address.decode())



