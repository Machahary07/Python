// Q11) The following C program is intended to merge two sorted integer arrays into a single sorted 
// array. However, it contains logical errors in the merging function. 
#include <stdio.h> 
void mergeArrays(int a[], int sizeA, int b[], int sizeB, int result[]) { 
int i=0, j=0, k=0; 
while(i < sizeA && j < sizeB) { 
        if(a[i] < b[j]) { 
            result[k++] = a[i++]; 
        } else { 
            result[k++] = b[j++]; 
        } 
    } 
        while(i < sizeA) { 
        result[k++] = a[i++]; 
    } 
    while(j < sizeB) { 
        result[k++] = b[j++]; 
    } 
} 
int main() { 
    int a[] = {51,30,11}; 
    int b[] = {2,40,6}; 
    int result[6]; 
    mergeArrays(a, 3, b, 3, result); 
    for(int i = 0; i < 6; i++) { 
        printf("%d ", result[i]); 
    } 
    return 0; 
}  
// Output: 1 2 3 4 5 6