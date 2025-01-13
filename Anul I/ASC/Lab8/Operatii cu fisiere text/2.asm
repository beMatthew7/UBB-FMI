bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, fopen, fread, printf               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll 
import fopen msvcrt.dll
import fread msvcrt.dll
import printf msvcrt.dll   ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    vocale db "qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM", 0
    len1 equ $-vocale
    file_name db "file.txt", 0
    acces_mode dd 'r', 0
    file_descriptor dd -1
    format db "%d", 0
    char db 0
; our code starts here
segment code use32 class=code
    start:
        ; ...
        push dword acces_mode
        push dword file_name
        call [fopen]
        add esp, 2 * 4
        
        mov dword [file_descriptor], eax
        cmp eax, 0
        je final
        
        mov ebx, 0
        
        citire:
            push dword [file_descriptor]
            push dword 1
            push dword 1
            push dword char
            call [fread]
            add esp, 4 * 4
            cmp eax, 0
            je afisare


            mov esi, vocale
            mov ecx, len1
            cld
            
            repeta:
                lodsb
                cmp al, byte [char]
                jne next
                add ebx,1

                
                next:
                loop repeta
            jmp citire  
                
        
        afisare:

            
            push ebx
            push format
            call [printf]
            add esp, 2 * 4
            
        
        final:
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
