from numpy import *
import math 

#logistic regression
def getPoints():
	points=array(genfromtxt("Desktop\\data2.csv",delimiter=",", skip_header=1))
	

	X1=[]
	X2=[]
	Y=[]

	
	X1=points[:,1]
	X2=points[:,2]
	Y=points[:,3]

	return X1,X2,Y
  
  
def sigmoid(x):
  return 1 / (1 + math.exp(-x))

def hypothesis(length,theta0,theta1,theta2,X1,X2):
	hyp=(sigmoid(theta0+(X1*theta1)+(X2*theta2)))
	return hyp


def gradient_descent(l,X1_values,X2_values,Y_values,theta_values):

	err=0
	length=l
	mafia0=0
	mafia1=0
	mafia2=0
	rate=0.0001

	for i in range(0,length):
		err=hypothesis(length, theta_values[0],theta_values[1],theta_values[2],X1_values[i],X2_values[i])-Y_values[i]
		milf0=err*1
		milf1=err*X1_values[i]
		milf2=err*X2_values[i]
		mafia0+=milf0
		mafia1+=milf1
		mafia2+=milf2
  # milf0,1,2 are the variables where the error gets multiplied with the corresponding x value
  #mafia0,1,2 are the variables where the error gets all added up into one big variable. This will then be finally used in gradient descent.
  #sorry for the wierd names. Couldn't think of anything else at  the time. Please change these names if using for important stuff.
  theta=theta_values
		
	theta[0]=theta_values[0]-(float(rate/length)*mafia0)
	theta[1]=theta_values[1]-(float(rate/length)*mafia1)
	theta[2]=theta_values[2]-(float(rate/length)*mafia2)

	return theta
  
def gradient_descent_runner():

	#run gradient descent until the theta values reach global minimum
	#print the cost function after every iteration
	#to show that the error is getting reduced after every iteration

	X1,X2,Y=getPoints()

	theta=[1,2,3]
	length=99
  #keeping length till 99 when dataset has 100 points so that one point can be used for testing purposes.

	for i in range(0,100000):
		theta=gradient_descent(length,X1,X2,Y,theta)

	print(theta[0])
	print(theta[1])
	print(theta[2])

	print("The final values of theta 0 is: ",theta[0])
	print("The final values of theta 1 is: ",theta[1])
	print("The final values of theta 2 is: ",theta[2])

	print("Please enter X1 and X2 test values")
	x1=float(input(">> "))
	x2=float(input(">> "))

	print("Please enter the expected resultant value")
	y=input(">> ")

	h=theta[0]+float(theta[1]*x1)+float(theta[2]*x2)
	if h>0.5:
		print("The prediction of the model is: 1")
	else:
		print("The prediction of the model is: 0")

gradient_descent_runner()
