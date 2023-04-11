import pygame
import os
from tkinter.filedialog import askdirectory

#let the user to choose directory
def select_dir():
    path = askdirectory(title="Select Directory for music", initialdir=r"./music", mustexist=True)
    return path

global_path = select_dir()

#music list
def music_list_from_dir(screen, dirname):
    pass

#knopochki kliks
class ButtonsFun():
    isPaused = False
    def __init__(self, path, currentMusic, musicList):
        self.path = path + "/"
        self.currentMusic = currentMusic
        self.musicList = musicList
        self.musicListLength = len(musicList)

    def next(self):
        pygame.mixer.music.unload()
        pygame.mixer.music.load(self.path + self.musicList[(self.currentMusic+1)%self.musicListLength])
        pygame.mixer.music.play()
        self.currentMusic = self.currentMusic +1
        ButtonsFun.isPaused = False


    def pause(self):
        if not ButtonsFun.isPaused: 
            pygame.mixer.music.pause()
            ButtonsFun.isPaused = True
            # print("Paused")
        elif ButtonsFun.isPaused: 
            pygame.mixer.music.unpause()
            ButtonsFun.isPaused = False
            # print("Unpaused")

    def prev(self):
        pygame.mixer.music.unload()
        pygame.mixer.music.load(self.path + self.musicList[(self.currentMusic-1)%self.musicListLength])
        pygame.mixer.music.play()
        self.currentMusic = self.currentMusic - 1
        ButtonsFun.isPaused = False

myMusicList = os.listdir(global_path)
music = ButtonsFun(global_path, 1, myMusicList)

pygame.init()
width = 600
lenght = 600
screen = pygame.display.set_mode((width, lenght))
pygame.display.set_caption("MusicPlayer")
done = False
font = pygame.font.SysFont("AndaleMono", 32)

clock = pygame.time.Clock()

music.prev()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                music.pause()
            elif event.key == pygame.K_LEFT:
                music.prev()
            elif event.key == pygame.K_RIGHT:
                music.next()

    screen.fill((255,255,255))
    text = font.render(myMusicList[music.currentMusic%music.musicListLength], True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (width// 2, lenght // 2)
    screen.blit(text, textRect)
    pygame.display.flip()