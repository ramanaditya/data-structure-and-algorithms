function sum(arr, n) {
  // Only change code below this line
  if (n <= 0) {
      return arr[0];
    } else {
      return sum(arr, n - 1) + arr[n];
    }
  // Only change code above this line
}
