#!/usr/bin/env python3
import sys

# Define substituições simples
substitutions = {
    'a': ['@', '4'],
    'e': ['3'],
    'i': ['1', '!'],
    'o': ['0'],
    's': ['$', '5']
}

def generate_variants(password):
    variants = set([password])
    for i, ch in enumerate(password.lower()):
        if ch in substitutions:
            new_variants = set()
            for variant in variants:
                for sub in substitutions[ch]:
                    # Cria uma variante substituindo o caractere na posição i
                    new_variant = variant[:i] + sub + variant[i+1:]
                    new_variants.add(new_variant)
            variants.update(new_variants)
    return variants


def main():
    input_file = "wordlist.txt"  # Pode ser alterado para "complex_wordlist.txt" se preferir
    output_file = "complex_wordlist.txt"
    all_variants = set()
    try:
        with open(input_file, "r") as f:
            for line in f:
                pwd = line.strip()
                if pwd:
                    all_variants.update(generate_variants(pwd))
    except Exception as err:
        print("Erro ao ler", input_file, ":", err)
        sys.exit(1)

    try:
        with open(output_file, "w") as f:
            for pwd in sorted(all_variants):
                f.write(pwd + "\n")
        print(f"Gerado {output_file} com {len(all_variants)} senhas.")
    except Exception as err:
        print("Erro ao escrever", output_file, ":", err)
        sys.exit(1)


if __name__ == "__main__":
    main() 