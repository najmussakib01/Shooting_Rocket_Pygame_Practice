import pygame
from tensorflow.python.distribute.cluster_resolver.tpu.tpu_cluster_resolver import is_running_in_gce

pygame.init()

screen_size = pygame.display.set_mode((800, 800))
is_running = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False


