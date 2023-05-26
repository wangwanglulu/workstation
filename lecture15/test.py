start_time = [9,9.5,10,10.5,11]
end_time = [10,10.5,11,11.5,12]
selected = []
earlist_end = 0

for index, end in enumerate(end_time):
    if start_time[index] >= earlist_end:
        selected.append(index)
        earlist_class = index
        earlist_end = end
print(selected)