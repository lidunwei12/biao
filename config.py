import re
ip_address = '192.168.20.240'
step_one_port = 8888
step_two_port = 8887
step_three_port = 8886
for line in open('config.ini'):
    line =line.replace('\n','')
    if line.find('ip =') != -1:
        ip = line[line.find('ip =')+4:].replace(' ','')
        print(ip)
    if line.find('step_one') != -1:
        step_one_port = int(re.findall(re.compile('\d+'), line)[0])
        print(step_one_port)
    if line.find('step_two') != -1:
        step_two_port = int(re.findall(re.compile('\d+'), line)[0])
        print(step_two_port)
    if line.find('step_three') != -1:
        step_three_port = int(re.findall(re.compile('\d+'), line)[0])
        print(step_three_port)
