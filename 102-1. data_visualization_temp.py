#!/usr/bin/env python
# coding: utf-8

# 책 따라하기

import csv
import matplotlib.pyplot as plt

f = open('./data/seoul_book.csv')
data = csv.reader(f)
next(data)
high = []
low = []

for row in data:
    if row[-1] != '' and row[-2] != '':
        date = row[0].split('-')
        if 1983 <= int(date[0]):
            if date[1] == '02' and date[2] == '14': # 2월 14일의 최고/최저 기온
                high.append(float(row[-1]))
                low.append(float(row[-2]))


plt.rc('font', family = 'Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False
plt.title('내 생일의 기온 변화 그래프')

plt.plot(high, 'hotpink', label='high')
plt.plot(low, 'skyblue', label='low')
plt.legend()
plt.show()


# 내 생일달의 기온변화 그래프로 나타내기

import csv
import matplotlib.pyplot as plt

f = open('./data/seoul.csv', encoding='utf-8')
data = csv.reader(f)
next(data)
high = []
low = []
# data[2]: 연월, data[5]: 최고기온, data[8]: 최저기온

for row in data:
    if row[5] != '' and row[8] != '':
        date = row[2].split('-')
        if date[1] == '09':
            high.append(float(row[5]))
            low.append(float(row[8]))
        
# print(high)
# print(low)


plt.rc('font', family = 'Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False
plt.title('내 생일달의 기온 변화 그래프')

plt.plot(high, 'r', label='high')
plt.plot(low, 'b', label='low')
plt.legend()
plt.show()


# 내 생일 기온변화 그래프로 나타내기

import csv
import matplotlib.pyplot as plt

f = open('./data/seoul_daily.csv')
data = csv.reader(f)
next(data)
high = []
low = []
# data[0]: 날짜, data[4]: 최고기온, data[3]: 최저기온

for row in data:
    if row[-1] != '' and row[-2] != '':    # csv 자료 마지막 줄에 빈 줄이 있으면 list index out of range 라는 메시지가 뜬다.
        date = row[0].split('-')            # 한줄까지만 괜찮다.
        if date[1] == '09' and date[2] == '10':
            high.append(float(row[-1]))
            low.append(float(row[-2]))
        
# print(high)
# print(low)


plt.rc('font', family = 'Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False
plt.title('내 생일 기온 변화 그래프')

plt.plot(high, 'r', label='high')
plt.plot(low, 'b', label='low')
plt.legend()
plt.show()


# 주피터 노트북으로 작성 후 py 파일로 변환
# matplotlib 학습

