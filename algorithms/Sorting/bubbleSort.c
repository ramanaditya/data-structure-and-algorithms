/*
Bubble Sort:
Runtime:
    Worst: O(n^2)
    Average: O(n^2)
    Best: O(n)
Memory: O(1)
*/

#include <stdio.h>


// function for Bubble Sort
void BubbleSort(int *data[], int size) {
    int i, j, temp;
    for (i = 0; i < size; i++) {
        for (j = 0; j < size - i - 1; j++) {
            if (*data[j] > *data[j + 1]) {
                temp = *data[j];
                *data[j] = *data[j + 1];
                *data[j + 1] = temp;
            }
        }
    }
}

// Function to Print the elements
void display(int *data[], int size) {
    printf("\nThe array Sorted in ascending order is :\n");
    for (int i = 0; i < size; i++)
        printf(" %d\t", *data[i]);
}

// main function
int main()
{
    int i, size, data[10];

    printf("\nEnter the number of elements in the array : ");
    scanf("%d", &size);
    printf("\nEnter the elements: ");
    for(i = 0; i < size; i++)
    {
        scanf("%d", &data[i]);
    }

    // function bubble sorting
    BubbleSort(*data, size);
    display(*data, size);

    return 0;
}
