#include <stdint.h>

int64_t test(int64_t rs) {
    int count = 0;
    for (int i = 0; i < 64; ++i) {
        if (rs & (1ll << i)) {
            break;
        }
        ++count;
    }
    return count;
}

