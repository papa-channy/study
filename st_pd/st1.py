import pandas as pd

# # 리스트로부터 series 생성
# s = pd.Series([1,2,3])
# print (s)

# #index를 직접 지정
# p = pd.Series([1,2,3],index=['a','b','c'])
# print(p)
# a=p.loc['a']
# print(a)
성적={'정배': [20,30,40],'예은' : [80,90,95],'찬':[100,100,100]}
df = pd.DataFrame(성적,['국어','수학','영어'])
print (df,type(성적))
