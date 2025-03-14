bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
; interpretarea cu semn
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
        
        mov al, [a] ; al = al
        cbw ; al devine ax
        cwde ; ax devine eax
        cdq ; eax devine edx:eax, eax = [a]
        
        mov ebx, dword [d + 0] ;
        mov ecx, dword [d + 4] ; mutarea d pe ecx:ebx
        
       ;edx:eax = a - d
        clc
        sub  eax, ebx
        sbb edx, ecx
        
        ; ecx:ebx = a -d
        mov ebx, eax
        mov ecx, edx
        
        ;ax = b + b
        mov ax, [b]
        add ax, [b]
        cwde ; eax = b + b
        
        ; eax = b + b +c
        add eax, [c]
        cdq ; edx:eax = b + b +c
        
        ; edx:eax = a-d+b+b+c
        clc
        add eax, ebx
        adc edx, ecx
        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
