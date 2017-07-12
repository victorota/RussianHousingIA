#!/usr/bin/python
import csv
import numpy as np

if __name__ == '__main__' :
    f = open('train.csv','r');
    reader = csv.reader(f)
    next(reader, None)
    X = []
    y = []
    for row in reader:
        exemplo = [int(row[0])]
        preco = [int(row[-1])]
        X.append(exemplo)
        y.append(preco)
    for i in range(len(X)):
        print (X[i], y[i])