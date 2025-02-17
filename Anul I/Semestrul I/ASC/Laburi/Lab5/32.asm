bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    s db 1, 6, 3, 1
    len_s equ $-s
    d resb len_s-1

; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov ecx, len_s - 1
        mov esi, 0 ; pozitita in sirul s
        cmp ecx, 0
        jle final
        repeta:
            mov al, [s + esi]
            cbw ; ax = [s + esi]
            mov bl, [s + esi + 1]
            
            idiv bl ; al = catul
            
            mov [d + esi], al
            
            inc esi
            
        loop repeta
            
            
        
        
        
        
        
        
        final:
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
