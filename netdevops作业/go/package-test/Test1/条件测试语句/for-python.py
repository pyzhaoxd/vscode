
# // for key, value := range oldMap {
# //     newMap[key] = value
# // }


a = [1,2,3,4,5]
b = ['zhaoxd','sz','bj','dx','fs']
f= []


c = zip(a,b)

for key,value in c:
    f.append(key)
    f.append(value)
    print(f)