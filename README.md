# Wifi Attacker
> Desenvolvido por [Erick Moreira](https://github.com/heryckmp)

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
Para gerar a wordlist otimizada:
1. Coloque o arquivo rockyou.txt no diretório Source Code
2. Execute o comando `filter` para gerar wifi_wordlist.txt
3. O script irá criar uma lista otimizada focada em senhas comuns de WiFi

A wordlist gerada (wifi_wordlist.txt) será usada automaticamente se estiver presente.
Você também pode fornecer sua própria wordlist usando o comando `wordlist`.

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
 - filter           : Filtra rockyou.txt para senhas WiFi
 - exit             : Fecha o programa

 Para mais informações, consulte "README.md".
```

## Sobre o Projeto

### Criador
Projeto desenvolvido e mantido por:
- **Erick Moreira**
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

## Tutorial Detalhado: Configurando a Wordlist

### 1. Obtendo o rockyou.txt
O rockyou.txt é uma das wordlists mais famosas para testes de penetração. Para usá-la:

1. Baixe o arquivo rockyou.txt (disponível em repositórios de pentest)
2. O arquivo original tem cerca de 14 milhões de senhas (~133MB)
3. Coloque o arquivo na pasta "Source Code" do projeto

### 2. Usando o Comando Filter
O comando `filter` foi desenvolvido para criar uma wordlist otimizada para WiFi:

1. Abra o programa executando `bruteforcer.cmd`
2. Digite `filter` no menu principal
3. O script irá:
   - Ler o arquivo rockyou.txt
   - Filtrar apenas senhas válidas para WiFi (8-63 caracteres)
   - Selecionar senhas que correspondam a padrões comuns como:
     * Contém "wifi", "casa", "home"
     * Números de 8 dígitos
     * Anos atuais (2023, 2024)
     * Palavras como "admin", "pass", "router"
   - Criar o arquivo wifi_wordlist.txt com as senhas filtradas

### 3. Processo de Filtragem
O script wifi_rockyou_filter.py aplica os seguintes critérios:

1. **Validação de Tamanho**
   - Mínimo: 8 caracteres (requisito WPA/WPA2)
   - Máximo: 63 caracteres (limite WiFi)

2. **Validação de Caracteres**
   - Apenas caracteres ASCII imprimíveis
   - Remove caracteres especiais inválidos

3. **Padrões de Senha WiFi**
   ```python
   Padrões incluídos:
   - .*wifi.*     (exemplo: mywifi123)
   - .*casa.*     (exemplo: casa2023)
   - .*home.*     (exemplo: home1234)
   - .*router.*   (exemplo: router123)
   - .*admin.*    (exemplo: admin2024)
   - \d{8}       (exemplo: 12345678)
   - .*2023.*    (exemplo: wifi2023)
   - .*2024.*    (exemplo: pass2024)
   - .*pass.*    (exemplo: password123)
   ```

### 4. Resultado
- O arquivo wifi_wordlist.txt será gerado na pasta "Source Code"
- Apenas senhas relevantes para WiFi serão incluídas
- O programa usará automaticamente esta lista otimizada
- O arquivo de resultado (result.txt) será criado se uma senha for encontrada

### 5. Dicas de Uso
- Execute o `filter` antes de iniciar um ataque
- Aguarde a conclusão do processo de filtragem
- Verifique se wifi_wordlist.txt foi criado
- Use o comando `attack` para iniciar o teste
- O contador pode ser ajustado com o comando `counter`

### 6. Exemplo de Fluxo de Trabalho
```bash
1. Coloque rockyou.txt na pasta Source Code
2. Execute bruteforcer.cmd
3. Digite 'filter' para gerar wifi_wordlist.txt
4. Digite 'interface' para selecionar interface WiFi
5. Digite 'scan' para encontrar redes
6. Selecione a rede alvo
7. Digite 'attack' para iniciar
```

### 7. Observações Importantes
- O processo de filtragem pode levar alguns minutos
- O arquivo rockyou.txt original não será modificado
- A lista filtrada será muito menor que a original
- Senhas mais prováveis serão testadas primeiro
- O processo é totalmente automatizado
