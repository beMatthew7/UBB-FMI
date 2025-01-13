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
    format_citire db '%d', 0
    a dd 0
    max dd 0
; our code starts here
segment code use32 class=code
    start:
        ; ...
        citire:
        push a
        push format_citire
        call [scanf]
        add esp, 2 * 4
        
        mov eax, [a]
        mov ebx, [max]
     
        cmp eax, 0
        je afisare
        cmp eax, ebx
        jl citire
        mov [max], eax
        

        jmp citire
        
        afisare:
        
        push dword [max]
        push format_citire
        call [printf]
        add esp, 2 * 4
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
