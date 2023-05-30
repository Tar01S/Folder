# ----------------------------------book(173)---------------------------------------------------
# def summ():
#     num=input("Enter text or '': ")
#     if num =='':
#         return 0
#     else:
#         return float(num)+summ()
# print(summ())   
# ----------------------------------book(174)---------------------------------------------------
# def evklid(a,b):
#     if b==0:
#         return a
#     else:
#         c= a%b
#         return evklid(b,c)
# a= int(input("Enter number: "))
# b= int(input("Enter number: "))
# print(evklid(a,b))
# ----------------------------------book(175)---------------------------------------------------
# def erkuakan(n):
#     if n ==1:
#         return 1
#     else:
#         return str(erkuakan(n//2))+str(n%2)
# print(erkuakan(int(input('Enter number: '))))  
# ----------------------------------book(176)---------------------------------------------------
# def nato(word):
#     aybuben = {
#         'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo', 'F': 'Foxtrot',
#         'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliet', 'K': 'Kilo', 'L': 'Lima',
#         'M': 'Mike', 'N': 'November', 'O': 'Oscar', 'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo',
#         'S': 'Sierra', 'T': 'Tango', 'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray',
#         'Y': 'Yankee', 'Z': 'Zulu'
#     }
#     if len(word)==0:
#         return ''
#     araj_tar=word[0].upper()
#     if araj_tar.isalpha():
#         stac_bar=aybuben[araj_tar]
#     else:
#         stac_bar=''
#     bary=word[1:]
#     return stac_bar + ' ' +nato(bary)
# print(nato(input("Enter word: ")))        
# ----------------------------------book(177)---------------------------------------------------
# def  hrom(hrom_tver):
#     hrom_to_hazar = {
#             'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1
#     }
#     if hrom_tver=='':
#         return 0
#     if len(hrom_tver)==1 or hrom_to_hazar[hrom_tver[0]]>=hrom_to_hazar[hrom_tver[1]]:
#         return hrom_to_hazar[hrom_tver[0]]+hrom(hrom_tver[1:])
#     else:
#         hrom_to_hazar[hrom_tver[1]]-hrom_to_hazar[hrom_tver[0]]+hrom(hrom_tver[2:])
# print(hrom(input("Enter hromeakan tivy: ")))         
# ----------------------------------book(178)---------------------------------------------------
# def palindrom(word):
#     if len(word)<=1:
#         return True
#     if word[0]==word[-1]:
#         return palindrom(word[1:-2])
#     else:
#         return False
# print(palindrom(input("Enter word:")))  
# ----------------------------------book(180)---------------------------------------------------
# def radikal(s,t):
#     if len(s)==0:
#         return len(t)
#     elif len(t)==0:
#         return len(s)
#     else:
#         cost=0
#         if s[-1] != t[-1]:
#             cost=1
#         d1 = radikal(s[:-1],t) + 1 
#         d2 = radikal(t[:-1],s) + 1
#         d3 = radikal(s[:-1],t[:-1]) + cost
#         return min(d1,d2,d3)
# s=input("Enter toxy: ")
# t=input("Enter toxy: ")    
# print(radikal(s,t))
# ----------------------------------book(184)---------------------------------------------------
# def listss(data):
#     if data ==[]:
#         return []
#     if type(data[0])==list:
#         return listss(data[0])+listss(data[1:])
#     else:
#         return [data[0]]+listss(data[1:])
# print(listss([1, [2, [3,[11,15,17]]], [4, [5, [6, 7]]], [[[8],
# 9], [10]]])) 
# ----------------------------------book(185)---------------------------------------------------
'''Es depqum  stanum em senc xndri outputy chem stacel['AAAAAAAAAAAA', 'BBBB', 'AAAAAA', 'B'] '''
# def shifrav(mylist):
#     if len(mylist)==0:
#         return []
#     else:
#         return [mylist[1]*mylist[0]]+shifrav(mylist[2:])
# print(shifrav( ["A", 12, "B", 4, "A", 6, "B", 1]))  
#       
