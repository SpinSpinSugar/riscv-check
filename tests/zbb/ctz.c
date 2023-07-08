int test() {
	volatile int a = 0;
	return __builtin_ctz(a);
}
