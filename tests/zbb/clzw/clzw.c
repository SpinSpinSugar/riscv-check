#include <stdint.h>

int test(int32_t x) {
    return __builtin_clz(x);
}

