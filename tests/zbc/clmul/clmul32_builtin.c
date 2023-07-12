#include <stdint.h>

uint32_t test(uint32_t x, uint32_t y) {
    return __builtin_riscv_clmul(x, y);
}

