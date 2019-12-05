# importing numpy and pandas
import numpy as np
import random

no_of_in = input("Enter the number of input units: ") # number of input units
no_of_in = int(no_of_in) # converting string to int

while 1:
	no_of_out = int(input("Enter the number of output units: ")) # no of output units
	if no_of_out > no_of_in:
		print('Your number of output(s) are more than the number of input(s)')
		continue
	else:
		break

dis = list(np.zeros(no_of_out, dtype = float))  # Distance of input units from the output units
dis_temp = list(np.zeros(no_of_out, dtype = float))

alpha = input("Enter the learing rate: ") # Learning rate
alpha = float(alpha)

check = input("Do you want to enter the individual values of the inputs (y/n): ")

if check == 'y':
	print("Enter inputs row-wise in a line separated by space")
	values = list(map(float,input().split()))
	print("The array of inputs is\n")
	mat = np.array(values).reshape(no_of_in,no_of_in)
	print(mat)
else:
	# generating random array
	mat = np.random.rand(no_of_in,no_of_in)
	print("The array of inputs is\n")
	print(mat)
	print("\n")


M = np.random.rand(no_of_in,no_of_out) # Matrix of weights for the 2 output units
print("The initial array of weights:\n")
print(M)
print("\n")

# Copy of M
M_temp = np.copy(M)

#calculating the euclid distance and updating weights
count = 1
while 1:
	for u in range(0,no_of_in):
		#print("Calculating for input unit",u+1)
		for s in range(0,no_of_out):
			for ind,val in zip(range(0,no_of_in),mat[u]):
				dis[s] = dis[s] + ((val - M[ind][s])*(val - M[ind][s]))
				dis_temp[s] = dis_temp[s] + ((val - M[ind][s])*(val - M[ind][s]))
			#print('Distance' + str(s+1) + ' = ' + str(dis[s]))

		dis_temp.sort()


		#print("Distance from unit {} is less".format(dis.index(dis_temp[0])))
		for ind,val in zip(range(0,no_of_in),mat[u]):
			M[ind][dis.index(dis_temp[0])] = M[ind][dis.index(dis_temp[0])] + alpha * (val - M[ind][dis.index(dis_temp[0])])


		#print("After unit",u+1)
		dis_temp = list(np.zeros(no_of_out, dtype = float))
		dis = list(np.zeros(no_of_out, dtype = float))
	print('\n')
	print("After Iteration number: {}".format(count))
	print("Present array:")
	print(M)
	print('\n')
	print("Previous array:")
	print(M_temp)
	if np.array_equal(M_temp,M):
		break
	count = count + 1
	M_temp = np.copy(M)


print("\n")
print("==============================")
print("After all the updates are done:\n")
print("Input array\n")
print(mat)
print("\n")
print("Updated array of weights\n")
print(M)
print("\n")
print("==============================")


#printing cluster values
print("Results:\n\n")

for u in range(0,no_of_in):
	for s in range(0,no_of_out):
		for ind,val in zip(range(0,no_of_in),mat[u]):
			dis[s] = dis[s] + ((val - M[ind][s])*(val - M[ind][s]))
			dis_temp[s] = dis_temp[s] + ((val - M[ind][s])*(val - M[ind][s]))

	dis_temp.sort(reverse=True)

	res = 'Unit ' + str(u+1) + ' belongs to cluster: ' + str(dis.index(dis_temp[0]) + 1)

	print(res)


	dis_temp = list(np.zeros(no_of_out, dtype = float))
	dis = list(np.zeros(no_of_out, dtype = float))
