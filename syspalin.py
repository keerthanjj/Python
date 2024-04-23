str=input("Enter the String! \n")
def sym(str):
    str=str.lower()
    l=len(str)
    start1=0
    mid=l//2
    first=str[start1:mid]
    sec=str[mid:len(str)]
    if first==sec:
        print("Its Symmentric one")
    else:
        print("Not a symmentric one")

def pal(str):
    str=str.lower()
    if str==str[::-1]:
        print("But Its a palindrome")
    else:
        print("But Not a palindrome")

        
        


sym(str)
pal(str)