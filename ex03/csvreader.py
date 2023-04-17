# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    csvreader.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: joslopez <joslopez@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/16 17:27:01 by joslopez          #+#    #+#              #
#    Updated: 2023/04/17 14:06:52 by joslopez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import csv
import sys
sys.tracebacklimit = 0

class CsvReader():
    def __init__(self, filename=None, sep=', ', header=False, skip_top=0, skip_bottom=0):
        if not filename:
            raise ValueError("must specify a file to read")
        if not isinstance(skip_top, int) or skip_top < 0:
            raise ValueError("skip_top must be a positive integer")
        if not isinstance(skip_bottom, int) or skip_bottom < 0:
            raise ValueError("skip_bottom must be a positive integer")
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.file_obj = None
        self.fulldata = []

    def __enter__(self):
        self.file_obj = open(self.filename, mode="r", encoding="utf-8")
        for line in self.file_obj:
            self.fulldata.append(list(map(str.strip, line.split(self.sep))))
        if all(len(elem) == len(self.fulldata[0]) for elem in self.fulldata):
            return self
        else:
            return None

    def __exit__(self, type, value, traceback):
        self.fulldata = []
        self.file_obj.close()

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
            Returns:
            nested list (list(list, list, ...)) representing the data.
        """
        start = self.skip_top
        end = len(self.fulldata) - self.skip_bottom
        if self.header:
            return self.fulldata[ start + 1 : end ]
        else:
            return self.fulldata[ start : end ]

    def getheader(self):
        """ Retrieves the header from csv file.
            Returns:
            list: representing the data (when self.header is True).
            None: (when self.header is False).
        """
        if self.header:
            return self.fulldata[0]
        else:
            return None

if __name__ == "__main__":
    filename = sys.argv[1]
    with CsvReader(filename, skip_top=18, skip_bottom=0) as reader:
        if reader == None:
            print("File is corrupted or missing")
        else:
            print(reader.getheader(), end = "\n")
            print(reader.getdata(), end = "\n\n")
            
    with CsvReader(filename, header = True, skip_top=17, skip_bottom=0) as reader:
        if reader == None:
            print("File is corrupted or missing")
        else:
            print(reader.getheader(), end = "\n")
            print(reader.getdata(), end = "\n\n")