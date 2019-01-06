# Modified version of https://github.com/yashk2810/Encryption-Tool
import os
import sys
from stat import *
from Crypto.Cipher import AES
import os
from Crypto.Protocol.KDF import PBKDF2
import base64

def traversetree(top, callback):
    dirs = os.listdir(top)
    for files in dirs:
        pathname = os.path.join(top, files)
        # print pathname
        mode = os.stat(pathname)[ST_MODE]

        if S_ISDIR(mode):
            traversetree(pathname, callback)

        elif S_ISREG(mode):
            key = 'WU9TT1lHUjAwVDE5NjA='.decode('base64') + '00'

            # Decryption part
            if sys.argv[1] == '-d':
                print "Decrypting"
                fr=open(pathname,'r')
                chunk=fr.read(1024*16)
                key='secret message a'
                iv = chunk[:16]
                mode = AES.MODE_CBC
                decryptor = AES.new(key, mode, IV=iv)
                fw1=open(pathname,'w')
                original=decryptor.decrypt(chunk[16:])
                fw1.write(original.replace('*',''))

            callback(pathname)   
        else:
            print "Skipping %s" % (pathname)


def visitfile(file):
    print file

traversetree(sys.argv[2], visitfile)
