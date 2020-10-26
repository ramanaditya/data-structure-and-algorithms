// program to enter n numbers in an array.
// Redisplay the array with elements being sorted in ascending order.
// Bubble Sort method.

#include <stdio.h>


// function for Bubble Sort
void BubbleSort(int arr[], int size) {
    int i, j, temp;

    for (i = 0; i < size; i++) {

        for (j = 0; j < size - i - 1; j++) {

            if (arr[j] > arr[j + 1]) {

                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;

            }

        }

    }

    printf("\n The array Sorted in ascending order is :\n");
    for (i = 0; i < size; i++)
        printf(" %d\t", arr[i]);

}


// main function
int main()
{
    int i, size, arr[10];

    printf("\n Enter the number of elements in the array : ");
    scanf("%d", &size);
    printf("\n Enter the elements: ");
    for(i=0; i<size; i++)
    {
        scanf("%d", &arr[i]);
    }

    // function bubble sorting
    BubbleSort(arr, size);

    return 0;
}
