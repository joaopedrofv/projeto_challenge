
# menu
print("Bem Vindo ao menu da Sales Force!")
print("1- Produtos \n2- Industrias \n3- Aprendizado \n4- Suporte \n5- Empresa")

# variaveis de menu
menu = input("Selecione a opção desejada: ")

# Produto1
if menu == "1":
    print("1- Vendas \n2- Atendimento ao cliente \n3- Marketing \n4- Commerce \n5- Plataforma \n6- Sustentabilidade \n7- Especialistas e Apps de Parceiros \n8- Serviços e Planos")

    ServicoProdutos = input("Qual tipo de serviço: ")

    if ServicoProdutos == "1":
        print("1- Visão Geral \n2- Funcionalidades \n3- Ferramentas \n4- Preços")
    elif ServicoProdutos == "2":
        print( "1- Funcionalidades do Service Cloud \n2- Atendimento ao Cliente em Canais Digitais \n3- Vantagens Service Cloud: benefícios da plataforma \n4- Conceitos básicos \n5- Service Cloud: case de sucesso, histórias de cliente \n6- O que é atendimento ao cliente?")
    elif ServicoProdutos == "3":
        print(  "1- Marketing Cloud: plataforma de marketing digital \n2- Canais \n3- Produtos \n4- Account Engagement \n5- Edições e Preços \n6- Comece a Usar")
    elif ServicoProdutos == "4":
        print("1- Overview \n2- E-Commerce B2C: Plataforma Commerce Cloud \n3- Tudo sobre E-commerce \n4- Commerce Marketplace \n5-Comércio sem periféricos")
    elif ServicoProdutos == "5":
        print("1- Visão geral \n2- Soluções \n3- Infraestrutura \n4- Recursos \n5- Produtos \n6- App Cloud: APIs, Ferramentas e Serviços")
    elif ServicoProdutos == "6":
        print("1- Net Zero Cloud")
    elif ServicoProdutos == "7":
        print("""
  Especialistas & Apps de Parceiros

  Aproveite o Salesforce ao máximo com
  parceiros, apps, soluções e consultoria
  """)
    elif ServicoProdutos == "8":
        print("""
  Serviços e planos

  Cumpra seus objetivos com nossos
  parceiros e especialistas em sucesso do 
  cliente.
  """)
    else:
        print("Opção inválida")

    escolhaOpcao = input("Selecione a opção desejada: ")

    if escolhaOpcao == "1":
        print("""
    Reduza os custos e aumente a produtividade

    Eficiência máxima com automação, dados e inteligência 
    melhores. Como? Com automação da força de
    vendas impulsionada por IA.
        """)
    elif escolhaOpcao == "2":
        print("""
        Acelere o crescimento das vendas.

        Com o sistema de vendas da Salesforce, você pode 
        expandir suas contas, encontrar novos clientes e fechar 
        negócios com mais rapidez e de qualquer lugar.

        Feche mais negócios.

        Não importa o tamanho de sua empresa, todos os agentes de vendas
        têm uma meta em comum:o desejo de terem um desempenho superior.
        No entanto é difícil conseguir isso sozinho,e é por isso que nós 
        vamos ajudar você.
        """)
    elif escolhaOpcao == "3":
        print("""
        Amplie o poder do Sales Cloud com aplicações, opções e produtos inovadores.
        O Sales Cloud é a base para ter uma equipe de vendas mais ágil,
        produtiva e informada.Descubra como ir mais longe e dar a sua parte 
        em cada projeto.
        """)
    elif escolhaOpcao == "4":
        print("""
        Preços do Sales Cloud
        Venda mais rápido e com mais inteligência com qualquer uma das nossas edições 
        de CRM totalmente personalizáveis.

        Starter: Ferramentas de vendas e atendimento ao cliente em um app - $ 25
        Sales Professional: Solução de vendas completa para equipes de qualquer tamanho - $ 80
        Enterprise: CRM de vendas altamente personalizável para o seu negócio - $ 165
        Unlimited: A plataforma definitiva para seu crescimento - $ 330

        Todos planos cobrados anualmente!
        """)
    else:
        print("Opção inválida")

    if escolhaOpcao == "1":
        print("""
        Obtenha as ferramentas e recursos de atendimento ao cliente para ajudar
        seus agentes aprestar o melhor serviço possível.

        Veja todos os recursos, desde chat ao vivo até pesquisa em base de conhecimentos, 
        que tornam o Service Cloud a principal solução de suporte e atendimento ao cliente do mundo.
        """)
    elif escolhaOpcao == "2":
        print(""""
        Ofereça atendimento inteligente no canal, na hora e no momento que o cliente mais precisa.
        Esteja onde seus clientes estiverem com o Service Cloud Digital Engagement. 
        Alcance clientes em todos os canais digitais, incluindo mensagens móveis, chat na web,
        redes sociais e muito mais, para fornecer uma experiência de serviço perfeita em 
        todas as principais plataforma para serviço.
        """)
    elif escolhaOpcao == "3":
        print(""""
        AS VANTAGENS DA PLATAFORMA:

        Ofereça uma experiência inesquecível usando a plataforma de atendimento ao cliente
        mais completa do mundo.

        O Service Cloud está incorporado à plataforma mais ágil, confiável e inovadora que existe,
        disponibilizando todas as ferramentas de suporte necessárias para um bom atendimento ao cliente.
        """)
    elif escolhaOpcao == "4":
        print(""""
        Quando você estiver pronto para começar, estaremos aqui para ajudá-lo:

        Desde recursos de ajuda e treinamentos, passando por parceiros de tecnologia que podem
        acelerar a implementação e a integração, até centenas de aplicativos disponíveis no
        AppExchange: temos tudo de que você precisa para dar o primeiro passo com a Salesforce.

        Ajuda e treinamento:

        Quanto mais você souber, mais vai aproveitar a Salesforce. Temos uma ampla gama de recursos para
        ajudar você do início ao fim mais rapidamente. Desde webinários semanais e vídeos apresentando o
        que esperar em uma instalação típica até o acesso à experiência da Salesforce: você vai encontrar
        toda a ajuda de que precisa em um só lugar.

        Implementação e integração:

        Quando você tem o parceiro certo, a implementação e a integração são apenas itens em sua lista.
        Nossos parceiros estratégicos são escolhidos por suas experiências com centenas de empresas de diferentes
        tamanhos e setores. Então, não importa qual é o seu negócio, eles têm a experiência necessária para
        ajudar você a levantar voo.
        """)
    elif escolhaOpcao == "5":
        print(""""
        CASOS DE SUCESSO DE CLIENTES:
        As novas tecnologias criam mais interações com clientes humanos.

        *******************************************************************

        Descubra todas as formas de sucesso das empresas com o Salesforce.
        """)
    elif escolhaOpcao == "6":
        print(""""
        O que é atendimento ao cliente?

        Atendimento ao cliente é todo o suporte que você oferece aos seus clientes, seja antes, durante
        ou depois da compra, e que os ajuda a ter uma excelente experiência com a sua empresa.
        A definição de atendimento ao cliente vai muito além de apenas dar respostas: o conceito de
        atendimento é uma parte importantíssima do que a sua marca significa para os clientes,
        transformando-se em um fator crítico para o sucesso do seu negócio.

        Não importa se o seu objetivo é manter clientes ou gerar novos leads, é preciso ter qualidade no 
        atendimento ao cliente, que deve estar alinhado ao valor que sua empresa quer passar para os
        consumidores e as suas metas como um todo. Assim, você tem uma grande oportunidade de estar 
        em contato com seu target, impulsionar a gestão de relacionamento com o cliente e 
        demonstrar que está preocupado com ele.
        """)
    else:
        print("Opção inválida")

    if escolhaOpcao == "1":
        print(""""
        Faça cada momento valer a pena para alcançar o sucesso imediato
        Atraia clientes. Gere mais engajamento. Construa relações duradouras.
        Tudo isso graças ao marketing digital baseado em dados.
        """)
    elif escolhaOpcao == "2":
        print(""""
        Personalize as experiências dos clientes em todos os canais com o Marketing Cloud:

        ***************************************************************************************

        Email Studio:
        Personalize as mensagens de e-mail marketing enviadas através do Sales Cloud,do Service Cloud
        e de qualquer outra origem. Envie mensagens promocionais, transacionais. Aproveite os recursos
        poderosos de segmentação, automação e previsão e use as ferramentas de relatórios para acompanhar
        o desempenho.

        Mobile Studio:
        Impacte seus clientes no momento adequado com SMS, MMS, mensagens por push e mensagens em grupos e
        potencialize as estratégias de mobile marketing da sua empresa. Os envios podem ser baseados
        em eventos, localização, proximidade e outros fatores.

        Web Studio:
        Crie sites e landing pages com conteúdos personalizados. Acompanhe todas as ações dos seus
        clientes e faça análises de comportamento através das informações coletadas.

        Advertising Studio:
        Ativando os dados de clientes você alimenta as campanhas digitais e gerencia as campanhas
        publicitárias. Reforce a aquisição de clientes com públicos semelhantes, renove o 
        envolvimento com clientes inativos e otimize a publicidade durante a jornada do cliente.
        """)
    elif escolhaOpcao == "3":
        print(""""
        Email Studio
        Journey Builder
        Marketing Cloud Personalization 
        Marketing Cloud Customer Data Platform
        Marketing Cloud Intelligence
        Marketing Cloud Account Engagement
        """)
    elif escolhaOpcao == "4":
        print(""""
        Marketing Cloud Account Engagement:

        Impulsione o crescimento eficiente com alinhamento de marketing e vendas.
        """)
    elif escolhaOpcao == "5":
        print(""""
        Preços do Marketing Cloud:

        Envolva os clientes com as soluções de marketing alinhadas à sua estratégia.
        Unifique e conecte seus dados para permitir interações personalizadas.
        """)
    elif escolhaOpcao == "6":
        print("""
        Comece com tudo:
        Seja você um usuário iniciante do Marketing Cloud ou um usuário experiente com um
        novo produto, temos vários recursos para ajudá-lo a ser bem-sucedido.
        """)
    else:
        print("Opção Inválida")

