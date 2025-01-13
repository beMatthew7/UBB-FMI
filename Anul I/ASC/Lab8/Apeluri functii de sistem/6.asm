bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, scanf, printf               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll
import scanf msvcrt.dll
import printf msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    a dd 0
    b dw 0
    format_citire db '%d', 0
    format_afisare db "%d/%d = %d", 0
    cat dd 0

; our code starts here
segment code use32 class=code
    start:
        ; ...
        push a
        push format_citire
        call [scanf]
        
        push b
        push format_afisare
        call [scanf]
        
        mov ax, [a]
        mov dx, [a+2]
        mov bx, [b]
        
        div bx
        mov [cat], ax
        mov ax, [b]
        cwde
        
        push dword [cat]
        push eax
        push dword [a]
        push format_afisare
        call [printf]
        add esp, 4 * 3
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
