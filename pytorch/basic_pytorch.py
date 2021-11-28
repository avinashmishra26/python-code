# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



import torch

x = torch.empty(2,3)

print(x)



x = torch.ones(2,3)

print(x.dtype)


x = torch.ones(2,3, dtype= torch.int)

print(x.dtype)


lst = [[1,2,3],[4,5,6]]

x = torch.tensor(lst, dtype=torch.float)
print(x)
print(x.size())


x1 = torch.tensor([1,2])

x2 = torch.tensor([3,4])


z = x1+x2
print(z)


z = torch.add(x1,x2)
print(z)


print('inplace addition',x2.add_(x1))


x1 = torch.tensor([1,2])

x2 = torch.tensor([3,4])

print(torch.mul(x1,x2))



#slicing 
x = torch.randn(5,3)

print(x)

print(x[1,0:2])



print(x[1,1].item())


x=x.reshape(3,5)
print('x.size()',x.size())
x= x.view(-1,3)
print(x)



