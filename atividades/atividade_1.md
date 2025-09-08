## Atividade 1

* Explique, com suas palavras, o que é machine learning?

Machine learning é um campo da inteligência artificial que se concentra no desenvolvimento de algoritmos e modelos que permitem as máquina aprenderem a partir de dados, seja eles rotulados ou não, identificando padrões e fazendo previsões ou classificações.

* Explique o conceito de conjunto de treinamento, conjunto de validação e
conjunto de teste em machine learning.

O conjunto de treinamento é o conjunto de dados usado para treinar o modelo de machine learning, onde o modelo aprende os padrões nos dados. O conjunto de validação é um subconjunto dos dados que não é usado durante o treinamento, mas sim para ajustar os hiperparâmetros do modelo e avaliar seu desempenho durante o processo de desenvolvimento. O conjunto de teste é um conjunto de dados separado que é usado para avaliar o desempenho final do modelo após o treinamento e a validação, informando o quão bem seu modelo está performando.

* Explique como você lidaria com dados ausentes em um conjunto de dados
de treinamento.

Existem algumas maneiras de lidar com dados ausentes em um conjunto de dados de treinamento. Algumas abordagens que eu já usei , foram:
  - Remover linhas ou colunas com dados ausentes, se a quantidade de dados ausentes for pequena.
  - Imputar valores ausentes usando a média, mediana ou moda dos valores existentes na coluna.
  - Dividir os dados, caso o valor ausente tenha um significado específico, como por exemplo ele ser a tag alvo para previsão. Você pode dividir ele em dois datasets, os que possuem valor e os que não possuem, treinar com os que possuem e testar nos que não.

* O que é uma matriz de confusão e como ela é usada para avaliar o
desempenho de um modelo preditivo?

Uma matriz de confusão é uma tabela que é usada para avaliar o desempenho de um modelo de classificação. Ela mostra as previsões do modelo em relação aos valores reais, permitindo que você veja quantas previsões foram corretas e quantas foram incorretas. A matriz de confusão é composta por quatro elementos principais: verdadeiros positivos (TP), falsos positivos (FP), verdadeiros negativos (TN) e falsos negativos (FN).

* Em quais áreas (tais como construção civil, agricultura, saúde, manufatura,
entre outras) você acha mais interessante aplicar algoritmos de machine
learning?

Na área da saúde, para diagnóstico de doenças e análise de imagens médicas.