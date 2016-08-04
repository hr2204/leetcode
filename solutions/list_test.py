print [3,3,3,31,2,3][:-1] + [1]

my_list=[1]


def add_ele(list):
    list.append(2)


def replace(list):
    list = [5,6]
    return list

add_ele(my_list)
print my_list

replace(my_list)
print my_list



if __name__ == "__main__":
    # assert Solution().rotate([1,2,3,4,5,6,7])
    Solution().rotate([1,2],1)