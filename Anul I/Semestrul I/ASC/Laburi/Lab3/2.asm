bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
;interpretare fara semn
;((a + a) + (b + b) + (c + c)) - d
segment data use32 class=data
    ; ...
    a db 7
    b dw 19
    c dd 20
    d dq 10
; our code starts here
segment code use32 class=code
    start:
        ; ...
        ;al = a + a
        mov al, [a]
        add al, [a]
        
        mov bx, 0
        mov bl, al ; bx = al = a + a
        
        ; bx = (a + a) + (b + b)
        add bx, [b]
        add bx, [b]
        
        ; eax = (a + a) + (b + b)
        mov eax, 0
        mov ax, bx
        
        ;eax = (a + a) + (b + b) + (c + c)
        add eax, [c]
        add eax, [c]
        
        ; edx:eax = eax = (a + a) + (b + b) + (c + c)
        mov edx, 0
        
        mov ebx, dword [d + 0]
        mov ecx, dword [d + 4]
        
        ;edx:eax = ((a + a) + (b + b) + (c + c)) - d
        clc
        sub eax, ebx ; eax = eax - ebx
        sbb edx, ecx ; edx = edx - ecx
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
