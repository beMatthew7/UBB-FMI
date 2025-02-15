bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, scanf              ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll
import scanf msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    format_citire db "%c", 0
    sir_numere times 50 db 0
    caracter dd 0
    sir_ordonat d

; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov edi, sir_numere
        
        citire_caractere:
            push caracter
            push format_citire
            call [scanf]
            add esp, 2 * 4
            
            mov al, [caracter]
            cmp al, '!'
            je afara
            cmp al, '0'
            jb citire_caractere
            cmp al, '9'
            ja citire_caractere
            
            stosb
            jmp citire_caractere
            
            
            
            
            
            
            
            
            
            
            afara:
                mov esi, sir_numere
                
                for1:
                    lodsb
                    mov bl, al
                    push esi
                    
                    
                    for2:
                        
                
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
