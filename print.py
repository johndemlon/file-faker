import time
import base64

def encode(key, string):
    encoded_chars = []
    for i in xrange(len(string)):
        key_c = key[i % len(key)]
        encoded_c = chr(ord(string[i]) + ord(key_c) % 256)
        encoded_chars.append(encoded_c)
    encoded_string = "".join(encoded_chars)
    return base64.urlsafe_b64encode(encoded_string)
#print(encode("da","hello"))

f = open("a.txt", "r+")
#f2 = open("crpted.txt", "r")
lst=[]
print("enter key : ")
ky = raw_input()
print("program started")
for x in f:
	#time.sleep(0.1)
	ln = f.readline()
	print(x)
	ln.strip("\n")
	#print(str(encode(str(ky),str(ln))))
	lst.append(str(encode(str(ky),str(x))))
	f.write("")


f.close()
f = open("a.txt", "r+")
#f.seek(0)
for y in f:
	for ele in lst:
		#print(ele)
		f.write(ele)
		
		
	#if "asdf1243" in x :
	#	print("true")
	#	break
print("done")

f.close()
#f2.close()