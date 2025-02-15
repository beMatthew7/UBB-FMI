bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
;interpretare cu semn
;(a-b+c*128)/(a+b)+e-x

segment data use32 class=data
    ; ...
    a db 8
    b db 4
    c dw 1
    e dd 7
    x dq 5

; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov al, [a] ; al = a
        sub al, [b] ; al = a - b
        cbw
        cwde ; eax = a - b
        
        mov ebx, eax ; ebx = a - be
        mov ax, [c] ; ax = c
        mov cx, 128 ; cx = 128
        imul cx ; dx:ax = ax * cx = c * 128
        
        push dx
        push ax
        pop eax ; eax = dx:ax = c * 128
        
        add ebx, eax ; ebx = (a-b+c*128)
        
        mov al, [a] ; al = a
        add al, [b] ; al = a + b
        cbw ; ax = a + b
        
        mov cx, ax ; cx = a + b
        
        push ebx
        pop ax
        pop dx ;dx:ax = eax = (a-b+c*128)
        
        idiv cx ; ax = (a-b+c*128)/(a+b)
        
        cwde ; eax = (a-b+c*128)/(a+b)
        
        add eax, [e] ; eax = (a-b+c*128)/(a+b)+e
        cdq ; edx:eax = (a-b+c*128)/(a+b)+e
        
        ;ecx:ebx = x
        mov ebx, dword [x + 0] ;
        mov ecx, dword [x + 4] ; mutarea x pe ecx:ebx
        
        clc
        sub eax, ebx
        sbb edx, ecx ; edx:eax = (a-b+c*128)/(a+b)+e-x

        
        
        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