# Industria2
elif menu == "2":
    print("1- Automotivos \n2- Comunicações \n3- Bens de Consumo \n4- Serviços Financeiros \n5- Sáude & Ciências da Vida \n6- Mídia \n7- Setor Público \n8- Varejo9- Tecnologia")
    ServicoIndustrias = input("Qual tipo de serviço: ")

    if ServicoIndustrias == "1":
        print("1-CRM Automotive gestão na nuvem do setor | SalesForce \n2-OEMs \n3-Revendedores \n4-Fornecedores \n5-Serviço de mobilidade")

    elif ServicoIndustrias == "2":
        print("1- Visão geral \n2- Perguntas frequentes")

    elif ServicoIndustrias == "3":
        print("1- Vestuário, calçados e acessórios \n2- Saúde e beleza \n3- Bens domésticos duráveis (BDR) \n4- Bens de consumo rápido")

    elif ServicoIndustrias == "4":
        print("1- Produtos \n2- Financial Services Cloud \n3- Operações bancárias \n4- Seguros \n5- Hipoteca e empréstimo \n6- Recursos \n7- Perguntas frequentes: O que é a nuvem de serviços financeiros?")

    elif ServicoIndustrias == "5":
        print("1- Health Cloud \n2- Pharma \n3- Soluções MedTech: melhore seus serviços de saúde \n4- Biotecnologia \n5- Recursos \n6- FAQ")

    elif ServicoIndustrias == "6":
        print("1- Visão geral \n2- Soluções")

    elif ServicoIndustrias == "7":
        print("1- Visão geral \n2- Soluções \n3- Produtos \n4- Preços")

    elif ServicoIndustrias == "8":
        print("1- Overview \n2- Soluções \n3- Moda \n4- Mercearias, farmácias e lojas de conveniência \n5- Atacadistas e Departamentos \n6- Restaurantes \n7- Recursos")

    elif ServicoIndustrias == "9":
        print("1- Visão geral")
    else:
        print("Opção inválida")


