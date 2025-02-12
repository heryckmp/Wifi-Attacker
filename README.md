# Wifi Attacker
> Desenvolvido por [Heryck](https://github.com/heryckmp)

Uma ferramenta avançada de teste de segurança para redes Wi-Fi usando comandos CMD e Python.

Este projeto é uma evolução do conceito original de brute force em redes Wi-Fi,
agora com recursos aprimorados de geração de wordlists e otimização de ataques.
Desenvolvido para fins educacionais e de teste de segurança, combina a simplicidade
do Batch com a potência do Python para criar uma ferramenta mais eficiente.

## Como Usar

### Inicialização da Interface
O programa detecta automaticamente suas interfaces wireless quando você executa o arquivo batch.
Se encontrar apenas uma, ela será selecionada como padrão. Se houver múltiplas interfaces,
o programa pedirá para você escolher uma. Se nenhuma existir, permanecerá como "not_defined".

> Você pode alterar a interface posteriormente digitando `interface` no menu principal.
> Isso trará a tela de inicialização da interface de volta.

### Scan
Quando você digita `scan` no menu principal, o programa listará todas as redes Wi-Fi
disponíveis na interface wireless selecionada. Você pode escolher uma digitando o número
associado ao SSID.

> "No Name" pode significar que a rede está oculta. Você não pode atacar essa rede.

> Realizar um scan desconecta a interface da rede à qual estava conectada anteriormente.

### Wordlist
Existem duas maneiras de gerar/atualizar a wordlist:

1. Usando o comando `filter`:
   - Coloque o arquivo rockyou.txt no diretório Source Code
   - Execute o comando `filter` para gerar wifi_wordlist.txt
   - Isso criará uma lista otimizada focada em senhas comuns de WiFi

2. Usando o comando `generate`:
   - Isso criará variações das senhas existentes
   - Útil para criar mais combinações de senhas

A wordlist padrão (wifi_wordlist.txt) será usada automaticamente se estiver presente.

### Ataque
Digite `attack` e o programa mostrará uma tela de aviso informando que este processo
irá deletar o perfil associado ao SSID se você já tiver se conectado a ele antes.
Isso significa que você perderá a senha que inseriu ao se conectar àquele SSID anteriormente.
Salve-a antes de usar o ataque.

### Contador
Quando uma conexão é tentada com `netsh` em uma rede, leva tempo para estabelecer a conexão.
Para verificar se a conexão foi bem-sucedida, o programa consulta repetidamente o status
da conexão da interface selecionada. Um valor de contador controla quantas vezes essa
consulta será feita. Se não for alterado, o valor do contador é 5 e diminui após cada
consulta para cada combinação de senha.

> Se uma autenticação for detectada, este valor é aumentado em 5 para garantir uma conexão bem-sucedida.

## Limitações
- Este programa foi testado sem sucesso no Windows 7 e testado com sucesso no Windows 10 e 11.
- Sequências de escape ANSI usadas no terminal foram adicionadas ao Console do Windows na versão 1511 do Windows 10.
- Há uma dependência estrita do utilitário de linha de comando `netsh`.
- A velocidade é significativamente lenta devido à sua natureza.
- Não pode atacar redes ocultas.

## Arquivo de Resultado
Se um ataque for bem-sucedido, o resultado é automaticamente escrito em `result.txt`.

## Tela de Ajuda
```txt
Comandos

 - help             : Mostra esta página
 - wordlist         : Fornece um arquivo de wordlist
 - scan             : Realiza um scan de WI-FI
 - interface        : Abre o Gerenciamento de Interface
 - attack           : Ataca o WI-FI selecionado
 - counter          : Define o contador de tentativas
 - generate         : Gera wordlist complexa
 - filter           : Filtra rockyou.txt para senhas WiFi
 - exit             : Fecha o programa

 Para mais informações, consulte "README.md".
```

## Sobre o Projeto

### Criador
Projeto desenvolvido e mantido por:
- **Heryck Morais Pina**
  - GitHub: [heryckmp](https://github.com/heryckmp)
  - Projeto: [Wifi-Attacker](https://github.com/heryckmp/Wifi-Attacker)

### Recursos Implementados:
1. Integração com Python para geração de wordlists mais eficientes
2. Suporte ao rockyou.txt com filtragem inteligente
3. Geração de variações de senha usando algoritmos avançados
4. Interface em português para melhor usabilidade
5. Otimização do processo de ataque e detecção de senhas
6. Sistema de log e registro de resultados

### Tecnologias Utilizadas:
- Batch Script (Windows CMD)
- Python 3.x
- Netsh (Windows Network Shell)
- Regex para filtragem de padrões
- Manipulação avançada de arquivos e strings

## Uso Ético e Legal
Esta ferramenta foi desenvolvida exclusivamente para:
- Fins educacionais e de pesquisa
- Testes de segurança autorizados
- Avaliação de vulnerabilidades em redes próprias

**AVISO:** O uso não autorizado desta ferramenta em redes de terceiros é ilegal
e pode resultar em consequências legais graves. O criador não se responsabiliza
pelo uso indevido do software.
