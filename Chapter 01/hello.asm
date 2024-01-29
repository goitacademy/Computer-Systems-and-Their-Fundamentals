org  0x100             ; Вказівка, що це програма .COM
section .data
    message db 'Hello, World!', '$' ; Визначення рядка для виведення

section .text
_start:
    mov ah, 09h        ; Функція DOS для виведення рядка
    mov dx, message    ; Встановити DX на адресу рядка
    int 21h            ; Виклик DOS-переривання

    mov ax, 4c00h      ; Функція DOS для завершення програми
    int 21h            ; Виклик DOS-переривання