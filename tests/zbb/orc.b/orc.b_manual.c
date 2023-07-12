#include <stdint.h>
//#include <stdio.h>

uint32_t test(uint32_t rs) {
    uint32_t res = 0;
    for (int i = 0; i < 4; ++i) {
        int8_t byte = rs >> (i * 8);
        if (byte) (res |= (0b11111111u << (i * 8)));
    }
    return res;
}

/*
int main() {
    //try change 1 to 0 or change 1 position
    printf("%x", test(0b010000000100000000000100000000001));
    return 0;
}
*/

