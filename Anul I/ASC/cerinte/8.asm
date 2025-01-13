bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, fopen, fclose, fprintf, scanf, fprintf,printf               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll
import fopen msvcrt.dll
import fclose msvcrt.dll 
import scanf msvcrt.dll
import fprintf msvcrt.dll 
import printf msvcrt.dll  ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    file_name db "string.txt"
    sir times 200 db 0
    sir_majuscule times 200 db 0
    sir_minuscule times 200 db 0
    acces_mode db "w", 0
    format_citire db "%s", 0
    format_afisare db "%s ", 0
    i dd 198
    j dd 198
    file_descriptor dd -1
    

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
        
        citire_sir:
            push sir
            push format_citire
            call [scanf]
            add esp, 2 * 4
            
        mov esi, sir
        prelucrare_sir:
            lodsb
            cmp al, 0
            je afisare
            
            cmp al, 'A'
            jb continua
            cmp al, 'Z'
            ja continua
            
            mov ecx, [i]
            mov byte [sir_majuscule + ecx], al
            dec ecx
            mov [i], ecx
            jmp prelucrare_sir
            
            
            continua:
            cmp al, 'a'
            jb continua1
            cmp al, 'z'
            ja continua1
            
            mov ecx, [j]
            mov byte [sir_minuscule + ecx], al
            dec ecx
            mov [j], ecx
            jmp prelucrare_sir
            
            
            continua1:
            jmp prelucrare_sir
            
        
        
        afisare:
            mov ecx, [i]
            inc ecx
            lea edi, [sir_majuscule + ecx]
            push edi
            push format_afisare
            push dword [file_descriptor]
            call [fprintf]
            add esp, 3 * 4
            
            mov ecx, [j]
            inc ecx
            lea edi, [sir_minuscule + ecx]
            push edi
            push format_afisare
            push dword [file_descriptor]
            call [fprintf]
            add esp, 3 * 4
        
        final:
        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
