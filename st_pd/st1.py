import pandas as pd

# 리스트로부터 series 생성
s = pd.Series([1,2,3])
print (s)

#index를 직접 지정
p = pd.Series([1,2,3],index=['a','b','c'])
print(p)
a=p.loc['a']
print(a)