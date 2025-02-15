bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, fopen, fscanf, printf , fprintf              ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll
import fopen msvcrt.dll
import fscanf msvcrt.dll
import printf msvcrt.dll
import fprintf msvcrt.dll     ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    sir db "abcdefgh", 0
    acces_mode_r db "r", 0
    acces_mode_w db "w", 0
    file_name_r db "razvi.txt", 0
    file_descriptor_r dd -1
    n dd 0
    file_name_w db"fisier_i.txt", 0
    format_citire db "%c", 0
    file_descriptor_w dd -1
    format_afisare db "%s", 0
    

; our code starts here
segment code use32 class=code
    start:
        ; ...
        push acces_mode_r
        push file_name_r
        call [fopen]
        add esp, 2 *4
        
        cmp eax, 0
        je final
        
        mov [file_descriptor_r], eax
        
        push n
        push format_citire
        push dword [file_descriptor_r]
        call [fscanf]
        add esp, 3 * 4
        
        mov ebx, [n]
        sub ebx, '0'
        mov ecx, 8
        sub ecx, ebx
        lea esi,[sir + ecx]
        repeta:
            mov bl, [n]
            mov [file_name_w + 7], bl
        
            push acces_mode_w
            push file_name_w
            call [fopen]
            add esp, 2 * 4
            
            cmp eax, 0
            je final
            mov dword[file_descriptor_w], eax
            
            push esi
            push format_afisare
            push dword[file_descriptor_w]
            call [fprintf]
            add esp, 3 * 4
            inc esi
            
            sub dword[n], 1
            mov bl, [n]
            cmp bl, '0'
            je final
            jmp repeta
            
            
            
        push dword[n]
        push format_citire
        call[printf]
        add esp, 2 * 4
        
        
        
        
        
        
        final:
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
