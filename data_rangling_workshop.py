"""
## 환경설정 (pycharm)
"""

# Pycharm
# PycharmProject에 project 생성
# venv 설정

"""
## 자료형 (str, int, float, boolean, set, list, tuple, dictionary)
"""

############ [str 자료형] ############


str_var = "홍길동_87_Vancomycin"
print(str_var)

# 슬라이싱(slicing)

print(str_var[2:7])

# split 메소드

print(str_var.split("_"))

# strip 메소드

str_var = "    홍길동_87_Vancomycin  "
print(str_var.strip())

# replace 메소드

print(str_var.replace("Vancomycin","Amikacin"))

str_var = str_var.replace("Vancomycin","Amikacin")  # 바로 저장되는게 아니고 변수에 할당해야 변경됨
print(str_var)

# upper case / lower case

upper_str = str_var.upper()
print(upper_str)

lower_str = str_var.lower()
print(lower_str)


# 연산 (+)

str_var1 = '동길홍_90_Amikacin'
str_var2 = '_peak(35)trough(2.5)'
sum_str_var = str_var1 + str_var2
print(sum_str_var)

# formatting

drug = 'Digoxin'
str_var = f'길동이_44_{drug}'
print(str_var)

age = 55
str_var = f'길동이_{age}_{drug}'
print(str_var)

# str 자료로 변환

list_str = str(['1', '2', '3'])
print(list_str)


############ [float, int 자료형] ############

int_var = 3
float_var = 5.01

## 연산

new_num = int_var + float_var           # 더하기
print(new_num)

new_num = int_var - float_var           # 빼기
print(new_num)

new_num = int_var * float_var           # 곱하기
print(new_num)

new_num = int_var / float_var           # 나누기
print(new_num)

new_num = float_var // int_var          # 나눈몫
print(new_num)

new_num = float_var % int_var           # 나눈나머지
print(new_num)

new_num = int_var**float_var            # 지수
print(new_num)

# int, float 변환

int_to_float = float(int_var)
print(int_to_float)

float_to_int = int(float_var)
print(float_to_int)

# 올림, 내림, 반올림

fvar1 = 5.6373
fvar2 = 4455.2388
fvar3 = 123.55

# 반올림
rfvar2 = round(fvar2,3)
print(rfvar2)

rfvar2 = round(fvar2,-2)
print(rfvar2)

# 올림, 내림

import math
new_fvar1 = math.ceil(fvar1)
print(new_fvar1)

new_fvar3 = math.floor(fvar3)
print(new_fvar3)

print(math.sqrt(4))        # 제곱근
print(math.exp(4))         # 밑이 e인 지수
print(math.log(4))         # 밑이 e인 로그

############ [Boolean 자료형] ############

bool_var = True
bool_var2 = False

print(bool_var)
print(bool_var2)

print(new_fvar1 == new_fvar3)    # 같다
print(new_fvar1 != new_fvar3)    # 같지 않다
print(new_fvar1 > new_fvar3)     # 왼쪽이 크다
print(new_fvar1 >= new_fvar1)    # 왼쪽이 크거나 같다
print(new_fvar1 < new_fvar1)     # 오른쪽이 크다
print(new_fvar1 <= new_fvar1)    # 오른쪽이 크거나 같다

date1 = '2025-01-27T18:20'
date2 = '2025-01-24T13:20'
date3 = '2025-01-24T13:22'

print(date1 < date2)
print(date1 > date3)

print(f"날짜 {date1}은 {date2}보다 크다: {date1 > date3}")

############ [set 자료형] ############ (원소 중복 불허 / 순서가 없어 슬라이싱 불가)

set1 = {'Amikacin', 'Vancomycin', 'Digoxin', 'Valproate'}
set2 = {'Gentamicin', 'Digosin', 'Prednisone', 'Vancomycin'}
set3 = {1, 2, 4.0, 'Vancomycin'}

# add : 원소 추가

set1.add('Phenytoin')      # set1이 바로 바뀜 (따로 값이 return 되는게 아님)
print(f"원소 추가된 set1: ",set1)

# union: 두 집합 합치기

set4 = set1.union(set2)
print(f"set1과 set2의 합집합: ",set4)

set4 = set1|set2
print(f"set1과 set2의 합집합: ",set4)

# intersection: 교집합 구하기

set4 = set1.intersection(set2)
print(f"set1과 set2의 교집합: ",set4)

set4 = set1&set2
print(f"set1과 set2의 교집합: ",set4)

# -: 차집합 구하기

set4 = set1-set2
print(f"set1과 set2의 차집합: ",set4)

############ [list 자료형] ############ (원소 중복 허용)

list1 = ['Amikacin', 'Vancomycin', 'Digoxin', 'Valproate']
list2 = ['Gentamicin', 'Digosin', 'Prednisone', 'Vancomycin']
list3 = [1, 2, 4.0, 'Vancomycin', 'Vancomycin']

