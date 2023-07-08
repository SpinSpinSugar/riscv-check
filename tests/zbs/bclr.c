int test() {
	volatile int x = 0xff;
	int index = 5;
	return x & ~(1 << index);
}

