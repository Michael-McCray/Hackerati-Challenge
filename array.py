# Identify ascending/descending runs of 3 numbers in an unsorted array.

#input array
arr = [] 
while True:
	num = input("Please enter a number and type done when finished: ")
	if num.lower() == "done":
		#make sure there are enouphe numbers in array
		if len(arr) < 3:
			print("Needs to be atleast 3 numbers.")
			continue
		break
	try:
		#make srure a number was enterd
		num = int(num)
		arr.append(num)
	except:
		print("Oops!  That was not a valid number.  Try again...")

final = []
run = []

def findRun (arr):
	for i , v in enumerate(arr):
		run = arr[i:i+3] 
		#make sure it's a full run 
		if len(run) >= 3:
		#Does sum = middle element X 3?	
			if run[1] * 3 == sum(run):
				final.append(i)

#run function
findRun(arr)

#print position of run if found
if len(final)>= 1:
	print (final)
else:
	print ("no match")