# Aprendizado3
elif menu == "3":
    print("1- Aprendizado no Trailhead \n2- Eventos e Experiências \n3- Blogs \n4- Por tópico \n5- Por tipo de conteúdo \n6- Por função \n7- Por indústria")

    ServicoAprendizado = input("Qual tipo de aprendizado: ")

    if ServicoAprendizado == "1":
        print("""
        Aprenda no Trailhead

        Desenvolva suas habilidades para o futuro 
        a partir de qualquer lugar com o Trailhead,
        nossa plataforma gratuita e online de ensino.
        """)
    elif ServicoAprendizado == "2":
        print("""
      Eventos & Experiências

      Participe de eventos virtuais da Salesforce.
      """)

    elif ServicoAprendizado == "3":
        print("""
      O 360 Blog

      Aprenda a se adiantar às tendências e 
      turbine seus relacionamentos profissionais.
      """)

    elif ServicoAprendizado == "4":
        print("""
      Por tópico

      Encontre produtos e recursos projetados 
      para ajudar todo mundo a se reunir de 
      forma segura e trabalhar a partir de qualquer local.
      """)

    elif ServicoAprendizado == "5":
        print("""
      Por tipo de Conteúdo

      Envolva-se com recursos especializados e 
      infinitos – em qualquer formato que você preferir.
      """)

    elif ServicoAprendizado == "6":
        print("""
      Por função

      Explore os recursos mais interessantes para 
      você, sua equipe e sua organização.
      """)

    elif ServicoAprendizado == "7":
        print("""
      Por indústria

      Descubra pesquisas, insights e soluções 
      feitos sob medida para sua empresa e sua indústria.
      """)
    else:
        print("Opção inválida")

