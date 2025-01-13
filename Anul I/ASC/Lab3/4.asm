bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
; interpretare cu semn
; a + b + c + d - (a + b)
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
        ; al = a
        mov al, [a]
        cbw ; ax = a
        
        ; ax =  a + b
        add ax, [b]
        cwde ; eax =  a + b
        
        ;eax =  a + b + c
        add eax, [c]
        cdq ; edx:eax = a + b + c
        
        ;ecx:ebx = d
        mov ebx, dword [d + 0] ;
        mov ecx, dword [d + 4] ; mutarea d pe ecx:ebx
        
        ;ecx:ebx = a + b + c + d
        clc
        add ebx, eax
        adc ecx, edx
        
        ; al = a
        mov al, [a]
        cbw ; ax = a
        
        ; ax =  a + b
        add ax, [b]
        cwde ; eax = a + b
        cdq ;  edx:eax = a + b
        
        
        ;ecx:ebx = a + b + c + d - (a + b)
        clc
        sub ebx, eax
        sbb ecx, edx
        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
