#include <stdint.h>

uint32_t test(uint32_t rs) {
    uint8_t tmp = 0;
    uint32_t res = 0;
    for (int i = 0; i < 4; ++i) {
        tmp = rs >> (i * 8);
        uint32_t new_byte = ((uint32_t) tmp) << ((3 - i) * 8);
        res |= new_byte;
    }

    return res;
}

