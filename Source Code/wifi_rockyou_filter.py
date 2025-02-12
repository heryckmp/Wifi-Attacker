#!/usr/bin/env python3
import re
import os

def is_valid_wifi_password(password):
    # Verifica se a senha tem entre 8 e 63 caracteres
    if len(password) < 8 or len(password) > 63:
        return False
    
    # Verifica se contém apenas caracteres ASCII imprimíveis
    if not all(ord(c) >= 32 and ord(c) <= 126 for c in password):
        return False
    
    return True

def filter_rockyou():
    try:
        # Arquivo de entrada (rockyou.txt)
        input_file = "rockyou.txt"
        # Arquivo de saída filtrado
        output_file = "wifi_wordlist.txt"
        
        print("Filtrando senhas do rockyou.txt...")
        
        # Conjunto para armazenar senhas únicas
        wifi_passwords = set()
        
        # Padrões comuns de senha WiFi
        wifi_patterns = [
            r'.*wifi.*',
            r'.*casa.*',
            r'.*home.*',
            r'.*router.*',
            r'.*admin.*',
            r'\d{8}',  # 8 dígitos
            r'.*2023.*',
            r'.*2024.*',
            r'.*pass.*'
        ]
        
        # Compilar padrões
        patterns = [re.compile(pattern, re.IGNORECASE) for pattern in wifi_patterns]
        
        # Ler rockyou.txt e filtrar senhas
        with open(input_file, 'r', encoding='latin-1', errors='ignore') as f:
            for line in f:
                password = line.strip()
                
                # Verificar se é uma senha válida para WiFi
                if is_valid_wifi_password(password):
                    # Verificar se corresponde a algum padrão comum de WiFi
                    if any(pattern.match(password) for pattern in patterns):
                        wifi_passwords.add(password)
        
        # Salvar senhas filtradas
        with open(output_file, 'w', encoding='utf-8') as f:
            for password in sorted(wifi_passwords):
                f.write(password + '\n')
        
        print(f"Processo concluído! {len(wifi_passwords)} senhas foram salvas em {output_file}")
        
    except FileNotFoundError:
        print("Erro: rockyou.txt não encontrado!")
        print("Por favor, coloque o arquivo rockyou.txt no mesmo diretório.")
    except Exception as e:
        print(f"Erro: {str(e)}")

if __name__ == "__main__":
    filter_rockyou() 