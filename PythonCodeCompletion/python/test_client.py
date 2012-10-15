
def f(x):
    return x**2
 # client-side test program for python_completion_server.py

import xmlrpclib
import os
import subprocess
import sys
import struct
#xml=xmlrpclib.dumps(('os',),'complete_phrase')
#print xml
#p=subprocess.Popen(['python','python_completion_server.py'],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
#p.communicate(struct.pack('@I',len(xml)))
#p.communicate(xml)
#print sys.stdin.read()

#import sys
#sys.exit()

s = xmlrpclib.ServerProxy('http://localhost:8001')
# Print list of available methods
print 'Methods'
for m in s.system.listMethods():
    print m
print

code ='''
class A:
    def a(x):
        pass
    def b(x):
        pass
def f(x):
    'f(x)\\nreturns a function'
    return x**2
x=1
y=f(x)
a=A()
f()
'''


f=os.getcwd()+'/test_client.py'

print f
print s.complete_phrase(f,code,len(code)-3)
print s.complete_tip(f,code,len(code)-3)
code = code + '\na.'
print s.complete_phrase(f,code,len(code))
code = 'code = 1\nco'
print len(code)
print s.complete_phrase(f,code,len(code))
code = 'code = 1\r\nco'
print len(code)
#code = code.replace('\r\n',' \n')
print s.complete_phrase(f,code,len(code))
