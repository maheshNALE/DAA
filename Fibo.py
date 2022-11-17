#%%
prev=0
next=1
sum=1
num=10
for i in range(1,11):
    pre=next
    next=sum
    sum=pre+next
    print(sum)
print("end of program")
#%%