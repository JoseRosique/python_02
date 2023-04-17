# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_reduce.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: joslopez <joslopez@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/16 16:00:31 by joslopez          #+#    #+#              #
#    Updated: 2023/04/16 20:40:25 by joslopez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
sys.tracebacklimit = 0

def ft_reduce(function_to_apply, iterable):
    
    """Apply function of two arguments cumulatively.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    A value, of same type of elements in the iterable parameter.
    None if the iterable can not be used by the function.
    """
    
    try:
        iterator = iter(iterable)
        accumulated_result = next(iterator)
        for element in iterator:
            accumulated_result = function_to_apply(accumulated_result, element)
        return accumulated_result
    except TypeError:
        return None