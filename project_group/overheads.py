import read_file

list= read_file.overheads()

def overheads_write():
    all_overheads= []
    for value in list:
        all_overheads.append(value[1])

    highest_amt= max(all_overheads)
    

    for number, values in enumerate(all_overheads):
        if values== highest_amt:
            category= list[number][0]
    return category, highest_amt


print(overheads_write())

    