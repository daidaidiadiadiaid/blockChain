import hashlib
input_text="satoshi"
for nonce in range(20):
    input_date=input_text+str(nonce)
    hash=hashlib.sha256(input_date.encode("UTF-8")).hexdigest()
    print(hash)

#proof of work

class Block():#ブロック
    def __init__(self,data,prev_hash):
        self.index=0
        self.nonce=0
        self.prev_hash=prev_hash #一個前のデータ
        self.data=data

    def blockhash(self): #ブロックチェーンの全データにナンス値を加えてハッシュ化
        blockheader=str(self.index)+str(self.prev_hash)+str(self.data)+str(self.nonce)
        block_hash=hashlib.sha256(blockheader.encode()).hexdigest()
        return block_hash
    
    def __str__(self):
        return "Block Hash:"+self.blockhash()+"\nPrevious Hash:" +self.prev_hash

    
class Hashchain():#ここに追加されていく
    def __init__(self):
        self.chain=["11111111"]

    def add(self,hash):
            self.chain.append(hash)

hashchain=Hashchain()
target=0x777777*2**(8*(0x1e-0x03))
for i in range(30):#全部で30ブロックできる
     block=Block("Block"+str(i+1),hashchain.chain[-1])
     block.index=block.index+i+1
     for n in range(4294967296):
          block.nonce=block.nonce+n
          if int(block.blockhash(),16)<target:# マイニング成功
               print(block)
               hashchain.add(block.blockhash())
               break