# Suporte4
elif menu == "4":
    print("1- Ajuda e Documentação \n2- Comunidades \n3- Serviços e planos")

    ServicoSuporte = input("Qual tipo de serviço: ")

    if ServicoSuporte == "1":
        print("""
        Ajuda e documentação

        Precisando de ajuda? Registre casos, 
        encontre documentos e muito mais. 
        Receba todo o suporte que você precisar, a qualquer momento.
        """)
    elif ServicoSuporte == "2":
        print("""
        a colocar ainda
        """)
    elif ServicoSuporte == "3":
        print("""
        Serviços e planos

        Cumpra seus objetivos com nossos parceiros 
        e especialistas em sucesso do cliente.
        """)
    else:
        print("Opção inválida")


# Empresa5
elif menu == "5":
    print("1- Sobre a Sales Force \n2- Nossos valores \n3- Nosso Impacto \n4- Carreiras \n5- Notícias \n6- Mais Marcas da Sales Force")

    ServicoEmpresa = input("Qual tipo de serviço: ")

    if ServicoEmpresa == "1":
        print("""
        Sobre a Salesforce

        Descubra nossa história, nossos produtos e nossos valores.
        """)
    elif ServicoEmpresa == "2":
        print("""
        ofjhdaofhdafh
     """)
    elif ServicoEmpresa == "3":
        print("""
     Nosso impacto (Inglês)

     Nós sabemos que fazer negócios é a maior forma de gerar transformações.
     Veja como estamos construindo um futuro melhor.
     """)
    elif ServicoEmpresa == "4":
        print("""
     Carreiras (Inglês)

     Inicie uma nova jornada conosco. 
     Comece uma carreira aqui na Salesforce.
     """)
    elif ServicoEmpresa == "5":
        print("""
     Notícias

     Fique a par dos anúncios e notícias mais fresquinhos.
     """)
    elif ServicoEmpresa == "6":
        print("""
    a colocar ainda
     """)
    else:
        print("Opção inválida")
else:
    print("Opção inválida")
