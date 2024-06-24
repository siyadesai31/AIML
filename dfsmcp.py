def creatpath(v):
    dpath=[]
    cnt=0
    while v!=(3,3,0):
        for j in path:
            if v in path[j] and j not in p:
                dpath.append(j)
                v=j
                break
    p.append(v)
    return dpath[::-1]
def Rule(v):
    (x,y,z)=v
    newstate=[]
    if z==0 :
        if((x>=(y-2) or x==0)and (((3-x)>=(3-y+2)) or 3-x==0) ):
            newstate.append((x,y-2,1))
        if((x-2)>=y or (x-2)==0):
            newstate.append((x-2,y,1))
        if((x-1)>=(y-1)and (((3-x+1)>=(3-y+1)) or 3-x+1==0)):
            newstate.append((x-1,y-1,1))
        if(((x-1)>=y or (x-1)==0)and (((3-x+1)>=(3-y)) or 3-x+1==0)):
            newstate.append((x-1,y,1))
        if(x>=(y-1)and (((3-x)>=(3-y+1)) or 3-x==0) ):
            newstate.append((x,y-1,1))
    if z== 1:
        if(x>=(y+2)and (((3-x)>=(3-y-2)) or 3-x==0)  ):
            newstate.append((x,y+2,0))
        if((x+2)>=y and (((3-x-2)>=(3-y)) or 3-x-2==0) ):
            newstate.append((x+2,y,0))
        if((x+1)>=(y+1)and (((3-x-1)>=(3-y-1)) or 3-x-1==0) ):
            newstate.append((x+1,y+1,0))
        if((x+1)>=y and (((3-x-1)>=(3-y)) or 3-x-1==0)):
            newstate.append((x+1,y,0))
        if((x>=(y+1) or x==0 )and (((3-x)>=(3-y-1)) or 3-x==0 )):
            newstate.append((x,y+1,0))
    return newstate
start=(3,3,0)
goal=(0,0,1)
visited=[]
p=[]
stack=[]
stack.append(start)
path={}
print("State produced")
while len(stack)!=0 :
    v=stack.pop()
    path[v]=[]
    newstate=Rule(v)
    path[v].extend(newstate)
    visited.append(v)
    print(v,end=" , ")
    if v==goal:
        print("")
        print("Solution:")
        print("The path is")
        path1=creatpath(v)
        path1.append(v)
        print(path1)
        ct=1
        break
        
    for j in newstate:
           (x,y,z)=j
           if j  not in  visited and x<4 and y<4 and x>-1 and y>-1 :
                stack.append(j)

if ct!=1:
    print("Solution Not Found")