# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_map.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: joslopez <joslopez@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/16 16:00:06 by joslopez          #+#    #+#              #
#    Updated: 2023/04/16 20:40:17 by joslopez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
sys.tracebacklimit = 0

def ft_map(function_to_apply, iterable):
    
    """Map the function to all elements of the iterable.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    An iterable.
    None if the iterable can not be used by the function.
    """
    
    try:
        for element in iterable:
            yield function_to_apply(element)
    except TypeError:
        return None