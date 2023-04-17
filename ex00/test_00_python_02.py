# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: joslopez <joslopez@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/16 16:11:39 by joslopez          #+#    #+#              #
#    Updated: 2023/04/17 13:59:06 by joslopez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from ft_map import ft_map
from ft_filter import ft_filter
from ft_reduce import ft_reduce

# Example 1:
print("Example 1: ")
x = [1, 2, 3, 4, 5]
result = ft_map(lambda dum: dum + 1, x)
print(result)
print(list(result))
print()
# Output:
# <generator object ft_map at 0x7f708faab7b0> # The adress will be different

list(ft_map(lambda t: t + 1, x))
# Output:
# [2, 3, 4, 5, 6]

# Example 2:
print("Example 2: ")
result = ft_filter(lambda dum: not (dum % 2), x)
print(result)
print()
# Output:
# <generator object ft_filter at 0x7f709c777d00> # The adress will be different

list(ft_filter(lambda dum: not (dum % 2), x))
# Output:
# [2, 4]

# Example 3:
print("Example 3: ")
lst = ['H', 'e', 'l',  'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
result = ft_reduce(lambda u, v: u + v, lst)
print(result)
# Output:
# "Hello world"