# 슬라이싱

print(list1[0])
print(list1[-2])
print(list1[-2:])
print(list2[1:3])
print(list3[0:-2])

# 원소 바꾸기

list3[1] = 'Sitagliptin'
list3[2] = 'Lobeglitazone'
print(list3)

# append: 원소 추가

list1.append('Phenytoin')      # list1이 바로 바뀜 (따로 값이 return 되는게 아님)
print(f"원소 추가된 list1: ",list1)

# union: 두 리스트 합치기

list4 = list1 + list2
print(f"list1과 list2의 합: ",list4)

# sort: 순서대로 정렬

list2.sort()     # list2가 바로 바뀜 (따로 값이 return 되는게 아님)
print(f"set1과 set2의 교집합: ",list2)

# len: 길이 구하기

print(len(list1))

############ [tuple 자료형] ############ (원소 중복 허용 / 한번 정의되면 수정불가 - 원소 추가/삭제 등)

drug_tup = ('vancomycin', 'amikacin', 'gentamicin')
drug_list = list(drug_tup)

print(drug_tup)

# 슬라이싱

print(drug_tup[1:3])

# 변환불가 (에러남)

drug_tup[0] = 'digoxin'


############ [dictionary 자료형] ############ (원소 중복 불허 / key 와 value 값)

empty_dict = dict()

print(empty_dict)

target_str = 'Target: AUC 400 ~ 600 / Target: peak > 25 trough < 5 / Target: peak and trough 50 ~ 100'
target_list = target_str.split(' / ')
drug_dict = {'Vancomycin': target_list[0], 'Amikacin':target_list[1], 'Valproate':target_list[2]}     # dictionary를 구성합니다

print(drug_dict)
print(drug_dict['Amikacin'])

# key 값만 조회

drug_dict.keys()

# value 값만 조회

drug_dict.values()

# key, value 추가하기

drug_dict['Digoxin'] = 'Target: peak and trough 0.5~1.0'
print(drug_dict)

# update: dictionary에 다른 dictionary를 업데이트하기

dict1 = {'Vancomycin': target_list[0], 'Amikacin':target_list[1]}
dict2 = {'Valproate':target_list[2], 'Digoxin': 'Target: peak and trough 0.5~1.0'}
dict1.update(dict2)
print(dict1)

# dict 를 원소가 tuple로 구성된 list로 변환
dict_to_tup_list = list(drug_dict.items())
print(dict_to_tup_list)

"""
## 반복문 (for, while)
"""

# for문

for c in list2:
    print("Drugname: "+c)

# for문에서 변수 연속적으로 변환하기

drug_str = ''
for s in list2:
    drug_str = drug_str + ' ' + s
    drug_str+= '_ <-'
print(drug_str)

# for문에서 숫자로 된 iteration

drug_str = ''
for i in range(len(list2)):
    drug_str = drug_str + ' ' + list2[i]
    drug_str += '_ <-'
print(drug_str)

# for문에서 enumerate를 이용하여 index까지 같이 얻기

drug_str = ''
for i, v in enumerate(list2):
    drug_str = drug_str + f'({i}) ' + v
    drug_str += '_ <- '
print(drug_str)


"""
## 조건문 (if)
"""

## if 만

if list2[3]=='Vancomycin':
    print('Target: AUC 400 ~ 600')

## if, else

if list2[0]!='Gentamicin':
    print('Target: Peak 5~10 and Trough < 2')
else:
    print('Gentamicin 타겟이 아닙니다.')

## if, elif, else

if list2[0]!='Gentamicin':
    print('Target: Peak 5~10 and Trough < 2')
elif list2[1]=='Digosin':
    print('Digosin 이니 확인바랍니다.')
else:
    print('아무 조건에도 해당되지 않습니다.')

"""
## for문, if문 합작
"""

for i, drug in enumerate(list2):
    if i==0:
        print(f"({i}) {drug}")

    if drug == 'Digosin':
        print(f"{drug}이 나왔습니다. for문을 지속합니다")
        continue

    if drug=='Prednisone':
        print(f"{drug}이 나왔습니다. for문을 종료합니다")
        break

    print('다음 넘어가자')

"""
## Small projects
"""

import pandas as pd

pt_list = ['홍길동','동길홍','길동이','길냥이','강아지','고양이','토끼']
drug_list = [('Vancomycin','25/01/03'),('Vancomycin','25/01/05'),('Amikacin','25/03/09'),('Amikacin','25/03/09'),('Amikacin','25/05/09'),('Gentamicin','25/07/09'),('Gentamicin','25/07/09')]

final_str = ''
for i in range(len(pt_list)):
    frag_str = f"{pt_list[i]}_{drug_list[i][0]}_{drug_list[i][1]}"
    final_str += (frag_str + ' <- ')
final_str = final_str[:-4]
print(final_str)


