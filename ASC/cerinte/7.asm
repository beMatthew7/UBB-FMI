bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, printf               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll
import printf msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    sir dq 123, 312321,312312321
    len equ $ - sir
    format_afisare db "%b ", 0
; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov esi, sir
        mov ebx, len
        afisare_bytes:
            mov eax, 0
            lodsb
            push eax
            push format_afisare
            call [printf]
            add esp, 2 * 4
            dec ebx
            cmp ebx, 0
            je final
            jmp afisare_bytes
            
            
            
        
        final:
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
