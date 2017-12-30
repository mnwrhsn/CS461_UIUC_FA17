#
#  Note: You must run ./setcookie before running make.
#

CC := gcc
CFLAGS := -m32 -static -U_FORTIFY_SOURCE -DCOOKIE=$(shell cat cookie)
LDFLAGS :=
LDLIBS :=

programs := 2.1.1 2.1.2 2.1.3 2.1.4 2.1.5 2.2.1 2.2.2 2.2.3 2.2.4 2.2.5 2.2.6 2.2.7 2.2.8 2.2.9 2.2.10 2.2.11

.PHONY: default clean install uninstall

default: $(programs) permissions

2.1.1: CFLAGS += -w
2.1.2: CFLAGS +=
2.1.3: CFLAGS +=
2.1.4: CFLAGS +=
2.1.5: CFLAGS +=
2.2.1: CFLAGS += -fno-stack-protector -z execstack
2.2.2: CFLAGS += -fno-stack-protector -z execstack
2.2.3: CFLAGS += -fno-stack-protector -z execstack
2.2.4: CFLAGS += -fno-stack-protector -z execstack
2.2.5: CFLAGS += -fno-stack-protector -z execstack
2.2.6: CFLAGS += -fno-stack-protector
2.2.7: CFLAGS += -fno-stack-protector -z execstack
2.2.8: CFLAGS += -fno-stack-protector -z execstack
2.2.9: CFLAGS += -fno-stack-protector
2.2.10: CFLAGS += -fno-stack-protector -z execstack
2.2.11: CFLAGS += -fno-stack-protector -z execstack -w

2.1.1: 2.1.1.c helper.c 2.1.1.S
2.1.2: 2.1.2.c helper.c 2.1.2.S
2.1.3: 2.1.3.c helper.c 2.1.3.S
2.1.4: 2.1.4.c helper.c 2.1.4.S
2.1.5: helper.c 2.1.5.S
2.2.1: 2.2.1.c helper.c
2.2.2: 2.2.2.c helper.c
2.2.3: 2.2.3.c helper.c
2.2.4: 2.2.4.c helper.c
2.2.5: 2.2.5.c helper.c
2.2.6: 2.2.6.c helper.c
2.2.7: 2.2.7.c helper.c
2.2.8: 2.2.8.c helper.c
2.2.9: 2.2.9.c helper.c
2.2.10: 2.2.10.c helper.c
2.2.11: 2.2.11.c helper.c

clean:
	rm -f $(programs)

permissions:
	sudo chown root:ubuntu 2.2.[123456789] 2.2.10 2.2.11 2.1.5
	sudo chmod 6777 2.2.[123456789] 2.2.10 2.2.11 2.1.5

