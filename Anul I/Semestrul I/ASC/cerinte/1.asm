bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, fopen, fread, fclose, fscanf , printf, fgets              ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll 
import fopen msvcrt.dll
import fread msvcrt.dll
import fclose msvcrt.dll
import fscanf msvcrt.dll
import printf msvcrt.dll
import fgets msvcrt.dll   ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    file_name db "input.txt", 0
    acces_mode db "r", 0
    file_descriptor dd -1
    numere times 200 db 0
    format db "%s", 0
    format_afisare db "%c ", 0
    numar_min dd 0    
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
        
        citire:
            push dword [file_descriptor]
            push 200
            push numere
            call [fgets]
            add esp, 3 * 4
            
            mov esi, numere
        inceput_numar:
            mov byte [numar_min], 'F'
            mov edi, esi
            cld
        parcurgere_numere:
            lodsb
            cmp al, 0
            je final
            cmp al, ' '
            je afisare_numar_min
            cmp al, byte [numar_min]
            ja continua
            mov byte [numar_min], al
            continua:
            jmp parcurgere_numere
        
        
        afisare_numar_min:
        push dword [numar_min]
        push format_afisare
        call [printf]
        add esp, 2 * 4
        jmp inceput_numar
        final:
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
