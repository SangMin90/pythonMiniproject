#!/usr/bin/env python
# coding: utf-8

# In[ ]:

# 내용: 
# 파라미터:
# 목적: 

def roundFunction(inValue):
    # step1 : 입력값을 1000으로 곱한다
    step1 = inValue * 1000
    
    # step2 : step1 결과를 int 캐스팅
    step2 = int(step1)
    
    # stpe3 : 1000으로 나눈다
    outValue = step2 / 1000
    
    return outValue

