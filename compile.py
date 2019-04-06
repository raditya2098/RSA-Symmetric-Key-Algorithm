#import AESencryption
#import AESdecryption
import SHA_256
import DSAsignature
import DSAverification
import RSA_encryption
import RSA_decryption


n=input("Enter your choice:\n1.RSA\n2.SHA256\n3.AES\n4.DSA")
if(n==1):
    RSA_encryption.RSAencryption()
    RSA_decryption.RSAdecryption()
