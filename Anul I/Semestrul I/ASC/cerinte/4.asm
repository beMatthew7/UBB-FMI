bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, gets, printf            ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll
import gets msvcrt.dll
import printf msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    propozitie times 200 db 0
    numar_litere dd 0
    format_afisare db '%d ', 0
; our code starts here
segment code use32 class=code
    start:
        ; ...
        push propozitie
        call [gets]
        add esp, 4
        
        mov esi, propozitie
        
        numarare_litere:
            lodsb
            cmp al, 0
            je afisare_finala
            add dword[numar_litere], 1
            cmp al, ' '
            je afisare
            jmp numarare_litere
         

        afisare:
            sub dword[numar_litere], 1
            push dword[numar_litere]
            push format_afisare
            call [printf]
            
            mov dword[numar_litere], 0
            jmp numarare_litere
            
            
        afisare_finala: 
            push dword[numar_litere]
            push format_afisare
            call [printf]
            
            mov dword[numar_litere], 0            
            
        
        final:
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
