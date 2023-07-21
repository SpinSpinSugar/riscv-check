#include <stdint.h>

int64_t test(int64_t x) {
    return __builtin_clzl(x);
}
