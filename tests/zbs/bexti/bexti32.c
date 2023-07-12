#include <stdint.h>

uint32_t test (uint32_t rs) {
  return 1 & (rs >> 20);
}

