	.file	"ctz.c"
	.option nopic
	.attribute arch, "rv64i2p1_f2p2_d2p2_zicsr2p0_zba1p0_zbb1p0_zbc1p0_zbs1p0"
	.attribute unaligned_access, 0
	.attribute stack_align, 16
	.text
	.align	2
	.globl	test
	.type	test, @function
test:
	addi	sp,sp,-16
	sw	zero,12(sp)
	lw	a0,12(sp)
	addi	sp,sp,16
	ctzw	a0,a0
	jr	ra
	.size	test, .-test
	.ident	"GCC: (g2ee5e430018) 12.2.0"
	.section	.note.GNU-stack,"",@progbits
