bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, scanf, fopen               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll
import scanf msvcrt.dll
import fopen msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    file_name times 50 db 0
    acces_mode db 'w', 0
    format_citire db "%s", 0
    
; our code starts here
segment code use32 class=code
    start:
        ; ...
        push file_name
        push format_citire
        call [scanf]
        add esp, 2 * 4
        
        mov esi, file_name
        
        citire_nume:
            lodsb
            cmp al, 0
            je concatenare
            jmp citire_nume
            
        concatenare:
            dec esi
            mov edi, esi
            mov al, '.'
            stosb
            mov al, 't'
            stosb
            mov al, 'x'
            stosb
            mov al, 't'
            stosb
            
        push acces_mode
        push file_name
        call [fopen]
        add esp, 2 * 4
            
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
