import re
import os
import time

def my_mkdir(name):
    if os.path.isdir(name) == False:
        os.system("mkdir " + name)

my_mkdir("html")
my_mkdir("data")
for component in ["Demographics", "Dietary", "Examination", "Laboratory", "Questionnaire"]:
    for year in range(1999, 2021, 2):
        os.system("wget -O ./html/" + str(year) + component + ".txt -o log.txt https://wwwn.cdc.gov/nchs/nhanes/search/datapage.aspx?Component=" + str(component) + "\&CycleBeginYear=" + str(year))

for year in range(1999, 2021, 2):
    my_mkdir("data/" + str(year))
    for component in ["Demographics", "Dietary", "Examination", "Laboratory", "Questionnaire"]:
        my_mkdir("data/" + str(year) + "/" + component)
        with open("html/"  + str(year) + component + ".txt") as f:
            print("Checking html/"  + str(year) + component + ".txt")
            page = f.read()
            print("len(page) = ", len(page))
        print("len(page) = ", len(page))
        urls = re.findall('(?<=href=").*?.XPT', page)
        print(urls)
        for url in urls:
            var_name = re.findall("(?<=/)[^/]*(?=.XPT)", url)[0]
            os.system("wget -O ./data/" + str(year) + "/" + component + "/" + var_name + " " + "https://wwwn.cdc.gov/" + url)
            time.sleep(1)

