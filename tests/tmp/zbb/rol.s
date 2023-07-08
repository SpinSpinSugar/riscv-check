	.file	"rol.c"
	.option nopic
	.attribute arch, "rv64i2p1_f2p2_d2p2_zicsr2p0_zba1p0_zbb1p0_zbc1p0_zbs1p0"
	.attribute unaligned_access, 0
	.attribute stack_align, 16
	.text
	.align	2
	.globl	test
	.type	test, @function
test:
	li	a5,6
	li	a2,1
	li	a3,64
.L2:
	sllw	a4,a2,a5
	addiw	a5,a5,1
	andn	a1,a1,a4
	sext.w	a1,a1
	bne	a5,a3,.L2
	li	a5,64
	subw	a5,a5,a1
	sraw	a5,a0,a5
	sllw	a0,a0,a1
	or	a0,a5,a0
	sext.w	a0,a0
	ret
	.size	test, .-test
	.ident	"GCC: (g2ee5e430018) 12.2.0"
	.section	.note.GNU-stack,"",@progbits
