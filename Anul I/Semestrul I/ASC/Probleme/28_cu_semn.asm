bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, printf             ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll  
import printf msvcrt.dll  ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
;x - (a * 100 - b) / (b  + c + d)
segment data use32 class=data
    a dw 3
    b db 5
    c dd 7
    x dq 23
    d db 10
    format db "Rezultat:%d", 10, 13, 0

; our code starts here
segment code use32 class=code
    start:
        ; interpretare cu semn
        mov ax, [a]
        mov bx, 100
        
        imul bx ; dx:ax =  a * 100
        ;dx:ax -> ebx
        push dx
        push ax
        pop ebx
        
        mov al, [b]
        cbw
        cwde; eax = b
        
        
        sub ebx, eax ; ebx = a * 100 - b
        
        ; b + c
        mov al, [b]
        cbw
        cwde
        
        mov ecx, [c]
        add ecx, eax ; ecx = b + c
        
        mov al, [d]
        cbw
        cwde
        
        add ecx, eax ; ecx = b + c + d
        
        ; ebx -> edx:eax
        
        mov eax, ebx
        cdq
        
        idiv ecx ; eax = (a * 100 - b) /(b + c + d)
        
        
        push eax
        push format
        call [printf]
        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
