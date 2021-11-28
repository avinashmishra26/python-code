def impl(I) :
    my_dict = {}
    for data in I :
       if data < -1 :
            if -1 in my_dict:
                my_dict[-1].append(data)
            else:
                my_dict[-1] = [data]
       elif -1<= data < 1 :
            if 0 in my_dict:
                my_dict[0].append(data)
            else:
                my_dict[0] = [data]
       else:
            if 1 in my_dict:
                my_dict[1].append(data)
            else:
                my_dict[1] = [data]

    return my_dict


#print(impl([-1.2,-3.4, 0.5, 1,2,3,5]))

for i in range(10,20,2):
    print(i)

str = "smkndsd"

print(str[1:5])

