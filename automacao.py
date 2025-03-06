from preenchimento import preencher_contrato

dados_empresa = {
    "{{nome-contratante}}": "Empresa Exemplo LTDA",
    "{{rua-e-numero}}": "Rua das Flores, 123",
    "{{bairro}}": "Centro",
    "{{cep}}": "01010-000",
    "{{cidade-e-estado}}": "São Paulo - SP",
    "{{cnpj}}": "12.345.678/0001-90",
    "{{inicio-campanha}}": "01/03/2024",
    "{{fim-campanha}}": "30/06/2024",
    "{{data-atual}}": "28 de fevereiro de 2025",
    "{{nome}}": "João Silva",
    "{{cargo}}": "Diretor",
    "{{cpf}}": "123.456.789-00",
    "{{associacao}}": "Associação Comercial do Brasil",
    "{{nome-promocao}}": "Promoção de Aniversário",
    "{{telefone-fax}}": "(46) 99999-9999"
}

preencher_contrato(dados_empresa)
print("Contratos preenchidos com sucesso!")