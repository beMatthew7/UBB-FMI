bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
;x - (a * 100 - b) / (b  + c + d)
segment data use32 class=data
    a dw 3
    b db 5
    c dd 7
    x dq 23
    d db 10

; our code starts here
segment code use32 class=code
    start:
        ; interpretare fara semn
        mov ax, [a]
        mov bx, 100
        mul bx ; dx:ax = ax * bx = a * 100
        
        ; IL ADUCEM PE B IN CX:BX pentru scadere
        mov cx, 0
        mov bx, 0
        mov bl, [b]
        
        ;dx:ax - cx:bx
        sub ax, bx
        sbb dx, cx
        
        ; dx:ax -> eax 
        push dx
        push ax
        pop eax
        mov edx, 0
        
        ;b + c
        mov ebx, 0
        mov bl, [b]
        mov ecx, [c]
        
        add ebx, ecx; ebx =  b + c
        mov ecx, 0
        mov cl, [d]
        add ebx, ecx ; ebx =  b + c + d
        
        div ebx; eax = edx:eax / ebx = (a * 100 -b) / (b + c + d)
        mov edx, 0

        sub ebx, eax
        sbb ecx, edx
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
