bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, fscanf, fopen, fclose, fgets, fscanf, printf, fclose               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll  
import fscanf msvcrt.dll
import fopen msvcrt.dll
import fgets msvcrt.dll
import fscanf msvcrt.dll
import printf msvcrt.dll
import fclose msvcrt.dll  ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    file_name db "numere.txt", 0
    acces_mode db "r", 0
    file_descriptor dd -1
    numere times 20 db 0
    format_citire db "%d", 0
    
    format_afisare db "%d ", 0
    
    sir_nr_pare times 20 dd -1
    sir_nr_impare times 20 dd -1
    i dd 0
    j dd 0
; our code starts here
segment code use32 class=code
    start:
        ; ...
        push dword acces_mode
        push dword file_name
        call [fopen]
        add esp, 4 * 3
        
        cmp eax, 0
        je final
        mov dword [file_descriptor], eax
        
        citire_numere:
            push dword numere
            push dword format_citire
            push dword [file_descriptor]
            call [fscanf]
            add esp, 3 * 4
            
            cmp eax, -1
            je gata_citirea
            
            mov ebx, dword[numere]
            shl bl, 7
            shr bl, 7
            cmp bl, 0
            je nr_par
            
            nr_impar:
                mov ebx, dword[numere]
                mov ecx, [j]
                mov dword[sir_nr_impare + ecx], ebx
                add ecx, 4
                mov dword[j], ecx
                
                mov dword[numere], 0
                jmp citire_numere
            
            nr_par:
                mov ebx, dword[numere]
                mov ecx, [i]
                mov dword[sir_nr_pare + ecx], ebx
                add ecx, 4
                mov dword[i], ecx
                
                mov dword[numere], 0
                jmp citire_numere
            

                
        
        
        
        gata_citirea:
        mov esi, sir_nr_pare
        afisare_sir_nr_pare:
            mov eax, [esi]
            cmp eax, -1
            je afisare_sir_nr_impare1
            push eax
            push format_afisare
            call [printf]
            add esp, 2 * 4
            add esi, 4
            jmp afisare_sir_nr_pare
            
                
                
                
        afisare_sir_nr_impare1:
        mov esi, sir_nr_impare
        afisare_sir_nr_impare:
            mov eax, [esi]
            cmp eax, -1
            je close
            push eax
            push format_afisare
            call [printf]
            add esp, 2 * 4
            add esi, 4
            jmp afisare_sir_nr_impare
        
        
        
        close:
        push dword[file_descriptor]
        call [fclose]
        add esp, 4
        
        
        
        
        
        
        
        final:
        
        
        
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
