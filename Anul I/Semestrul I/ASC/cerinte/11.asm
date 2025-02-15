bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, gets, fopen, fprintf               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll 
import gets msvcrt.dll
import fopen msvcrt.dll
import fprintf msvcrt.dll   ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    cuvinte times 200 db 0
    file_name times 30 db 0
    acces_mode db "w", 0
    file_descriptor dd -1
    format_afisare db '%s', 10, 0
    cuvant times 50 db 0
    
    
; our code starts here
segment code use32 class=code
    start:
        ; ...
        push cuvinte
        call [gets]
        add esp, 4
        
        mov esi, cuvinte
        mov edi, file_name
        
        citire_nume
            lodsb
            cmp al, ' '
            je nume_complet
            stosb
            jmp citire_nume
            
            
        nume_complet:
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
        
        cmp eax, 0
        je final
        
        mov dword[file_descriptor], eax
        
        lea edi, [cuvant + 48]
        citire_cuvinte:
            lodsb
            cmp al, 0
            je final
            cmp al, ' '
            je afisare_in_fisier
            mov [edi], al
            dec edi
            jmp citire_cuvinte
            
        
        
        
        afisare_in_fisier:
            inc edi
            push edi
            push format_afisare
            push dword[file_descriptor]
            call [fprintf]
            add esp, 3 * 4
            lea edi, [cuvant + 48]
            jmp citire_cuvinte
            
        
        
        
        
        final:
        inc edi
            push edi
            push format_afisare
            push dword[file_descriptor]
            call [fprintf]
            add esp, 3 * 4
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
