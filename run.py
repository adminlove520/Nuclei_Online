#run.py代码
import os

with open('domain.txt','r') as file:
    hosts = [line.strip() for line in file.readlines()]
for host in hosts:
    os.system("python3 ParamSpider/paramspider.py --domain "+host+" --output output/output.txt")