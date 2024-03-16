# -*- coding: utf-8 -*-
'''

Esse arquivo contém algumas funções que podem ajudar você a 
fazer o EP06, para criar um vídeo a partir da classe NumPymagem.

Você não deve entregar esse arquivo junto com o seu EP.
'''

import pygame as pg
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ========================================================================

def converta_3c(imgs, normaliza=False):
    ''' (list, bool) -> list
    recebe uma lista com NumPymagens com 1 canal e retorna uma 
    lista com np.arrays com 3 canais necessários para o PyGame.
    '''
    saida = []
    # w, h = imgs[0].data.shape
    h, w = imgs[0].data.shape 
    if normaliza:
        vmax = max( [img.data.max() for img in imgs] )

    for img in imgs:
        if normaliza:
            img = 255 * (img.data / vmax)
        ret = np.empty((w, h, 3), dtype=np.uint8)
        ret[:, :, 2] = ret[:, :, 1] = ret[:, :, 0] = np.rot90(np.flipud(img.data),3)
        saida.append( ret ) 
    return saida

# ========================================================================

def mostre_video( video ):
    ''' (list) -> None  
    recebe uma lista de objetos NumPymagem e exibe um vídeo
     a partir das imagens.
    '''

    imgs = converta_3c(video)
    fim = len(video)
    frame = 0

    nlin, ncol, depth = imgs[0].shape
    print("Video com altura %d e largura %d\n"%(nlin, ncol))

    pg.init()
    screen = pg.display.set_mode( (nlin, ncol) )
    clock = pg.time.Clock()    
    
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        surface = pg.surfarray.make_surface( imgs[frame] )
        screen.blit(surface, (0, 0))        
        pg.display.flip()

        frame = (frame+1) % fim
        clock.tick(60)
    pg.quit()

# ========================================================================
def converta_1c( numpymagens ):
    ''' (list) -> list
    recebe uma lista de numpymagens e retorna uma lista de imagens
    (arrays de Numpy) prontas para serem animadas.
    '''
    npimgs = []
    for img in numpymagens:
        npimgs.append( [plt.imshow( img.data, cmap='gray', vmin=0, vmax=255, animated=True)] )
    return npimgs

# ========================================================================

def salve_video( numpymagens, interval=50, blit=True, repeat_delay=1000 ):
    ''' (list) -> None
    Recebe uma lista de numpymagens em numpymagens
    e cria e mostra uma animação dessas numpymagens.
    '''
    fig = plt.figure()
    npimgs = converta_1c( numpymagens )
    ani = animation.ArtistAnimation(fig, npimgs, interval, blit, repeat_delay)
    
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps = 30, metadata=dict(artist='ep'), bitrate=1800)
    ani.save('video_do_meu_ep.mp4', writer=writer)

# ========================================================================
