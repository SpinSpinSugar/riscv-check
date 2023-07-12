#include <stdint.h>

uint32_t test(uint32_t rs1, uint32_t rs2) {
    uint32_t index = rs2 & (32 - 1);
    uint32_t res = rs1 | (1 << index);
    return res;
}

