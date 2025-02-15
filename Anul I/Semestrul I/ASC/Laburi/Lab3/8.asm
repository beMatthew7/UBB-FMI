bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
;interpretare  semun
;(a*b-2*c*d)/(c-e)+x/a
segment data use32 class=data
    ; ...
    a db 8
    b db 6
    c db 4
    d db 2
    e dw 2
    x dq 32

; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov al, [a] ; al = a
        mov bl, [b] ; bl = b
        imul bl ; ax = a * b
        cwde ; eax = a * b
        mov ecx, eax ; ecx = a * b
        
        
        mov al, [c] ; al = c
        mov bl, [d] ; bl = d
        
        imul bl ; ax = c * d
        cwde; eax = c * d
        add eax, eax ; eax = 2 * c * d
        
        sub ecx, eax
        
        mov al, [c] ; al = c
        cbw
        sub ax, [e] ; ax = c - e
        mov bx, ax ; bx = c -e
        
        push ecx
        pop ax
        pop dx ; dx:ax = ecx = (a*b-2*c*d)
        
        div bx ; ax = (a*b-2*c*d)/(c-e)
        mov bx, ax ; bx = (a*b-2*c*d) / (c-e)
        
        
        mov al, [a]
        cbw
        cwde ; eax = a
        mov ecx, eax ; ecx = a
        mov eax, dword [x + 0] ;
        mov edx, dword [x + 4] ; mutarea x pe edx:abx
        
        idiv ecx ; eax = x / a
        mov ecx, eax
        
        mov ax, bx ; ax = (a*b-2*c*d) / (c-e)
        cwde
        
        add eax, ecx ; eax = (a*b-2*c*d)/(c-e)+x/a
        
        
        
        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
