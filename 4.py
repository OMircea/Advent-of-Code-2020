import re
with open("4.txt", "r") as fp:
    text = fp.read()

def checkDict(dictionar):
    cnt=0
    if "cid" in dictionar.keys():
        del dictionar["cid"]

    print(dictionar.keys())
    print(dictionar.values())
    if "byr" in dictionar.keys():
        if int(dictionar["byr"]) not in range(1920, 2003):
            del dictionar["byr"]

    if "iyr" in dictionar.keys():
        if int(dictionar["iyr"]) not in range(2010, 2021):
            del dictionar["iyr"]

    if "eyr" in dictionar.keys():
        if int(dictionar["eyr"]) not in range(2020, 2031):
            del dictionar["eyr"]

    if "hgt" in dictionar.keys():
        if dictionar["hgt"].isdigit():
            del dictionar["hgt"]
        if "hgt" in dictionar.keys():
            if "cm" in dictionar["hgt"]:
                print(dictionar["hgt"])
                dictionar["hgt"] = dictionar["hgt"].replace("cm", "")
                if int(dictionar["hgt"]) not in range(150, 194):
                    del dictionar["hgt"]

        if "hgt" in dictionar.keys():
            if "in" in dictionar["hgt"]:
                print(dictionar["hgt"])
                dictionar["hgt"] = dictionar["hgt"].replace("in", "")
                if int(dictionar["hgt"]) not in range(59, 77):
                    del dictionar["hgt"]

    if "hcl" in dictionar.keys():
        lung = len(dictionar["hcl"])
        is_ok = re.sub(r'#[0-9a-f]+', 'ok', dictionar["hcl"])
        if lung is 7 and is_ok is "ok":
            pass
        else:
            del dictionar["hcl"]


    if "ecl" in dictionar.keys():
        contor = 0
        lista = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        for elem in lista:
            if elem == dictionar["ecl"]:
                contor+=1
        if contor is 1:
            pass
        else:
            del dictionar["ecl"]

    if "pid" in dictionar.keys():
        lung = len(dictionar["pid"])
        nr = dictionar["pid"]
        if lung is 9 and nr.isdigit():
            pass
        else:
            del dictionar["pid"]

    for key in dictionar:
        cnt+=1

    #print(cnt)

    if cnt is 7:
        return 1
    else:
        return 0

def part_one():

    suma=0
    result = text.split("\n")
    dictionar={}
    for line in result:
        if line is '':
            suma+=checkDict(dictionar)
            dictionar.clear()
        else:
            lista = line.split(" ")
            for elem in lista:
                k,v = elem.split(":")
                dictionar[k]=v

    return suma

import time
st = time.time()
print(part_one())
sf = time.time()
print(sf-st)


