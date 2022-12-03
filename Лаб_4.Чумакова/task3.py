def delete(list_2, index=None):
    if isinstance(index,  int) and index != -1:
        if not index:
            index = 0
            result = list_2[1:]
        elif index > 0:
            result = list_2[0:index] + list_2[index + 1:]
        else:
            len_ = len(list_2)
            new_index = len_ + index
            result = list_2[0:index] + list_2[index + 1:]
    else:
         result = list_2[:-1]
    return result

print(delete([0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
