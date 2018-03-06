#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
Author:
Radhika Kulkarni
Nearest neighbor: This method calculates the euclidean distance between a test  vector 
and all the training  vectors and assigns the orientation of closest training data to the test data.

Input Train file :- criminal_train.csv
Input Test file:- criminal_test.csv
Output File: criminal_output.csv 

References:
https://www.pyimagesearch.com/2016/08/08/k-nn-classifier-for-image-classification/
http://shodhganga.inflibnet.ac.in/bitstream/10603/33597/12/12_chapter4.pdf


'''
from __future__ import division
from io import StringIO
import sys
import numpy as np


# ----------------Variable declarations----------------------------------------------------------
train_input = {}        # defined as dictionary
test_input = {}

P_detail_std = {}
str_write = ""



# ---------------For Nearest neighbor- Calculating  Euclidean distance-------------------------------

test_files = {}
train_files = {}



#--------- Function to read the data from the file given as parameter and returns a numpy array of that data
def read_files(file_name,flag):
    files = {}
    input_file = open(file_name, 'r')
    next(input_file)
    for line in input_file:
        data = line.split(",")
        P_detail = np.empty(70, dtype=np.float)
        index = 1
        i = 0
        while i < 70:
            P_detail[i] =float(data[index])
            index += 1
            i += 1
        if(flag==1):     
            files[data[0]] = {"orient": int(data[71].strip("\n")), "P_detail": P_detail}

        else:
            files[data[0]] = {"P_detail": P_detail}
    input_file.close()
    return files


 #------------Nearest Neighbor alogorithm---------------------------------------------------------------------- 

def test_nearest(train_files,test_files):
    i = 0

    nearest_file_str = StringIO()
    nearest_file_str.write("PERID"+","+"Criminal"+"\n")
    for test_f_id in test_files:
        i += 1
        test_f_P_detail = test_files[test_f_id]["P_detail"]

        min_dist = 999999
     
        P_detail_with_min_dist = ""

        for train_f_id in train_files:
            train_f_P_detail = train_files[train_f_id]["P_detail"]
            new_P_detail = np.subtract(train_f_P_detail, test_f_P_detail)
            new_P_detail = np.square(new_P_detail)
            dist = np.sum(new_P_detail)
            if dist < min_dist:
                min_dist = dist
                P_detail_with_min_dist = train_f_id
 
        nearest_file_str.write(
            test_f_id + ","+str(train_files[P_detail_with_min_dist]["orient"]) + '\n')


    return(nearest_file_str.getvalue())

#------------------------Nearest neighbor  Algorithm Ends------------------------------------------------------------



#--------------Function to write output to the file--------------------------------------------------------------------
def output_to_file(str_write):                
    with open('criminal_output.csv', 'w') as f:
        f.write(str_write)
        print("Final Output is written to criminal_output.csv")   
#---------------------------------------------------------------------------------------------------------------------   




#--------------------Main Section----------------------------------------------------------------------------------------------------------

if __name__ == "__main__":  

 train_file="criminal_train.csv"                # Train data file
 test_file="criminal_test.csv"                  # Test data file 
 flag=1                                         #Set flag=1 for train data file 
 train_files = read_files(train_file,flag)      #Read the train data file for the criminal record 
 print("Reading of Criminal Train file is complete!!\n")
 flag=0                                         #Set falg=0 for test data file     
 test_files = read_files(test_file,flag)        #Read the test file  for criminal record
 print("Reading of Criminal Test file is complete!!\n")
 print("Predicting the Criminal data based on Nearest Neighbor algorithm..\n")
 str_write=test_nearest(train_files,test_files)  # Call the nearest neighborhood algorithm 
 output_to_file(str_write)                   # Print the output to file
