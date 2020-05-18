def kadanes(arr):
    max_Current = 0
    max_Total = 0
    start = 0
    end = 0
    temp = 0

    for num in range(0,len(arr)):
        max_Current = max(arr[num], max_Current + arr[num])
        if max_Current < 0:
            max_Current = 0
            temp = num + 1
        print("num is: " + str(num) + " Max Current is: " + str(max_Current))
        if max_Current > max_Total:
            max_Total = max(max_Current,max_Total)
            start = temp
            end = num
        print("num is: " + str(num) + " Max Total is: " + str(max_Total))

    return max_Total, start, end

def main():
    #a = [3,-4,2,6,-3,2,10]
    a = [3,-4,4,5,2]
    b = kadanes(a)
    print("The max sum for a sub-array is is: " + str(b[0]) + " \nThe sub-array is:  " + str(a[b[1]:b[2] + 1]))

if __name__ == "__main__":
    main()


