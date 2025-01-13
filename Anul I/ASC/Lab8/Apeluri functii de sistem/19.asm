bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, scanf, printf               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import scanf msvcrt.dll
import printf msvcrt.dll     ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    a dd 0
    b dd 0
    format_h db "%x%x", 0
    format_c db "%c%c", 0
    format db "nu" , 0
; our code starts here
segment code use32 class=code
    start:
        ; ...
        push a
        push b
        push format_h
        call [scanf]
        
        mov al, [a]
        mov bx, [b]
        
        mov ecx, 8
        verificare:
        cmp al, bl
        je da
        shl bx, 1
        loop verificare
        jmp nu
        da:
        push 'a'
        push 'd'
        push format_c
        call [printf]
        add esp, 4 * 2
        jmp final
        
        

        
        nu:
        
        push format
        call [printf]
        add esp, 4
        final :
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
