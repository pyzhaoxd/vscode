import re
import sys

log_file = sys.argv[1]
sum_line = []
reachable_line = []
unreachable_line = []

with open(log_file,mode="r",encoding='utf8') as f:
    lines = len(f.readlines())
    #print(lines)
    sum_line.append(lines)
    #print(sum_line)


with open(log_file,mode="r",encoding='utf8') as p:
    for lines in p.readlines():
        linestrip = lines.strip()
        #print(linestrip)

 
        reg = r'time=(\d+\.?\d)'
        search_reachable = re.compile(reg)
        reachable = re.search(search_reachable, linestrip)
        if reachable:
            out = reachable.group(1)
            finout = float(''.join(out))
            #print(out)
            reachable_line.append(finout)

        reg1 = r"yet"
        search_unreachable = re.compile(reg1)
        unreachable = re.search(search_unreachable,linestrip)
        if unreachable:
            out1 = unreachable.group()
            finout1 = out1.replace('yet','1')
            finout2 = int(finout1)    
            unreachable_line.append(finout2)


total_time = sum(reachable_line)
total = round(total_time,2)
avg = total / len(reachable_line)



print("test total ping sum: ",sum_line)   
print("test ping reachableline: " ,len(reachable_line))
print("test ping unreachable line: ",len(unreachable_line))
print("test total ping Reachable max vaule: ",max(reachable_line))
print("test total ping Reachable min vaule: ",min(reachable_line))
print("test ping avg time: ",round(avg,2))


