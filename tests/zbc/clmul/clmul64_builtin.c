#include <stdint.h>

uint64_t test(uint64_t x, uint64_t y) {
    return __builtin_riscv_clmul(x, y);
}

