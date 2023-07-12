#include <stdint.h>

uint32_t test (uint32_t rs) {
  return rs & ~(1L << 20);
}

