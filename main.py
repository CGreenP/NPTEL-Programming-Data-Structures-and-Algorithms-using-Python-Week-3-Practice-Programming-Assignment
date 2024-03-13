def descending(l):
    lent= len(l)-1
    r= True
    if(len(l)==0):
        return (r)
    else:
        for i in range(lent,0,-1):
            if (l[i]>l[i-1]):
                r= False
                break
    return (r)

def valley(l):
    if(len(l)==0):
        return(True)
    if (len(l) < 4):
        return (False)
    if(l[0]<l[1]):
        return(False)
    for i in range(0,len(l)-1):
        if(l[i]<l[i+1]):
            pos=i
            break
        if(l[i]==l[i+1]):
            return(False) 
    else:
        return(False)
    for i in range(pos,len(l)-1):
        if(l[i]>=l[i+1]):
            return(False)
    return(True)
  
def transpose(m):
    result = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    return (result)
import ast

def parse(inp):
  inp = ast.literal_eval(inp)
  return (inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "descending":
  arg = parse(farg)
  print(descending(arg))

if fname == "valley":
  arg = parse(farg)
  print(valley(arg))

if fname == "transpose":
  arg = parse(farg)
  print(transpose(arg))
  
