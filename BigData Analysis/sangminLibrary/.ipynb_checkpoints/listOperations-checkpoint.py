#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 내용: 함수는 타입에 상관없이 list내 합계를 구함
# 파라미터: sampleList : list
# 목적: 문자열이든 숫자든 상관없이 합계 산출용

def listSum(sampleList):
    
    sampleListLen = len(sampleList)

    totalSum = 0
    
    for i in range(0, sampleListLen):
        eachItem = int(sampleList[i])
        totalSum = totalSum + eachItem

    return totalSum

#디버깅용
#sampleList = ["11", "22", "33"]
#listSum(sampleList)


# In[2]:

# 내용: 함수는 list의 최댓값, 최솟값을 제외한 평균을 산출함
# 파라미터: sampleList : list
# 목적: 최댓값, 최솟값을 제외한 평균 산출용

def avgFunction(list):
    #최댓값, 최솟값 구하기
    maxValue = max(list)
    minValue = min(list)
    
    #최댓값, 최솟값 수 구하기
    maxCnt = list.count(maxValue)
    minCnt = list.count(minValue)
    
    #최댓갑, 최솟값을 제외한 평균 구하기
    totalSum = sum(list) - (maxValue * maxCnt + minValue * minCnt)
    totalLen = len(list) - (maxCnt + minCnt)
    
    average = totalSum / totalLen
    
    return average




