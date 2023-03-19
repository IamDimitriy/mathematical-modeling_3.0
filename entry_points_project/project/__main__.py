import pygame
import sys
from bacanimal import Bacteria, Bacteriophage, Eat
from histogram import build_a_graph
from constants import *
import information_panel as inform
import pandas as pd
from nearest_neighbour import nearest_neighbours


def main(args=None):
    txt = None
    sec = 0
    timer_interval = 1000  # 1 seconds
    timer = pygame.USEREVENT + 1
    pygame.time.set_timer(timer, timer_interval)
    clock = pygame.time.Clock()
    data = []  # получение подробной статистики
    pygame.init()
    pygame.display.set_caption("Математическое моделирование")  # название
    pygame.display.set_icon(icon)  # иконка
    screen.blit(bg_image, (0, 0))
    for i in range(quantity_bac//2):  # бактерии без CRISPR/Cas
        resistb = 0.5
        immunityb = 0.5
        bac = Bacteria(resistb, immunityb, False, crispr_def, img_normal,  x=random.randrange(
            0, BOX_WIGHT-30), y=random.randrange(0, BOX_HEIGHT-30))
        all_sprites.add(bac)
        bacs.add(bac)
        non_crispr.add(bac)
        norm_bacs.add(bac)
        i += 1
    for i in range(quantity_bac//2):  # бактерии с CRISPR/Cas
        resistn = 0.5
        immunityn = 0.5
        bac = Bacteria(resistn, immunityn, True, crispr_def, img_normal,  x=random.randrange(
            0, BOX_WIGHT-30), y=random.randrange(0, BOX_HEIGHT-30))
        all_sprites.add(bac)
        bacs.add(bac)
        crispr_bacs.add(bac)
        norm_bacs.add(bac)
        i += 1
    for i in range(quantity_fac//3):  # фиолетовый вид фагов
        color = VIOLET
        fac = Bacteriophage(color, x=random.randrange(
            0, BOX_WIGHT-20), y=random.randrange(0, BOX_HEIGHT-20))
        all_sprites.add(fac)
        violet_facs.add(fac)
        i += 1
    for i in range(quantity_fac//3):  # красный вид фагов
        color = RED
        fac = Bacteriophage(color, x=random.randrange(
            0, BOX_WIGHT-20), y=random.randrange(0, BOX_HEIGHT-20))
        all_sprites.add(fac)
        red_facs.add(fac)
        i += 1
    for i in range(quantity_fac//3):  # желтый вид фагов
        color = YELLOW
        fac = Bacteriophage(color, x=random.randrange(
            0, BOX_WIGHT-20), y=random.randrange(0, BOX_HEIGHT-20))
        all_sprites.add(fac)
        yellow_facs.add(fac)
        i += 1
    for i in range(quantity_eat):  # еда
        x_eat = random.randrange(0, BOX_WIGHT-20)
        y_eat = random.randrange(0, BOX_HEIGHT-20)
        eat = Eat(color_eat, x_eat, y_eat)
        all_sprites.add(eat)
        eats.add(eat)
        i += 1
    run = True
    time = 0  # счётчик шагов моделирования

    while run:
        clock.tick(FPS)
        time += 1
        for event in pygame.event.get():
            if event.type == timer:
                sec += 1
                if sec >= 60:
                    min = (sec//60)
                    secs = sec - (min*60)
                    txt = "Время: %s мин %s сек" % (
                        str(int(min)), str(int(secs)))
                else:
                    txt = "Время:" + str(int(sec))
            if event.type == pygame.QUIT:
                run = False
                print(len(crispr_bacs), "crispr")
                print(len(non_crispr), "not crispr")
                print(len(inf_bacs), "inf")
                print(len(bacs) - len(inf_bacs), "not inf")
                df = pd.DataFrame(
                    data, columns=["with CRISPR/Cas", "no CRISPR/Cas"])  # передача данных для построения графика
                build_a_graph(df)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause(bacs, all_sprites)
        if (time % 10 == 0):  # парсим данные с частотой в секунду
            data.append([len(crispr_bacs), len(non_crispr)])
        if (time % 1 == 0):  # каждую итерацию спавним новую еду и фага
            x_eat = random.randrange(0, BOX_WIGHT-20)
            y_eat = random.randrange(0, BOX_HEIGHT-20)
            eat = Eat(color_eat, x_eat, y_eat)
            all_sprites.add(eat)
            eats.add(eat)
            color = random.choice(all_color)
            fac = Bacteriophage(color, x=random.randrange(
                0, BOX_WIGHT-20), y=random.randrange(0, BOX_HEIGHT-20))
            color = random.choice(all_color)
            if color == RED:
                all_sprites.add(fac)
                red_facs.add(fac)
            if color == YELLOW:
                all_sprites.add(fac)
                yellow_facs.add(fac)
            if color == VIOLET:
                all_sprites.add(fac)
                violet_facs.add(fac)
        nearest_neighbours(bacs, eats)
        screen.blit(bg_image, (0, 0))
        screen.blit(game_font.render(
            txt, True, txt_color), (0+5, BOX_HEIGHT-20))
        all_sprites.draw(screen)
        all_sprites.update()

        if 0:  # отрисовка круга чутья для каждой бактерии
            for bac in bacs:
                pygame.draw.circle(screen, (80, 80, 80),
                                   bac.rect.center, bac.sensitive, 1)
                # рендерим все спрайты на экране (аналогично фону)
                all_sprites.draw(screen)
        pygame.display.update()
        pygame.display.flip()  # отображаем всё, что нарендерили, на экране


def pause(bacs, all_sprites):  # пауза. Пробел - снять с паузы, p - поставить на паузу
    paused = True
    pygame.init()
    infos = pygame.sprite.Group()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()  # отслеживаем клик
                clicked_bacs = 0
                flag = False  # флаг нужен для удаления инф плашки по второму клику, иначе бы на месте удалённой создавалась новая
                for bac in bacs:
                    # если кликнули на бактерию, она она выделяется
                    if bac.rect.collidepoint(pos):
                        clicked_bacs = bac
                for info in infos:  # по второму клику удаляем табличку
                    if info.rect.collidepoint(pos):
                        info.kill()
                        screen.fill(BLACK)
                        all_sprites.draw(screen)
                        pygame.display.flip()
                        flag = True
                # блок вывода таблички с информацией о бактерии
                if clicked_bacs != 0 and flag == False:
                    clicked_bacs.image = pygame.image.load(
                        dir/"images"/"sprites"/"bacs"/"inf_bac.png")
                    info = inform.Info_panel(clicked_bacs, screen)
                    all_sprites.add(info)
                    all_sprites.draw(screen)
                    infos.add(info)
        if infos != 0:  # визуализируем текст
            for info in infos:
                info.vizualize_text(screen)
        pygame.display.update()
        clock.tick(15)
        pygame.display.flip()
    for info in infos:  # удаляем плашки
        info.kill()


if __name__ == "__main__":
    sys.exit(main())
