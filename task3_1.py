import pandas as pd
# 3_1
df = pd.read_excel('test1.xlsx')         # 엑셀파일 불러오기
print (df)


# 3_2
police = {'서대문서': '서대문구', '수서서': '강남구', '강서서': '강서구', '서초서': '서초구',
'서부서': '은평구', '중부서': '중구', '종로서': '종로구', '남대문서': '중구',
'혜화서': '종로구', '용산서': '용산구', '성북서': '성북구', '동대문서': '동대문구',
'마포서': '마포구', '영등포서': '영등포구', '성동서': '성동구', '동작서': '동작구',
'광진서': '광진구', '강북서': '강북구', '금천서': '금천구', '중랑서': '중랑구',
'강남서': '강남구', '관악서': '관악구', '강동서': '강동구', '종암서': '성북구', 
'구로서': '구로구', '양천서': '양천구', '송파서': '송파구', '노원서': '노원구', 
'방배서': '서초구', '은평서': '은평구', '도봉서': '도봉구'}

df['구별'] = df['관서명'].map(police).fillna('구 없음')         # 관서명을 매핑해서 구별컬럼 생성, 결측치에 '구 없음'을 넣어줌

print(df)

# 3_3
pivot = pd.pivot_table(df, index='구별', aggfunc='sum')           # pivot_table 을 통해 구별을 기준으로 합계를 내줌으로 데이터 재구조화 

pivot.drop(columns=['관서명'],inplace=True)                      # 필요없는 컬럼은 삭제 inplace로 바로 원본에서 삭제

print(pivot)


# 3_4
pivot.drop(['구 없음'], inplace=True)                         # 결측치구간 삭제

print(pivot)



# 3_5
pivot['강간검거율'] = (pivot['강간(검거)']/ pivot['강간(발생)'])*100
pivot['강도검거율'] = (pivot['강도(검거)']/ pivot['강도(발생)'])*100
pivot['살인검거율'] = (pivot['살인(검거)']/ pivot['살인(발생)'])*100
pivot['절도검거율'] = (pivot['절도(검거)']/ pivot['절도(발생)'])*100
pivot['폭력검거율'] = (pivot['폭력(검거)']/ pivot['폭력(발생)'])*100
pivot['검거율'] =  (pivot['소계(검거)']/ pivot['소계(발생)'])*100           # 각 검거율의 컬럼을 생성해 검거와 발생의 데이터를 통해 검거율을 측정. 

print(pivot)



# 3_6
del pivot['강간(검거)']
del pivot['강도(검거)']
del pivot['살인(검거)']
del pivot['절도(검거)']
del pivot['폭력(검거)']
del pivot['소계(검거)']
del pivot['소계(발생)']

print(pivot)                        # 필요없게된 검거컬럼들 del문으로 바로 삭제




# 3_7
df1 = pivot.rename(columns={'강간(발생)':'강간', '강도(발생)':'강도', '살인(발생)':'살인', '절도(발생)':'절도', '폭력(발생)':'폭력'})      # rename으로 컬럼이름들 변경

print(df1)                     



# 도전과제 3_1
df2 = pd.read_csv('https://file.notion.so/f/f/83c75a39-3aba-4ba4-a792-7aefe4b07895/6202f3a7-1bcf-4e66-913f-c6030d3eccd7/pop_kor.csv?table=block&id=1182dc3e-f514-813b-91ab-e52d7cf7929b&spaceId=83c75a39-3aba-4ba4-a792-7aefe4b07895&expirationTimestamp=1729137600000&signature=Yu8Gv1pJq4KPG2kGjcuwJJPpVft8_ypYe1yXSyKzn1I&downloadName=pop_kor.csv',index_col='구별')
df2 = pd.DataFrame(df2)   # url을 통해 파일을 불러옴

print(df2)

# 도전과제 3_2
merge_df = pd.merge(df1,df2, on = '구별', how ='outer')     # merge로 두 데이터프레임을 구별을 기준으로 전부다(outer)합쳐줌

print(merge_df)


# 도전과제 3_3
df = merge_df.sort_values(by=['인구수'],ascending=True)       # sort_values 와 ascending=True를 이용하여 인구수별로 오름차순 정리
