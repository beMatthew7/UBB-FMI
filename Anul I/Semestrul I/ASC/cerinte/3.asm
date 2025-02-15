; Simple x86 assembly program to print each word of a sentence on a new line
; Uses 32-bit NASM syntax
bits 32
; Declare entry point and external functions
    global start
    extern exit, gets, printf
    import exit msvcrt.dll
    import gets msvcrt.dll
    import printf msvcrt.dll

segment data use32 class=data
    format_input db "%s", 0   ; Format for gets
    text times 200 db 0        ; Buffer for input text
    format_newline db "%s", 10, 0 ; Format for printf with newline
    cuvant_invers times 50 db 0

segment code use32 class=code
start:
    ; Read input from user
    push text                  ; Address of input buffer
    call [gets]                ; Read string using gets
    add esp, 4                 ; Clean up the stack

    mov esi, text              ; Point to the beginning of the text
    mov edx, 45
print_words:
    mov edi, esi  
    mov edx, 45; Start of the current word

find_word:
    mov al, [esi]
    cmp al, 0                  ; Check for end of string
    je print_last_word
    mov ecx, 0
    
    cmp al, ' '

    je print_word
    mov byte [cuvant_invers + edx], al
    dec edx


    inc esi
    jmp find_word



    


   
print_word:
    mov byte [esi], 0 
    lea edi, [cuvant_invers + edx + 1]; Null-terminate the current word
             ; Push address of the word
    push edi
    push format_newline        ; Push format string
    call [printf]              ; Print the word
    add esp, 8                 ; Clean up the stack
    inc esi                    ; Move to the next character
    jmp print_words

print_last_word:
    cmp esi, edi               ; Check if there's any word left to print
    je end_program             ; If no word left, end the program
    mov byte [esi], 0 
    lea edi, [cuvant_invers + edx + 1]; Null-terminate the current word
             ; Push address of the word
    push edi
    push format_newline        ; Push format string
    call [printf]              ; Print the word
    add esp, 8                 ; Clean up the stack
    inc esi               ; Clean up the stack

end_program:
    push dword 0               ; Exit program
    call [exit]
