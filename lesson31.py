# --------------------------------------class (1)----------------------------------------------------
# class dar:

#     def __init__(self,year) -> None:
#         self.year=year

#     def tari_dar(self):
#         verj_dar=self.year//100
#         if self.year%100!=0:
#             verj_dar+=1
#         return verj_dar
    
# year=int(input("Enter the year: "))
# x=dar(year)
# print(x.tari_dar())                    
# --------------------------------------class (2)----------------------------------------------------
# class palindrom:

#     def __init__(self,word) -> None:
#         self.word=word.lower()


#     def func(self):
#         if self.word==self.word[::-1]:
#             return True
#         else:
#             return False
        
# word=input("Enter word: ")
# x=palindrom(word)
# print(x.func())
# --------------------------------------class (3)----------------------------------------------------
# class Largest:

#     def __init__(self,mylist) -> None:
#         self.mylist=mylist

#     def larg_arj(self):
#         max_arj=0

#         for i in range(0,len(self.mylist)-1):
#             if self.mylist[i] * self.mylist[i+1] >max_arj:
#                 max_arj = self.mylist[i] * self.mylist[i+1]    
#         return max_arj

# x=Largest([3, 6, -2, -5, 7, 3])
# print(x.larg_arj())        
# --------------------------------------class (4)----------------------------------------------------
# class erk:


#     def __init__(self,mylist) -> None:
#         self.mylist=mylist


#     def max_len(self):
#         self.mylist.sort(key=len,reverse=True)
#         max_arj=len(self.mylist[0])
#         return [i for i in self.mylist if len(i)==max_arj]

       
# obj=erk(["aba", "aa", "ad", "vcd", "aba"]) 
# print(obj.max_len())
# --------------------------------------class (5)----------------------------------------------------
# class  Lucky:

#     def __init__(self,number) -> None:
#         self.number=number

#     def func(self):
#         tox=str(self.number)
#         tox_kes=len(tox)//2
#         first_kes=sum([int(i) for i in tox[:tox_kes]]) 
#         second_kes=sum([int(i)for i in tox[tox_kes:]])
#         return first_kes == second_kes
    
# number= int(input("Enter number: "))
# x=Lucky(number)
# print(x.func())  
# --------------------------------------class (6)----------------------------------------------------
# class sort:
#     def __init__(self,mylist) -> None:
#         self.mylist=mylist

#     def func(self):
#         sort_list=sorted([i for i in self.mylist if i != -1])
#         for j in range(len(self.mylist)): 
#             if self.mylist[j] ==-1:
#                 sort_list.insert(j,-1) 
#         return sort_list           
              
               

# x=sort([-1, 150, 190, 170, -1, -1, 160, 180])
# print(x.func())
# --------------------------------------class (7)----------------------------------------------------
# class weight:
#     def __init__(self,mylist) -> None:
#         self.mylist=mylist
#     def func(self):
#         summ1=0
#         summ2=0
#         # new_list=[]
#         for i in range(len(self.mylist)):
#             if i%2==0:
#                 summ1+=self.mylist[i]
#             else:
#                 summ2+=self.mylist[i]   
#         return [summ1,summ2]
# x=weight([50, 60, 60, 45, 70])
# print(x.func())                 