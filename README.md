# EigenFaces-Cats
Aplicando EigenFaces para faces de gatos

O PCA (Análise dos Componentes Principais) é uma técnica de redução de dimensionalidade não supervisionada que projeta os dados nas direções (ortogonais) de maior variância. Nesta aplicação, as imagens das faces dos gatos são transformadas em vetores e colocadas em uma matriz para aplicação do PCA. Os autovetores (vetores normalizados que representam a direção de projeção dos novos eixos) são os chamados "eigenfaces" e representam as maiores variações presentes nas imagens. Para este projeto, os dois primeiros e o últimos autovetores encontrados foram:

![Captura de tela 2021-11-19 095051](https://user-images.githubusercontent.com/88464241/142625746-a0331130-1d30-4d4b-a8b4-e1dd45c4b7c4.png)

Foram utilizados 10 autovetores, correspondendo a uma representação de 68.8% da variância total dos dados. Para obtenção de uma representação de ao menos 90% da variância total, seriam necessários 143 autovetores. Quanto maior a representação obtida, melhor a reconstrução da imagem, mas pra fins de teste na geração de novas imagens, foram mantidos os 10 autovetores.
Para geração, somamos a média das imagens com a projeção inversa através dos autovetores da nova dimensão para a dimensão anterior, o que seria neste caso de 10 dimensões para 4096 (imagens de 64x64). Uma GUI simples foi desenvolvida para visualização dos resultados:

![EigenFaces - Cats 2021-11-19 09-25-31](https://user-images.githubusercontent.com/88464241/142626796-51e937ef-fc2d-4dd8-b52f-6279dd27f80e.gif)

*É recomendado possuir uma base de dados "comportada" para aplicação de EigenFaces, ou seja, imagens sem variações excessivas de posição e formas. Esta base possui pouca variação e apresentou bons resultados utilizando apenas 5000 imagens.* 

Algumas infos dos dados e arquivos:
 - Fonte dos dados: https://www.kaggle.com/spandan2/cats-faces-64x64-for-generative-models
 - Arquivo *main.py*: transforma imagens, aplica PCA e salva a média (mean.npy) e os autovetores (eigenvectors.npy).
 - Arquivo *testing.py*: Exibe a GUI para criação de novas faces de gatos através da média e autovetores salvos.
 - Arquivo *cats_rgb.npy*: Arquivo numpy que reúne todas as imagens. Foi transformado para este formato pois é mais rápido para carregar e utilizar em outras plataformas, como google colab. *Não foi carregado no repositório por ultrapassar o peso permitido*.
