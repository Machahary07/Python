// Q14) Given an integer array that may contain positive, negative, and zero values, implement a 
// function in C to find the maximum product of a contiguous subarray. The output of the following is 
// incorrect when the following code, the otput should match with code given below 
#include <stdio.h> 
int maxProduct(int arr[], int n) { 
    int max_so_far = arr[0]; 
    int curr_max = arr[0], curr_min = arr[0]; 
    for (int i = 1; i < n; i++) { 
        if (arr[i] < 0) { 
            int temp = curr_max; 
            curr_max = curr_min; 
            curr_min = temp; 
        } 
        curr_max = (arr[i] > curr_max * arr[i]) ? arr[i] : curr_max * arr[i]; 
        curr_min = (arr[i] < curr_min * arr[i]) ? arr[i] : curr_min * arr[i]; 
        if (curr_max > max_so_far) 
            max_so_far = curr_max; 
    } 
    return max_so_far; 
} 
 
int main() { 
    int arr[] = {6, -3, -10, 0, 2}; 
    int n = sizeof(arr)/sizeof(arr[0]); 
    printf("Maximum product subarray is %d", maxProduct(arr, n)); 
    return 0; 
} 
// Output : 180