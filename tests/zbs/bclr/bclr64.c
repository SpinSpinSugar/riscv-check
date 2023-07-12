#include <stdint.h>

uint64_t test(uint64_t rs1, uint64_t rs2) {
    uint64_t index = rs2 & (64 - 1);
    uint64_t res = rs1 & ~(1u << index);
    return res;
}

