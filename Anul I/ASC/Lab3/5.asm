bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
;interpretare fara semn
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
        mov bx, 0
        mov bl, [a] ; bx = a
        sub bl, [b] ; bx = a - b
        
        
        mov ax, [c] ; ax = c
        mov cx, 128
        mul cx ; dx:ax = ax * bx = c * 128
        
        add ax, bx; dx:ax = (a-b+c*128)
        
        mov cx, 0
        mov cl, [a]
        add cl, [b] ; cx = a + b
        
        div cx; ax = (a-b+c*128)/(a+b)
        mov cx, ax
        mov eax, 0
        mov ax, cx ; eax = (a-b+c*128)/(a+b)
        
        
        add eax, [e] ; eax = (a-b+c*128)/(a+b)+e
        
        mov edx, 0; edx:eax = eax = (a-b+c*128)/(a+b)+e
        
        ;ecx:ebx = x
        mov ebx, dword [x + 0] ;
        mov ecx, dword [x + 4] ; mutarea x pe ecx:ebx
        
        ; ecx:ebx = (a-b+c*128)/(a+b)+e-x
        clc
        sub eax, ebx
        sbb edx, ecx
        
        
        
        
        
        
        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
