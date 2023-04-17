# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_filter.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: joslopez <joslopez@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/16 16:00:17 by joslopez          #+#    #+#              #
#    Updated: 2023/04/16 20:39:58 by joslopez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
sys.tracebacklimit = 0

def ft_filter(function_to_apply, iterable):
    
    """Filter the result of function apply to all elements of the iterable.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    An iterable.
    None if the iterable can not be used by the function.
    """
    try:
        for element in iterable:
            if function_to_apply(element):
                yield element
    except TypeError:
        return None