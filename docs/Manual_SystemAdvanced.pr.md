



# SystemAdvanced
  
Módulo para ampliar funcionalidades da seção Sistema  

*Read this in other languages: [English](Manual_SystemAdvanced.md), [Português](Manual_SystemAdvanced.pr.md), [Español](Manual_SystemAdvanced.es.md)*
  
![banner](imgs/Modulo-System.jpg)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  


## Descrição do comando

### Exportar variáveis ​​para arquivo
  
Exportar variáveis ​​do Rocketbot para um arquivo
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Caminho do arquivo|Caminho e nome do arquivo onde as variáveis ​​serão salvas|C:/Usuário/Usuário/Pasta/arquivo.txt|

### Atribuir múltiplas variáveis
  
Atribua um valor a múltiplas variáveis ​​a partir de um objeto iterável.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Dato |Valor a ser definido||
|Atribuição de variáveis |As variáveis ​​a serem definidas devem ser separadas por vírgulas.|var1,var2,var|

### Fazer backup
  
Crie um novo backup
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |

### Limpar variável(is)
  
Insira as variáveis a serem limpas, separadas por vírgulas
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Variável|Variáveis ​​a serem limpas|Variável|

### Limpar variável(eis) por categoria
  
Insira a categoria de variáveis ​​a serem limpas.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Categoria|Nome da categoria à qual pertencem as variáveis ​​a serem limpas. Você pode adicionar várias categorias separadas por vírgulas.|Conexão|

### Aleatório
  
Comando para usar biblioteca aleatória
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Selecione o método|Método de biblioteca com o qual trabalhamos||
|Valor|Argumento para o método (random.randrange(argumento))|5,9|
|Variável|Variável onde o resultado será armazenado.|Variável|

### Aplicativo em destaque
  
Trazer um aplicativo para o primeiro plano
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Nome do aplicativo|Nome do aplicativo a ser trazido para o primeiro plano|test.xlsx - Excel|

### Obtenha o controle das janelas abertas.
  
Retorna uma lista com tuplas contendo o nome e o identificador das janelas abertas.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Variável|Variável onde o identificador será armazenado.|Variável|

### Contador
  
Retorna um número contador.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Variável|Variável onde o número será armazenado.|Variável|

### Obter argumentos
  
Ele recupera os argumentos fornecidos anteriormente ao iniciar o Rocketbot.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Argumentos necessários|Lista de argumentos obrigatórios separados por vírgulas..|['-start', 'id', '-db']|
|Atribua o resultado à variável|Variável onde o resultado do contador será armazenado.|Variável|

### Inicialize a(s) variável(eis) com o valor 0.
  
Insira as variáveis ​​que devem ser inicializadas com o valor 0, separadas por vírgulas.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Variável|Variáveis ​​a serem inicializadas com o valor 0.|Variável|
