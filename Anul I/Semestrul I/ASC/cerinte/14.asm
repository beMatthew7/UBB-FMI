bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, fgets, fopen, printf, fclose               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll
import fgets msvcrt.dll
import fopen  msvcrt.dll
import printf msvcrt.dll 
import fclose msvcrt.dll   ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    file_name db "preufung.txt", 0
    acces_mode db "r", 0
    file_descriptor dd -1
    text times 200 db 0
    format_afisare db "%s ", 10, 0
    

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
        
        push dword [file_descriptor]
        push 200
        push text
        call [fgets]
        add esp, 3 * 4
        
        mov esi, text
        
        inceput_de_cuvant:
        mov edi, esi
        
        citire_caractere:
            lodsb
            cmp al, 0
            je verificare_cuvant_final
            cmp al, ' '
            je verificare_cuvant
            cmp al, '.'
            je verificare_cuvant
            jmp citire_caractere
            
            
        verificare_cuvant:
            dec esi
            mov eax, esi
            sub eax, edi
            cmp eax, 1
            je continua
            shl al, 7
            shr al, 7
            cmp al, 0
            je continua
            

            mov byte[esi], 0

            
            mov eax, esi
            sub eax, edi
            mov dx, 0
            mov bx, 2
            div bx
            mov byte[edi + eax], ' '
            
            push edi
            push format_afisare
            call [printf]
            add esp, 2 * 4
            
            
            
            
            
            
            
            continua:
            inc esi
            jmp inceput_de_cuvant
            
            
        
        
        
        
        verificare_cuvant_final:
            dec esi
            mov eax, esi
            sub eax, edi
            cmp eax, 1
            je close
            shl al, 7
            shr al, 7
            cmp al, 0
            je close
            

            mov byte[esi], 0

            
            mov eax, esi
            sub eax, edi
            mov dx, 0
            mov bx, 2
            div bx
            mov byte[edi + eax], ' '
            
            push edi
            push format_afisare
            call [printf]
            add esp, 2 * 4
            
            
            
        close:
            push dword[file_descriptor]
            call [fclose]
            add esp, 4
        final:
        
        
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
