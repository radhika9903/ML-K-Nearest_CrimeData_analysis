# ML-K-Nearest_CrimeData_analysis
Predication of Criminals using ML K-Nearest algorithm


I have used K-Nearest Neighbours which is one of the most basic yet essential classification algorithms in Machine Learning. It belongs to the supervised learning domain and finds intense application in pattern recognition, data mining and intrusion detection.


How to Run:
1.Place all input files in one folder

2.Save crime_data_analysis.py in the same folder

3.Run ./crime_data_analysis.py from command line in python console Or from Spyder.



Algorithm
Let m be the number of training data samples. Let p be an unknown point.

1.Store the training samples in an array of data points arr[]. This means each element of this array represents a tuple (x, y).

2.for i=0 to m:
  Calculate Euclidean distance d(arr[i], p).

3.Make set S of K smallest distances obtained. Each of these distances correspond to an already classified data point.

4.Return the majority label among S.



Score :
 


Tools/Languages:
Python 3.0
Spyder 

