#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void bubble_sort(vector<int>& arr)
{
	bool swapped; // Flag to check if a swap occurred
	do
	{
		swapped = false; // Initialize flag as false for each iteration
		// Iterate over the array using an iterator
		for (auto it = arr.begin(); it != arr.end() - 1; ++it)
		{
			// If current element is greater than the next one
			if (*it > *(it + 1))
			{
				swap(*it, *(it + 1)); // Swap the two elements
				swapped = true; // Set flag to true as a swap occurred
			}
		}
	} while (swapped); // Continue if a swap occurred in the last iteration
}

int main()
{
	vector<int> array = { 5, 2, 3, 1, 4 }; // Declare and initialize a vector

	cout << "Unsorted array: ";
	// Iterate and print each number of the unsorted array
	for (const auto& num : array)
	{
		cout << num << " ";
	}
	cout << endl;

	bubble_sort(array); // Sort the array using the bubble_sort function

	cout << "Sorted array: ";
	// Iterate and print each number of the sorted array
	for (const auto& num : array)
	{
		cout << num << " ";
	}
	cout << endl;

	return 0;
}