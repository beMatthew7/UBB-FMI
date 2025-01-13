bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
extern fopen, fclose, fread, printf, scanf, fprintf
import fopen msvcrt.dll
import fclose msvcrt.dll
import fread msvcrt.dll
import printf msvcrt.dll
import scanf msvcrt.dll
import fprintf msvcrt.dll   ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    nume_fisier times 30 db 0
    text times 120 resb 1
    format_citire db "%s", 0
    format_new_line db "%s", 10, 0
    access_mode dd 'w', 0
    file_descriptor dd -1
    
; our code starts here
segment code use32 class=code
    start:
        ; ...
        push nume_fisier
        push format_citire
        call [scanf]
        add esp, 2 * 4

        

        push access_mode
        push nume_fisier
        call [fopen] 
        
        cmp eax, 0
        je final
        
        mov dword [file_descriptor], eax
        
        
        repeta:
            push text
            push format_citire
            call [scanf]
            add esp, 2 * 4
            
            cmp byte[text], '$'
            je close
        
        
            push text
            push format_new_line
            push dword [file_descriptor]
            call [fprintf]
            add esp, 4 * 3
        
        
        
        jmp repeta
        close:
        push dword[file_descriptor]
        call [fclose]
        add esp, 4
        
        
        
        
        final:
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
