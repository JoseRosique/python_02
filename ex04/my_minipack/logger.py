# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logger.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: joslopez <joslopez@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/16 18:40:54 by joslopez          #+#    #+#              #
#    Updated: 2023/04/16 18:48:14 by joslopez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import logging

class Logger:
    def __init__(self, name, log_file=None, level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        if log_file:
            handler = logging.FileHandler(log_file)
        else:
            handler = logging.StreamHandler()
        handler.setLevel(level)
        handler.setLevel(formater)
        self.logger.addHandler(handler)
        
    def info(self, message):
        self.logger.info(message)
        
    def warning(self, message):
        self.logger.warning(message)
    
    def error(self, message):
        self.logger.error(message)
        
    def critical(self, message):
        self.logger.critical(message)