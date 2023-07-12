#include <stdint.h>

int test(int64_t x) {
    return __builtin_clz(x);
}

