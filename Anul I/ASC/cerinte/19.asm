bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, scanf, fopen, fprintf               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll
import scanf msvcrt.dll
import fopen msvcrt.dll
import fprintf  msvcrt.dll   ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    n dd 0
    format_citire_d db  "%d", 0
    format_citire_s db "%s", 0
    cuvant times 50 db 0
    acces_mode db "w", 0
    file_name db "text.txt", 0
    file_descriptor dd -1
    format_afisare db "%s", 10, 0
    

; our code starts here
segment code use32 class=code
    start:
        ; ...
        citire_n:
            push n
            push format_citire_d
            call [scanf]
            add esp, 2 * 4
            
        deschidere_fisier:
            push acces_mode
            push file_name
            call [fopen]
            add esp, 2 * 4
            
            cmp eax, 0
            je eroare
            mov dword[file_descriptor], eax
            
        citire_cuvinte:
            push cuvant
            push format_citire_s
            call [scanf]
            add esp, 2 * 4
            
            mov esi, cuvant
            inceput_cuvant:
                mov edi, esi
            citire_caracter_cu_caracter:
                lodsb
                cmp al, '#'
                je final
                cmp al, 0
                je verificare_cuvant
                jmp citire_caracter_cu_caracter
                
                
                verificare_cuvant:
                    dec esi
                    mov eax, esi
                    sub eax, edi
                    dec esi
                    
                    cmp eax, dword[n]
                    jb continua
                    mov al, byte[esi]
                    mov ah, byte[edi]
                    
                    cmp al, ah
                    jne continua
                    push  edi
                    push format_afisare
                    push dword [file_descriptor]
                    call [fprintf]
                    add esp, 3 * 4
                    
                    
                    
                    
                    continua:
                    inc esi
                    inc esi
                    jmp citire_cuvinte
            
            
        eroare: 
        final:
            
            
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
