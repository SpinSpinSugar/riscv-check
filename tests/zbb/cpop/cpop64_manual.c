#include <stdint.h>

int64_t test(int64_t rs) {
    int64_t count = 0;
    for (int i = 0; i < 64; ++i) {
        if (rs & (1ll << i)) ++count;
    }
    return count;
}
