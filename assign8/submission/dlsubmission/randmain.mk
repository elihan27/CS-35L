OPTIMIZE = -O2

CC = gcc
CFLAGS = $(OPTIMIZE) -g3 -Wall -Wextra -march=native -mtune=native -mrdrnd

randlibhw.so:
	$(CC) $(CFLAGS) -fPIC -c randlibhw.c
	$(CC) $(CFLAGS) -shared randlibhw.o -o randlibhw.so

randlibsw.so:
	$(CC) $(CFLAGS) -fPIC -c randlibsw.c
	$(CC) $(CFLAGS) -shared	randlibsw.o -o randlibsw.so

randmain: 
	$(CC) $(CFLAGS) -static -c randmain.c randcpuid.c
	$(CC) $(CFLAGS) -ldl -Wl,-rpath=$PWD -o randmain randmain.o randcpuid.o 
