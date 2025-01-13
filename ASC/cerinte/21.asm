bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, fopen, fscanf, printf, fgets               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll
import fopen msvcrt.dll
import fscanf  msvcrt.dll
import printf msvcrt.dll
import fgets msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    file_name db "text.txt", 0
    acces_mode db "r", 0
    format_citire db "%s", 0
    cuvant times 50 db 0
    file_descriptor dd -1
    format_afisare db "%s", 10, 0
    
    

; our code starts here
segment code use32 class=code
    start:
        ; ...
        push acces_mode
        push file_name
        call [fopen]
        add esp, 2 * 4
        
        cmp eax, 0
        je final
        
        mov dword[file_descriptor], eax
        
        citire_cuvinte:
            push dword[file_descriptor]
            push 50
            push cuvant
            call [fgets]
            add esp, 2 * 4
            
            cmp eax, -1
            je final
            mov ebx , 0
            mov bl , [cuvant]
            
            push cuvant
            push format_afisare
            call [printf]
            add esp, 2 * 4
            
            ; jmp citire_cuvinte
            
    
    
    
        final:
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
