str="we are strong together"
def rev(str):
    str=str.split(" ")
    new=" "
    for word in str:
        new=word+" "+new
    return new

print(rev(str))