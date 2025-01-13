bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, scanf, printf               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import scanf msvcrt.dll
import printf msvcrt.dll ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    a dd 0
    b dd 0
    format_citire db "%d%d", 0
    format_a1 db "%d < %d", 0
    format_a2 db "%d = %d", 0
    format_a3 db "%d > %d", 0
    
    
    
    

; our code starts here
segment code use32 class=code
    start:
        ; ...
        push a
        push b
        push format_citire
        call [scanf]
        
        mov eax, [a]
        mov ebx, [b]
        
        cmp eax, ebx
        je egal
        jl mai_mic
        jg mai_mare
        
        egal:
        push dword[a]
        push dword[b]
        push format_a2
        call [printf]
        add esp, 3 * 4
        
        jmp final
        
        mai_mic:
        push dword [a]
        push dword [b]
        push format_a3
        call [printf]
        add esp, 3 * 4
        jmp final
        
        mai_mare:
        push dword [a]
        push dword [b]
        push format_a1
        call [printf]
        add esp, 3 * 4
        jmp final
        
        final:
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
