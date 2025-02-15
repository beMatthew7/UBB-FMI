bits 32

global start        
extern exit, printf, scanf               
import exit msvcrt.dll
import scanf msvcrt.dll
import printf msvcrt.dll

segment data use32 class=data
    a dd 0                       
    format_cititre db '%d', 0
    format_afisare db '%x', 0
    cifre_baza_16 db "0123456789ABCDEF", 0
    rezultat times 100 db 0      
    nr_cifre dw 0
segment code use32 class=code
    start:
            
        push a 
        push format_cititre
        call [scanf]
        add esp, 4 * 2
        
        push dword [a]
        push format_afisare
        call [printf]
        add esp, 4 * 2
        
        final:
        push dword 0             ; Terminare program
        call [exit]  