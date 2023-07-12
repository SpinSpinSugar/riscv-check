#include <stdint.h>

int test(int32_t rs) {
    int count = 0;
    for (int i = 0; i < 32; ++i) {
        if (rs & (1 << i)) {
            break;
        }
        ++count;
    }
    return count;
}

