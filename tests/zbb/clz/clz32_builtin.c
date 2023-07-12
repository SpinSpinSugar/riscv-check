#include <stdint.h>

int32_t test(int32_t x) {
    return __builtin_clz(x);
}

