bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, gets , scanf , printf, fprintf  , fopen, fclose           ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll
import gets msvcrt.dll 
import scanf msvcrt
import printf msvcrt.dll 
import fopen msvcrt.dll
import fclose msvcrt.dll
import fprintf msvcrt.dll  ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    format_citire db  "%d", 0
    n times 5 db 0
    numar times 10 db 0
    suma_nr_pare dd 0
    suma_nr_impare dd 0
    acces_mode db "w", 0
    file_name db "2.txt", 0
    file_descriptor dd -1
    format_afisare db "Suma nr impare:%x, Suma nr pare %x, Diferenta:%x", 0
; our code starts here
segment code use32 class=code
    start:
        ; ...
        push acces_mode
        push  file_name
        call [fopen]
        add esp, 2 * 4
        
        cmp eax, 0
        je final
        mov dword [file_descriptor], eax
        
        
        push n
        push format_citire
        call [scanf]
        add esp, 2 * 4
        

        citire_numere:
            push numar
            push format_citire
            call [scanf]
            
            mov eax, [numar]
            mov bl, al
            shl bl, 7
            shr bl, 7
            cmp bl, 0
            je par
            mov eax, [numar]
            add [suma_nr_impare], eax
            jmp continua
            par:
            mov eax, [numar]
            add [suma_nr_pare], eax
            continua:
            sub dword [n], 1
            mov ecx, [n]
            cmp ecx, 0
            je afisare_sume
            jmp citire_numere
            
        
        
        
        afisare_sume:
            mov eax , dword [suma_nr_pare]
            sub eax,dword [suma_nr_impare]
            
            push eax
            push dword [suma_nr_pare]
            push dword [suma_nr_impare]
            push format_afisare
            push dword [file_descriptor]
            call [fprintf]
            add esp, 3 * 4
        
        final:
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
