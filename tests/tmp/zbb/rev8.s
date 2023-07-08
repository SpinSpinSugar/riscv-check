	.file	"rev8.c"
	.option nopic
	.attribute arch, "rv64i2p1_f2p2_d2p2_zicsr2p0_zba1p0_zbb1p0_zbc1p0_zbs1p0"
	.attribute unaligned_access, 0
	.attribute stack_align, 16
	.text
	.align	2
	.globl	test
	.type	test, @function
test:
	lw	a3,0(a0)
	mv	a5,a0
	lui	a0,%hi(.LANCHOR0)
	addi	a4,a0,%lo(.LANCHOR0)
	sw	a3,28(a4)
	lw	a3,4(a5)
	lw	a2,28(a5)
	addi	a0,a0,%lo(.LANCHOR0)
	sw	a3,24(a4)
	lw	a3,8(a5)
	sw	a2,0(a4)
	lw	a1,24(a5)
	sw	a3,20(a4)
	lw	a2,12(a5)
	lw	a3,20(a5)
	sw	a1,4(a4)
	sw	a2,16(a4)
	lw	a5,16(a5)
	sw	a3,8(a4)
	sw	a5,12(a4)
	ret
	.size	test, .-test
	.globl	y
	.bss
	.align	3
	.set	.LANCHOR0,. + 0
	.type	y, @object
	.size	y, 32
y:
	.zero	32
	.ident	"GCC: (g2ee5e430018) 12.2.0"
	.section	.note.GNU-stack,"",@progbits
