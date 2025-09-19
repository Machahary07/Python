//Q12) The following C program attempts to sort an array of integers using the bubble sort algorithm. 
//However, it contains a logical error that prevents it from sorting the array correctly. 
#include <stdio.h> 
void bubbleSort(int arr[], int n) { 
    for(int i=0; i<n-1; i++) { 
        for(int j=0; j<n-1-i; j++) { 
            if(arr[j] > arr[j+1]) { 
                int temp = arr[j];
                arr[j] = arr[j+1]; 
                arr[j+1] = temp; 
            } 
        } 
    } 
} 
int main() { 
    int arr[] = {5, 3, 8, 4, 2}; 
    bubbleSort(arr, 5); 
    for(int i=0; i<5; i++) 
        printf("%d ", arr[i]); 
    return 0; 
} 
//Output:-     2 3 4 5 8