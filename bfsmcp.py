from queue import Queue
def creatpath(v):
    dpath=[]
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
queue=Queue()
queue.put(start)
print("State Visited")
path={}
while queue.empty()== False :
        v=queue.get()
        path[v]=[]
        newstate=Rule(v)   
        path[v].extend(newstate)
        visited.append(v)
        print(v,end=" , ")
        if v==goal :
            print("")
            print("Solution Found")
            print("The Path is")
            path1=creatpath(v)
            path1.append(v)
            print(path1)
            ct=1
            break
        
        for j in newstate:
           (x,y,z)=j
           if j  not in  visited and x<4 and y<4 and x>-1 and y>-1 :
                queue.put(j)   

if ct!=1:
    print("Solution Not Found")


#missionaries and cannibals using dfs
visited=set()
printlist=[]

parent={}
queue=[]
queue.append(((3,3),'L'));
def legal(a):
    m=a[0][0]
    c=a[0][1]
    if(m<0 or c<0 or m>3 or c>3):
        return 0;
    #checking if cannibals are more than missionaries 
    if( (m<c and m>0 and c>0 ) or ((3-m)<(3-c) and (3-c)>0 and (3-m)>0)):
        return 0;
    return 1;
    
def mnc():
    while(queue):
        a=queue.pop(0);
        m1=a[0][0]
        c1=a[0][1]
        b1=a[1][0]
        if(a in visited):
            continue;
        if( not (m1==0 and c1==0 and b1=='R')):
            visited.add(((m1,c1),b1));
        if(m1==0 and c1==0 and b1=='R'):
            temp=[]
            t=a;
            temp.append(t);
            while(t in parent ) :
                t=parent[t]
                temp.append(t)
            temp.reverse()
            print(temp)
            continue
        if(b1=='L'):
            newel=(((m1-1,c1),'R'))
            if newel not in visited and legal(newel):
                 queue.append(newel)
                 parent[newel]=a
            newel=(((m1,c1-1),'R'))
            if newel not in visited and legal(newel):
                 queue.append(newel)
                 parent[newel]=a
            newel=(((m1-2,c1),'R'))
            if newel not in visited and legal(newel):
                 queue.append(newel)
                 parent[newel]=a
            newel=(((m1,c1-2),'R'))
            if newel not in visited and legal(newel):
                 queue.append(newel)
                 parent[newel]=a
            newel=(((m1-1,c1-1),'R'))
            if newel not in visited and legal(newel):
                 queue.append(newel)
                 parent[newel]=a
        if(b1=='R'):
            newel=(((m1+1,c1),'L'))
            if newel not in visited and legal(newel):
                 queue.append(newel)
                 parent[newel]=a
            newel=(((m1,c1+1),'L'))
            if newel not in visited and legal(newel):
                 queue.append(newel)
                 parent[newel]=a
            newel=(((m1+2,c1),'L'))
            if newel not in visited and legal(newel):
                 queue.append(newel)
                 parent[newel]=a
            newel=(((m1,c1+2),'L'))
            if newel not in visited and legal(newel):
                 queue.append(newel)
                 parent[newel]=a
            newel=(((m1+1,c1+1),'L'))
            if newel not in visited and legal(newel):
                 queue.append(newel)
                 parent[newel]=a



mnc();
    