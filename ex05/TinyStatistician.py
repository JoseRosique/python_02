# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    TinyStatistician.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: joslopez <joslopez@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/16 19:51:25 by joslopez          #+#    #+#              #
#    Updated: 2023/04/17 14:15:54 by joslopez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import math

class TinyStatistician:
    
    def mean(self, x):
        if len(x) == 0:
            return None
        return sum(x)/len(x)
    
    def median(self, x):
        if len(x) == 0:
            return None
        x_sorted = sorted(x)
        n = len(x_sorted)
        if n % 2 == 0:
            return (x_sorted[n//2-1] + x_sorted[n//2])/2
        else:
            return x_sorted[n//2]
        
    def quartiles(self, x):
        if len(x) == 0:
            return None
        x_sorted = sorted(x)
        n = len(x_sorted)
        q1 = 0
        q3 = 0

        q1 = float((x_sorted[n//4]))
        q3 = float((x_sorted[n//4 * 3]))
        return q1, q3
    
    def var(self, x):
        if len(x) == 0:
            return None
        x_mean = self.mean(x)
        return sum([(xi - x_mean)**2 for xi in x])/len(x)
    
    def std(self, x):
        if len(x) == 0:
            return None
        return math.sqrt(self.var(x))