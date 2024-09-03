"""
    MÓDULOS EXTERNOS DO PYTHON >> Agora, vamos explorar os pacotes externos do Python! Utilizaremos o
                                  pip, a ferramenta padrão de gerenciamento de pacotes do Python, para
                                  instalar e gerenciar pacotes externos, desde bibliotecas científicas
                                  até ferramentas de desenvolvimento web. Você aprenderá a acessar e
                                  utilizar diversos recursos para aprimorar seus projetos e ampliar suas
                                  habilidades de programação, além de criar seus próprios módulos

    USANDO PACOTES EXTERNOS >> Além dos módulos fornecidos de forma integrada pela biblioteca padrão do
                               Python, a linguagem possui uma grande vantagem: sua característica
                               open-source permite que qualquer desenvolvedor, com o conhecimento
                               adequado, desenvolva a própria biblioteca e os próprios módulos, os quais
                               chamaremos, a partir de agora, de pacotes. Veremos como criar módulos
                               mais adiante neste conteúdo
    
    PARA DAR CONTINUIDADE É NECESSÁRIO TER O 'PIP' E O 'PACH' INSTALADO EM SEU COMPUTADOR
        pip >> Um programa do Python que instala os pacotes externos para a nossa máquina

    
    AMBIENTE VIRTUAL >> Antes de instalarmos nossas bibliotecas externas, é importante criar um ambiente virtual antes de tudo, para não dar erro posteriormente... Ou caso queira usar versões diferentes de bibliotecas em seu projeto... Basicamente, o ambiente virtual cria um local na memória serarado do ambiente global, onde estão nossos módulos internos...
        - Criando o Ambiente virtual
            * COMANDO CRIAÇÃO: python venv env
                - Onde 'env' é o nome do ambiente virtual
            * COMANDO PARA ATIVAR: env\Scripts\activate
                - Onde 'env' é o nome do ambiente virtual
            * COMANDO DESATIVAÇÃO: deactivate

    USANDO O PIP PARA INSTALAÇÃO DE PACOTYES EXTERNOS:
        COMANDO: pip intall <nome do pacote externo>

    Usando pacotes externos                                   
        * VAMOS TRATAR DE ALGUNS:
            - numpy >> Serve para cálculos, operações matemáticas e simulações
            - pandas >> Serve para manipulação de dados
            - scikit-learn >> Serve para modelos de aprendizado de máquina
            - matplotlib >> Serve para visualização de dados
            - requests >> Biblioteca de comandos de comunicação pelo protocolo HTTP
            - flask >> Construção de aplicações web
            - DJango >> Construção de aplicações web
    
            
    EXTRA:
        - Os desenvolvedores podem criar os próprios módulos de forma a reutilizar as funções que já
        escreveram e organizar melhor seu trabalho. Para isso, basta criar um arquivo .py e escrever
        nele suas funções. O arquivo do módulo precisa estar na mesma pasta do arquivo para onde ele
        será importado.
"""

# Não iremos instalar, mas farei uma pastaexplicando a base de todos eles...