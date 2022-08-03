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

    highest_amt = float(highest_amt)
    return(highest_amt)

print(overheads_write())

def cashonhand_write():
    coh_list = []
    for value in list:
        coh_list.append(value[1])

    