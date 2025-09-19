// Q13) The following C program is meant to rotate a square matrix by 90 degrees clockwise. It first 
// transposes the matrix and then reverses each row. However, the code contains an indexing error that 
// causes incorrect rotation. 
#include <stdio.h> 
#define N 3 
void rotateMatrix(int mat[N][N]) { 
    for(int i=0; i<N; i++) { 
        for(int j=i; j<N; j++) { 
            int temp = mat[i][j]; 
            mat[i][j] = mat[j][i]; 
            mat[j][i] = temp; 
        } 
    } 
    for(int i=0; i<N; i++) { 
        for(int j=0; j<N/2; j++) { 
            int temp = mat[i][j]; 
            mat[i][j] = mat[i][N-1-j]; 
            mat[i][N-1-j] = temp;
                    } 
    } 
} 
 
void printMatrix(int mat[N][N]) { 
    for(int i=0; i<N; i++) { 
        for(int j=0; j<N; j++) { 
            printf("%d ", mat[i][j]); 
        } 
        printf("\n"); 
    } 
} 
 
int main() { 
    int matrix[N][N] = { {1,2,3}, {4,5,6}, {7,8,9} }; 
    rotateMatrix(matrix); 
    printMatrix(matrix); 
    return 0; 
} 
// Output: 
// 7 4 1  
// 8 5 2  
// 9 6 3 
