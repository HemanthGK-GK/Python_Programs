# Sum of three Integer adds to ZERO
def findThreeSum(arr,m):

    found = False
    #assign i for first value of arr
    for i in range(0,m):
        #assign j for second value of arr
        for j in range(i+1,m):
            #assign k for third value of arr
            for k in range(j+1,m):
                #checking condition
                if (arr[i]+arr[j]+arr[k]==0):
                    print(arr[i],arr[j],arr[k])
                    found=True
    if (found==False):
        print("No Triplets found")


#Get input from user
arr=[]
m = int(input("Enter the length of array"))
if m>=3:
    for i in range(m):
        arr.append(int(input("Enter a number")))
print(arr)
# calling function
findThreeSum(arr)