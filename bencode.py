from collections import OrderedDict


class Decoder:

    TOKEN_INT='i'
    TOKEN_LIST='l'
    TOKEN_DICT='d'
    TOKEN_END='e'
    TOKEN_STR=':'

    def __init__(self,data:bytes):
        if not isinstance(data,bytes):
            raise TypeError('You stupid ni')
        self.data=data
        self.index=0
        
    def decode(self):
        
        c = self.data[self.index]
            
        if c == ord(self.TOKEN_DICT):
            return self._decode_dict()
        elif c == ord(self.TOKEN_LIST):
            return self._decode_list()
        elif c == ord(self.TOKEN_INT):
            return self._decode_int()
        elif 48<=c<=57 :
            return self._decode_string()
    
    def _decode_dict(self):
        dct=OrderedDict() 
        self.index+=1
        while self.data[self.index]!=ord(self.TOKEN_END):
            key=self.decode()
            value=self.decode()
            dct[key]=value
        self.index+=1
        return dct

    def _decode_list(self):
        lst=[]
        self.index +=1
        while self.data[self.index]!=ord(self.TOKEN_END):
            lst.append(self.decode())
        self.index +=1
        return lst

    def _decode_int(self):
        
        save=self.index
        while self.data[self.index] != ord(self.TOKEN_END):
            self.index=self.index + 1
        self.index=self.index+1
        return int(self.data[save + 1 : self.index-1].decode())

    def _decode_string(self):

        save=self.index
        while self.data[self.index]!=ord(self.TOKEN_STR):

            self.index=self.index + 1

        str_len=int(self.data[save:self.index].decode())
        self.index=self.index + 1
        self.index=self.index+str_len
        return self.data[self.index-str_len:self.index] 
class Encoder:

    TOKEN_INT='i'
    TOKEN_LIST='l'
    TOKEN_DICT='d'
    TOKEN_END='e'
    TOKEN_STR=':'

    def __init__(self,data):
        self.data=data
        
    def encode(self):
        
            
        if isinstance(self.data,dict):
            return self._encode_dict()
        elif isinstance(self.data,list):
            return self._encode_list()
        elif isinstance(self.data,int):
            return self._encode_int()
        elif isinstance(self.data,str):
            return self._encode_string()
        elif isinstance(self.data,bytes):
            return self._encode_bytes()
        else :raise(TypeError('You stupid ni'))
    
    def _encode_dict(self):
        result=bytearray(b'd')
        for e in self.data:
            result+=Encoder(e).encode()
            result+=Encoder(self.data[e]).encode()
        result+=b'e'
        return bytes(result)

    def _encode_list(self):
        result=bytearray(b'l')
        for e in self.data:
            result+=Encoder(e).encode()
        result+=b'e'
        return bytes(result)

    def _encode_int(self):
        return str.encode(self.TOKEN_INT+str(self.data)+self.TOKEN_END)

    def _encode_string(self):
        return str(len(self.data)).encode()+self.TOKEN_STR.encode()+self.data.encode()
    def _encode_bytes(self):
        return (str(len(self.data))+self.TOKEN_STR+str(self.data)).encode()

