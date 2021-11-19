import numpy as np
import pickle
import glob
import cv2
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

'''
# Aplicando técnica EigenFaces na face de gatos
Algumas fontes de pesquisa:

https://www.youtube.com/watch?v=_lY74pXWlS8&list=PLye4FtK3gI1Szyc_i8ygGVDiQqV_c0o6j&index=90
https://medium.com/@williangp/reconhecimento-de-padr%C3%B5es-eigenfaces-e4cef8f04919

'''

def adapta_imagem(img, shape, max_val=1):
    '''
    Função que adapta a imagem para o range e o tipo correto.
    '''
    img = (img - img.min())/(img.max() - img.min())
    
    if max_val > 1:
        img *= max_val
        return img.reshape(shape).astype(np.uint8)
    
    else:
        return img.reshape(shape)


# Carregando as imagens -> Utilizando apenas 5000 imagens [mais rápido/leve]
images = np.load('cats_rgb.npy')[:5000]

# Transformando as imagens em vetores. Na matriz resultante, cada linha é uma imagem e as colunas os respectivos pixels
images = np.array([file.flatten() for file in images])

# Visualizando uma imagem exemplo
plt.figure()
plt.imshow(images[5].reshape(64,64,3), cmap='gray')
plt.show()

# Obtendo e visualizando a média das imagens
mean_img = np.mean(images, axis=0)

plt.figure()
plt.imshow(adapta_imagem(mean_img, (64, 64, 3), 255))
plt.show()

# Padronizando o valor dos pixels das imagens [Pré-processamento para PCA]
scaler = StandardScaler()
images = scaler.fit_transform(images)

# Instanciando, adaptando o PCA e obtendo os autovetores. Aqui são escolhidos 10 autovetores, mas o ideal
# para se obter 90% de representação total da variância é de 143 autovetores. Para 10 autovetores, obtém-se 68.89%.
pca = PCA(n_components=10)
imgs_pca = pca.fit_transform(images) 
autovetores = pca.components_ # Autovetores

print(autovetores.shape)
print(f"Total da variância representada pelos componentes/autovetores: {pca.explained_variance_ratio_.sum()*100}[%]")

# Visualizando os três primeiros autovetores e o último
plt.figure()
plt.subplot(221)
plt.imshow(adapta_imagem(autovetores[0], (64, 64, 3), 255), cmap='gray')
plt.subplot(222)
plt.imshow(adapta_imagem(autovetores[1], (64, 64, 3), 255), cmap='gray')
plt.subplot(223)
plt.imshow(adapta_imagem(autovetores[2], (64, 64, 3), 255), cmap='gray')
plt.subplot(224)
plt.imshow(adapta_imagem(autovetores[-1], (64, 64, 3), 255), cmap='gray')
plt.show()

# Salvando a média e os autovetores
np.save('eigenvectors.npy', autovetores)
np.save('mean.npy', mean_img)