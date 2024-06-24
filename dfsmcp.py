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


#missionaries and cannibals using dfs

visited=set()
printlist=[]
n=2
def mnc(m,c,boat):
    
    #if illegal node
    if(m<0 or c<0 or m>n or c>n):
        return;
    #checking if cannibals are more than missionaries 
    if( (m<c and m>0 and c>0 ) or ((n-m)<(n-c) and (n-c)>0 and (n-m)>0)):
     return;
    if( ( (m,c),boat)  in visited ):
       return;
    if( not (m==0 and c==0 and boat=='R')):
        visited.add(((m,c),boat));
    #print(visited)
    printlist.append(((m,c),boat));
    if(m==0 and c==0 and boat== 'R'):
        print(printlist) 
        print("\n")
        #visited.pop();
        printlist.pop();
        return;  
    if(boat=='L'):
        mnc(m-1,c-1,'R')
        mnc(m,c-1,'R')
        mnc(m-1,c,'R')
        mnc(m-2,c,'R')
        mnc(m,c-2,'R')
        
    if(boat=='R'):
        mnc(m+1,c+1,'L')
        mnc(m,c+1,'L')
        mnc(m+1,c,'L')
        mnc(m+2,c,'L')
        mnc(m,c+2,'L')
    printlist.pop();
    

        
        
        
mnc(n,n,'L');