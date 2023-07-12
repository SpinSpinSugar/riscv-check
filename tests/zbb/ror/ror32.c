#include <stdint.h>

uint32_t test(uint32_t rs1, uint32_t rs2) {
    int32_t shamt = rs2;
    for (int i = 5; i < 32; ++i) shamt &= ~(1 << i);
    uint32_t res = (rs1 >> shamt) | (rs1 << (32 - shamt));
    return res;
}

