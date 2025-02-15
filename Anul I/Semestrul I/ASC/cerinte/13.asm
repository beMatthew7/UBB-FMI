bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, scanf, printf               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll
import scanf msvcrt.dll  
import printf msvcrt.dll  ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    cuvant times 50 db 0
    numar dd 0
    format_citire db "%s %d", 0
    rest1 db 0
    format_afisare db "%s", 0
    vocale db "aeiou", 0
    cuvant_nou times 50 db 0
    

; our code starts here
segment code use32 class=code
    start:
    push numar
    push cuvant
    push format_citire
    call [scanf]
    add esp, 3 * 4
    
    
    mov eax, [numar]
    shl al, 7
    shr al, 7
    cmp al, 0
    je nr_par
    
    mov eax, [numar]
    push eax
    pop ax
    pop dx
    mov bx, 20
    div bx
    mov byte[rest1], al
    mov esi, cuvant
    mov edi, cuvant
        criptare_impar:
            lodsb
            cmp al, 0
            je afisare
            add al, [rest1]
            stosb
            jmp criptare_impar
            
            
    
    
    
    nr_par:
        mov esi, cuvant
        mov edi, cuvant_nou
        nr_par_while:
        lodsb
        cmp al, 0
        je afisare_nou
        cmp al, 'a'
        je continuare
        cmp al, 'e'
        je continuare
        cmp al, 'i'
        je continuare
        cmp al, 'o'
        je continuare
        cmp al, 'u'
        je continuare
        stosb
        mov bl, al
        mov al, 'p'
        stosb
        mov al, bl
        stosb
        jmp nr_par_while
        continuare:
            stosb
            jmp nr_par_while
        
        
        
    
        
    afisare:
        push cuvant
        push format_afisare
        call [printf]
        add esp, 2 * 4
        jmp final
        
        afisare_nou:
            push cuvant_nou
            push format_afisare
            call [printf]
            add esp, 2 * 4
            
        
        
        
        final:
        ; ...
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
