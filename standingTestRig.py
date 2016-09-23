import time

TIME_DELAY = 500 #time between tests in miliseconds


#this will get the RPM from the RPM sensor
def getRPM():
	#not yet implemented
	return 0

#this will get the force from the force sensor
def getForce():
	#not yet implemented
	return 0

#this function will ask the user how many tests they want and what file they want
#to ouput the data to. Then it will run the test the designated amount of times
def main():
	testName = input('Enter a name for this test: ')
	print('This test shall be refered to as: ' + testName)
	testLength = input('how many cycles would you like to run the test: ')

	check = input('Enter anything to begin test: ')
	
	#open file and set time zero
	outputFile = open(testName + ".csv", 'w')
	timeZero = time.time()

	#This will write the values to the file
	for i in range(int(testLength)):
		thisTime = time.time() - timeZero
		thisTimeStr = "{:.4f}".format(thisTime) #formats to up to .0000 precision string

		RPM = getRPM() #this needs to find the RPM from the motor
		force = getForce() #this needs to find the force from the motor
		outputFile.write(str(i) + ': Time = ' + thisTimeStr + ', RPM = ' + str(RPM) + ', force = ' + str(force) + '\n')
		time.sleep(TIME_DELAY / 1000.0)

	outputFile.close()

	testAgain = input('Test finished, do you want to test again? (Y/N): ')
	if testAgain == 'Y':
		main()




main()
