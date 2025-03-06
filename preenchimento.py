import os
import sys
from docx import Document

def obter_caminho_recurso(relativo):
    """Retorna o caminho correto para um recurso, considerando execução normal ou como executável."""
    if getattr(sys, 'frozen', False):  
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    
    return os.path.join(base_path, relativo)

def preencher_contrato(dados_empresa, pasta_contratos=None, pasta_saida=None):
    """Preenche os modelos de contrato com os dados da empresa e salva os arquivos preenchidos."""

    if pasta_contratos is None:
        pasta_contratos = obter_caminho_recurso("contratos_templates")
    
    if pasta_saida is None:
        if getattr(sys, 'frozen', False):
            pasta_base = os.path.dirname(sys.executable)  
        else:
            pasta_base = os.path.dirname(os.path.abspath(__file__))  
        
        pasta_saida = os.path.join(pasta_base, "contratos_preenchidos")  

    os.makedirs(pasta_saida, exist_ok=True)  

    contratos = [
        "Procuração.docx",
        "Termo de adesão.docx",
        "Termo de mandatária.docx",
        "Termo de responsabilidade.docx"
    ]

    nome_contratante = dados_empresa.get("{{nome-contratante}}", "Sem_Nome")

    for contrato in contratos:
        caminho_contrato = os.path.join(pasta_contratos, contrato)

        if not os.path.exists(caminho_contrato):
            print(f"❌ Erro: Arquivo '{contrato}' não encontrado em '{pasta_contratos}'!")
            continue  

        try:
            doc = Document(caminho_contrato)

            for paragrafo in doc.paragraphs:
                for chave, valor in dados_empresa.items():
                    if chave in paragrafo.text:
                        paragrafo.text = paragrafo.text.replace(chave, valor)

            novo_nome = os.path.join(pasta_saida, f"{contrato.replace('.docx', '')}_{nome_contratante}.docx")
            doc.save(novo_nome)
            print(f"✅ Contrato preenchido salvo em: {novo_nome}")

        except Exception as e:
            print(f"⚠️ Erro ao preencher o contrato '{contrato}': {e}")

    return True