## Before running our shellcode
```asm
.data:0000000000202020 loc_202020:
.data:0000000000202020                 xor     r10d, r10d
.data:0000000000202023                 xor     r11d, r11d
.data:0000000000202026                 xor     r12d, r12d
.data:0000000000202029                 xor     r13d, r13d
.data:000000000020202C                 xor     r14d, r14d
.data:000000000020202F                 xor     r15d, r15d
.data:0000000000202032                 xor     r8d, r8d
.data:0000000000202035                 xor     r9d, r9d
.data:0000000000202038                 xor     eax, eax
.data:000000000020203A                 xor     ebp, ebp
.data:000000000020203C                 xor     ebx, ebx
.data:000000000020203E                 xor     ecx, ecx
.data:0000000000202040                 xor     edi, edi
.data:0000000000202042                 xor     esi, esi
.data:0000000000202044                 xor     esp, esp
.data:0000000000202046                 cdq
.data:0000000000202047                 db    0
```

## Hidden function in .init_array
```c
void sub_aa0() {
    int var_4 = edi;
    long var_10 = rsi;
    long var_18 = rdx;
    // check if file exists
    if (access("/flag", 0) == 0) {
        int64* loc_cafe000 = mmap(0xcafe000, 4096, 7, 0x32, 0, 0);
        int fd = open("/flag", 0, 0); // O_RDONLY
        read(fd, loc_cafe000, 48);
        int fd1 = open("/dev/urandom", 0, 0);
        read(fd1, loc_cafe000 + 10, 8);
        int i = 0;
        do {
            loc_cafe000[i] ^= loc_cafe000[10];
        } while (i < 6);
        loc_cafe000[10] = 0;
    }
    return;
}
```

## How to get the flag
- At the beginning, we have flag at 0xcafe000 and key from '/dev/urandom' at 0xcafe050
- The length of flag is 48 bytes and the length of key is 8 bytes
- After xor encryption, we have the encrypted flag at 0xcafe000 and the key is erased
- We know that flag start with 'ISITDTU{', so we will using this 8 bytes to restore the key and save it in 0xcafe050
- To leak the decrypted flag, we xor the flag with the key we find above,we will brute force flag one-by-one byte
- Cause we cannot print the flag, so we need to check whether our character is included in the flag by using exit code. If it fail, we will make a read syscall and then program will return SIGSYS (cause by seccomp rules). Otherwise we will get (SIGALRM).
- Take a look at the shellcode in exploit.py for more detail.