#ifndef XLEN
#define XLEN 64
#endif

int test(int rs1, int rs2) {
	int index = rs2 & (XLEN - 1);
	int rd = rs1 | (1 << index);
	return rd; 
}
