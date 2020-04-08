#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# In[1]:


# 내용: 함수는 input 타입에 상관없이 현재 연주차와 x주를 입력받아 x주 전 연주차를 구함
# 파라미터: nowYearWeek: string or int minusValue: string or int
# 목적: 현재 연주차와 x주 정보를 입력받아 x주 전 연주차를 "201015" 형태로 출력

from isoweek import Week

        
# 함수 변수 설정 nowYearWeek, minusWeek
def yearWeekFunction(nowYearWeek, minusValue):
    # 현재 연주차 정보를 연도와 주차로 나누고 정수로 형변환한다.
    nowYearWeek = str(nowYearWeek)
    currYear = int(nowYearWeek[:4])
    currWeek = int(nowYearWeek[4:])
    # 현재 주차에서 x주를 뺀 값을 지역변수로 저장한다
    beforeWeek = currWeek - int(minusValue)
    # x주 전 연도를 지역변수로 저장한다.
    beforeYear = currYear
    
    #x주 전 주차가 양수가 될 때까지 다음 과정을 반복한다.
    while beforeWeek <= 0:
        #전년도 정보와 x주 전 주차를 각각 문자열로 형변환하여 저장한다.
        beforeWeek = Week.last_week_of_year(beforeYear).week + beforeWeek
        beforeYear = beforeYear - 1
        
    # return 값을 반환할 지역변수 설정
    beforeYearWeek = ""
    # 주차가 한자리 수일 경우 0을 붙일 변수 설정
    weekOneDigit = "0"
    beforeWeekLen = len(str(beforeWeek))
    # 주차가 한자리 수인가?
    if beforeWeekLen == 1:
        # 그렇다면 주차에 0을 붙이고 합친다
        beforeWeek = weekOneDigit + str(beforeWeek)
        beforeYearWeek = str(beforeYear) + str(beforeWeek)
    # 아니라면 그대로 합친다
    else:
        beforeYearWeek = str(beforeYear) + str(beforeWeek)
    
    return beforeYearWeek

## 디버깅용
# targetWeek = '201503'
# beforeXWeek = "200"
# yearWeekFunction(targetWeek, beforeXWeek)

