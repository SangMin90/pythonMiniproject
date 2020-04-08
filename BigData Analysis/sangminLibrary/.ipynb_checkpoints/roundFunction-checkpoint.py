#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def roundFunction(inValue):
    # step1 : 입력값을 1000으로 곱한다
    step1 = inValue * 1000
    
    # step2 : step1 결과를 int 캐스팅
    step2 = int(step1)
    
    # stpe3 : 1000으로 나눈다
    outValue = step2 / 1000
    
    return outValue

# 내용: 함수는 타입에 상관없이 list내 합계를 구함
# 파라미터: sampleList : list
# 목적: 문자열이든 숫자든 상관없이 합계 산출용

def listSum(sampleList):

#디버깅용    sampleList = ["11", "22", "33"]

    sampleListLen = len(sampleList)

    totalSum = ""
    for i in range(0, sampleListLen):
        eachItem = sampleList[i]
        totalSum = totalSum + eachItem

    return totalSum
