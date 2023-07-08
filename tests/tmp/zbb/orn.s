	.file	"orn.c"
	.option nopic
	.attribute arch, "rv64i2p1_f2p2_d2p2_zicsr2p0_zba1p0_zbb1p0_zbc1p0_zbs1p0"
	.attribute unaligned_access, 0
	.attribute stack_align, 16
	.text
	.align	2
	.globl	test
	.type	test, @function
test:
	orn	a0,a0,a1
	ret
	.size	test, .-test
	.ident	"GCC: (g2ee5e430018) 12.2.0"
	.section	.note.GNU-stack,"",@progbits
