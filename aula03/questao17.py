'''Um dicionário Python pode ser usado para modelar um dicionário de verdade. No entanto, para evitar confusão,
chame este dicionário de glossário.
Pense em cinco palavras relacionadas à programação que você conhece.
Use estas palavras como chaves em seu glossário e armazene seus significados como valores.
Mostre cada palavra e seu significado em uma saída, formate a saída de uma forma bem elegante.
Por exemplo: você pode exibir a palavra seguida de dois-pontos e depois o seu significado,
ou apresentar a palavra em uma linha e então exibir seu significado identado em uma segunda linha.
Utilize o caractere de quebra de linha (\n) para inserir uma linha em branco entre cada palavra-significado em sua saída.
Sugestões de termos: Algoritmos, Python, Web Scraping, Lógica de Programação, Google Colab, Visual Studio Code.'''


glossario = {
    'Algoritmos': 'Um algoritmo é uma sequência de passos ou instruções bem definidas que são seguidas para resolver um problema ou executar uma tarefa. Os algoritmos podem ser expressos em diferentes formas, como texto, diagramas ou fluxogramas. Eles são utilizados em diversas áreas, como ciência da computação, matemática e engenharia, para resolver problemas de forma eficiente e sistemática.',
    'Web Scraping': 'Web scraping é o processo de extrair informações de websites de forma automatizada. Geralmente, é feito utilizando-se um programa ou script que acessa o conteúdo de uma página da web, analisa a estrutura do código HTML e extrai os dados relevantes. O web scraping é usado para coletar dados em larga escala, realizar monitoramento de preços, análise de mercado, pesquisa, entre outros fins.',
    'String': 'Em programação, uma string é uma sequência de caracteres. Ela pode ser composta por letras, números, símbolos ou espaços em branco. As strings são frequentemente utilizadas para armazenar e manipular texto em linguagens de programação. Em geral, as strings são tratadas como dados imutáveis, o que significa que qualquer alteração em uma string resulta em uma nova string.'
}

for i in glossario:
    print(f'{i.upper()}: \n\t{glossario[i]}')