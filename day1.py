elf_dict = {}
elf_list = []

## Read and build up the elf numbers in a dict
## Each elf is unique
with open('day1_input.txt') as fp:
    line = fp.readline()
    elf_idx = 1
    elf_dict['calories'] = []
    while line:
        elf_dict['id']=elf_idx
        if line.rstrip() == '':
            elf_list.append(elf_dict.copy())
            elf_dict.clear()
            elf_dict['calories'] = []
            elf_idx+=1
        else:
            elf_dict['calories'].append(int(line.rstrip()))
        line = fp.readline()

## Sum up all the Calories
elf_dict = {}
for i in elf_list:    
    elf_dict[i['id']] = sum(i['calories'])    
    
## Use the max_value which is the ID to get the total Calories
max_value = max(elf_dict, key=elf_dict.get)
print(elf_dict[max_value])