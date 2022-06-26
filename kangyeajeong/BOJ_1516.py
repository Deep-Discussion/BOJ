a = int(input());
time = [];
buildings = []

for i in range(a):
    items = list(map(int,input().split()));
    time.append(items[0]); #-1 제외
    buildings.append(items[1 : len(items)-1]);

timeTable = []
for i in range(len(buildings)):   
    new = buildings[i];             #초기화
    for build in  buildings[i]:
        new = new + buildings[build-1];
    timeTable.append(list(set(new)));

result = [];
#건물을 동시에 짓는 경우가 있음

for i in range (len(timeTable)) :
    sums=time[i];
    for t in timeTable[i]:
        if( sums - time[t-1] >= 0 ) :
            sums -= time[t - 1] ;
        elif ( sums - time[t-1] <0 ) :
            sums+=time[t-1];
    result.append(sums);
 
print(result);
for ans in result :
    print(ans);



        

