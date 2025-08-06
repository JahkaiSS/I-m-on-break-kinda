import pygame

pygame.init()

class Screen_settings:
    def __init__(self):
        self.screen_size = (500,500)
        self.bg_color = "red"
default_settings = Screen_settings()

font_num_1 = pygame.font.get_fonts()[88]
font_size_s = 32
my_font = pygame.font.SysFont(font_num_1, font_size_s, False, False)

BG_MUSIC_NAME = "this paper is crazy" + ".wav"
CURRENT_FOLDER = "sandboxPack"
LEFT_CLICK_SOUND_NAME = "left_up" + ".wav"
RIGHT_CLICK_SOUND_NAME = "right_up" + ".wav"
RESET_SOUND_NAME = "reset_sound" + ".wav"
bg_music = pygame.mixer.Sound(f"{CURRENT_FOLDER}/{BG_MUSIC_NAME}")
bg_music.play()


left_sound = pygame.mixer.Sound(f"{CURRENT_FOLDER}/{LEFT_CLICK_SOUND_NAME}")
right_sound = pygame.mixer.Sound(f"{CURRENT_FOLDER}/{RIGHT_CLICK_SOUND_NAME}")
reset_sound = pygame.mixer.Sound(f"{CURRENT_FOLDER}/{RESET_SOUND_NAME}")


screen = pygame.display.set_mode(default_settings.screen_size, pygame.RESIZABLE)
FPS = 144
clock = pygame.time.Clock()




def main(hasFuel):
    left_color_list = ["red","green","blue"]
    right_color_list = ["gray","orange","purple",(2,151,66),(255,0,36),(99,9,99)]
    left_color_index = 0
    right_color_index = 0
    bg_color = default_settings.bg_color
    displayed_key = ""
    hit_exit = False
    hit_escape = False
    hit_left_mouse = False
    hit_right_mouse = False
    left_sound_timer = 0
    left_sound_playing = False
    right_sound_timer = 0
    right_sound_playing = False
    any_sound_playing = False
    bg_music_volume = 1

    while hasFuel:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                displayed_key = "QUIT"
                hit_exit = True
            if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                displayed_key = pygame.key.name(event.key)
                hit_escape = True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                hit_right_mouse = False
                hit_left_mouse = True
                if left_color_index < len(left_color_list) - 1:  
                    left_color_index += 1
                else:
                    left_color_index = 0
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                hit_left_mouse = False
                hit_right_mouse = True
                if right_color_index < len(right_color_list) - 1:  
                    right_color_index += 1
                else:
                    right_color_index = 0
        
        bg_music.set_volume(bg_music_volume)
        if hit_left_mouse:
            bg_color = left_color_list[left_color_index]
            left_sound_playing = True
            hit_left_mouse = False
            left_sound_timer = 0
            
        if hit_right_mouse:
            bg_color = right_color_list[right_color_index]
            right_sound_playing = True
            hit_right_mouse = False
            right_sound_timer = 0

        if left_sound_playing:
            left_sound_timer += 1
            if left_sound_timer == 1:
                left_sound.play()
            if left_sound_timer == 200:
                left_sound_playing = False

        if right_sound_playing:
            right_sound_timer += 1
            if right_sound_timer == 1:
                right_sound.play()
            if right_sound_timer == 200:
                right_sound_playing = False

        any_sound_playing = left_sound_playing or right_sound_playing
            
            
        if any_sound_playing:
            bg_music_volume = 0.1
        else:
            bg_music_volume = 1
            

        


        
        if hit_exit or hit_escape:
            print(f"You exited the game via the {displayed_key} key")
            pygame.quit()
            exit()
        screen.fill(bg_color)

        displayed_index = my_font.render(f"{left_color_index},{right_color_index}",False,"white")
        screen.blit(displayed_index,[0,0])
        pygame.display.update()
        clock.tick(FPS)
    
main(True)
