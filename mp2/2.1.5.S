.global _main
.section .text

_main:

push	%ebp
mov	%esp,%ebp
mov $0xb,%eax
push $0x68732f
push $0x6e69622f
mov %esp, %ebx
xorl %edx,%edx
push %edx
push %ebx
mov %esp, %ecx
int $0x80
leave
ret
