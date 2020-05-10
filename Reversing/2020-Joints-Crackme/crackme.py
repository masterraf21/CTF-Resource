#!/usr/bin/env/ python3
from z3 import *
import os

s = Solver()

x = [ Int('x[%s]' % i) for i in range(25) ]
# print(x)

# Add constraints
s.add(x[20]-x[0]==24)
s.add(x[8]+x[5]==126)
s.add(x[14]*x[5]==3696)
s.add(x[21]-x[1]==33)
s.add(x[10]-x[0]==2)
s.add(x[17]-x[0]==19)
s.add(x[17]*x[1]==3848)
s.add(x[4]+x[6]==123)
s.add(x[13]*x[16]==4488)
s.add(x[1]*x[6]==2600)
s.add(x[13]*x[23]==3536)
s.add(x[8]-x[5]==14)
s.add(x[15]+x[5]==123)
s.add(x[20]-x[17]==5)
s.add(x[17]+x[16]==140)
s.add(x[16]+x[14]==132)
s.add(x[3]*x[6]==4250)
s.add(x[18]+x[14]==145)
s.add(2*x[13]==136)
s.add(x[17]-x[10]==17)
s.add(x[11]+x[8]==145)
s.add(x[9]+x[1]==135)
s.add(x[11]+x[24]==146)
s.add(x[3]-x[7]==11)
s.add(x[0]-x[2]==2)
s.add(x[11]-x[13]==7)
s.add(x[3]+x[4]==158)
s.add(x[3]-x[16]==19)
s.add(x[4]-x[14]==7)
s.add(x[12]*x[1]==4056)
s.add(x[20]+x[8]==149)
s.add(x[9]-x[4]==10)
s.add(x[9]-x[6]==33)
s.add(x[9]*x[13]==5644)
s.add(x[16]+x[5]==122)
s.add(x[16]-x[10]==9)
s.add(x[17]+x[24]==145)
s.add(x[20]-x[13]==11)
s.add(x[18]*x[11]==5925)
s.add(x[21]*x[23]==4420)
s.add(x[22]*x[7]==5698)
s.add(x[15]-x[19]==12)
s.add(x[16]-x[1]==14)
s.add(x[3]-x[13]==17)
s.add(x[12]*x[8]==5460)
s.add(x[21]*x[13]==5780)
s.add(x[7]*x[1]==3848)
s.add(x[22]+x[6]==127)
s.add(x[13]+x[5]==124)
s.add(x[24]+x[1]==123)

def to_serial(key):
    if(len(key)!=25):
        raise ValueError('Len not 25')
    key = key[:5]+'-'+key[5:]
    key = key[:11]+'-'+key[11:]
    key = key[:17]+'-'+key[17:]
    key = key[:23]+'-'+key[23:]
    return key

if (s.check()==sat):
    # print(s.check())
    m = s.model()
    key_list = [0 for i in range(25)]
    for i in range(25):
        key_list[i] = m[x[i]].as_long()
    # print(m)
    # print(key_list)
    key = ""
    for i in key_list:
        key += chr(i)
    print("Key: {}".format(to_serial(key)))
    
    
    
