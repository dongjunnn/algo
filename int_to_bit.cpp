#include <bitset>
#include <vector>
#include <iostream>

std::vector<int> binary(int num, int width = 32) {
    std::bitset<32> bits(num);  // Handles two's complement for negatives
    std::vector<int> result;
    for (int i = width - 1; i >= 0; --i) {
        result.push_back(bits[i]);
    }
    return result;
}

