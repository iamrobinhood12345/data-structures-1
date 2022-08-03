def radix_sort(sort_list):
    """Radix sort method."""
    if len(sort_list) == 1 or not sort_list:
        return sort_list
    temp_dict, new_dict, last_dict = {}, {}, {}
    for item in sort_list:
        temp_dict.setdefault(int(str(item)[2]), [])
        temp_dict[int(str(item)[2])].append(item)
    print(temp_dict)
    for key, item in temp_dict.items():
        new_dict.setdefault(int(str(item)[1]), [])
        new_dict[int(str(item)[1])].append(item)
    for key, item in new_dict.items():
        last_dict.setdefault(int(str(item)[0]), [])
        last_dict[int(str(item)[0])].append(item)
    return last_dict



    # pivot = sort_list[0]
    # sort_list1 = []
    # sort_list2 = []
    # for item in sort_list[1:]:
    #     if item < pivot:
    #         sort_list1.append(item)
    #     else:
    #         sort_list2.append(item)
    # sort_list1 = radix_sort(sort_list1)
    # sort_list1.append(pivot)
    # sort_list2 = radix_sort(sort_list2)
    # return sort_list1 + sort_list2

