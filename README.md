Como a AutoDoc funciona?

Pasta build
A pasta build é criada pelo PyInstaller durante o processo de empacotamento de um script Python em um executável. Ela contém arquivos temporários e intermediários gerados durante a compilação e construção do executável.

Pasta dist
A pasta dist é criada pelo PyInstaller após o processo de empacotamento de um script Python em um executável. Ela contém o executável final gerado, pronto para ser distribuído e executado em um sistema compatível, sem a necessidade de instalar o Python ou as dependências do projeto.

Arquivo interface.spec 
O arquivo interface.spec é um arquivo de configuração gerado pelo PyInstaller quando você empacota um script Python pela primeira vez. Ele contém instruções e parâmetros que o PyInstaller usa para controlar o processo de empacotamento. Esse arquivo é criado automaticamente, mas você pode editá-lo para personalizar o comportamento do PyInstaller.

Arquivo automação.py
Este código é um script Python que preenche modelos de documentos Word (.docx) com dados de uma empresa e salva os arquivos preenchidos em uma pasta de saída. Ele foi projetado para funcionar tanto durante o desenvolvimento (quando executado como script) quanto quando empacotado como um executável (usando PyInstaller). 

Arquivo preenchimento.py
Este código usa a função preencher_contrato para preencher modelos de contrato com os dados de uma empresa, substituindo placeholders por valores reais. Ele é útil para automatizar a geração de documentos personalizados.

Arquivo interface.py
Este código cria uma interface gráfica usando a biblioteca tkinter para preencher contratos automaticamente. Ele coleta dados de entrada do usuário, valida esses dados e, em seguida, chama a função preencher_contrato (importada do módulo preenchimento) para gerar os contratos preenchidos.

Como usar a automação?
Na pasta dist você encontrará 1 pasta (contratos_preenchidos) e um arquivo .exe (nosso executável). Clicando em interface.exe, você verá a interface da automação, de fácil entendimento. Após preencher os campos, clique no botão gerar contratos, isso fará com que seus documentos sejam gerados na pasta contratos_preenchidos.
Essa automação está configurada para o meu uso no trabalho, caso tenha interesse em utilizar, faça os ajustes necessários, como trocar os templates de documentos e suas variáveis, não se esqueça também de fazer ajustes no código!
