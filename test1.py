def simulate(entries):
    """
    :param entries: (list(int)) The numerical record files
    :returns: (list(int)) The record files after running the malware
    """
    # Write your code here
    to_replace_positions = []
    for i in range(len(entries)):
        position_x = i
        position_t1 = i - 3
        position_tr = i + 4
        if ((position_t1 < 0) and (entries[position_tr] >= entries[position_x])):  # no left side
            to_replace_positions.append(i)

        elif ((position_t1 >= 0) and (position_tr < len(entries))):
            if entries[position_t1] >= entries[position_x] or entries[position_tr] >= entries[position_x]:
                to_replace_positions.append(i)

        else:  # no right side
            if position_tr>=len(entries) and entries[position_t1] >= entries[position_x]:
                to_replace_positions.append(i)

    for j in to_replace_positions:
        entries[j] = 0

    return entries


records = [1, 2, 0, 5, 0, 2, 4, 3, 3, 3]
print(simulate(records))
# Expected output