from constants import BOX_WIGHT, BOX_HEIGHT


def nearest_neighbours(bacteries, meals):
    for bac1 in bacteries:
        min_distance1 = BOX_WIGHT * BOX_WIGHT + BOX_HEIGHT * BOX_HEIGHT
        min_distance2 = BOX_WIGHT * BOX_WIGHT + BOX_HEIGHT * BOX_HEIGHT
        if len(bacteries) > 1:
            for bac2 in bacteries:
                if bac2 == bac1:
                    continue
                dx = bac2.rect.centerx - bac1.rect.centerx
                dy = bac2.rect.centery - bac1.rect.centery
                dist = dx*dx + dy*dy
                if dist < min_distance1:
                    min_distance1 = dist
                    coord_x_target = bac2.rect.centerx  # координаты ближайшей к бак1 бактерии
                    coord_y_target = bac2.rect.centery
            bac1.neighbour[0][0] = min_distance1
            bac1.neighbour[1][0] = coord_x_target
            bac1.neighbour[2][0] = coord_y_target
        else:
            bac1.neighbour[0][0] = BOX_WIGHT * \
                BOX_WIGHT + BOX_HEIGHT * BOX_HEIGHT

        if len(meals) > 0:
            for meal in meals:
                dx = meal.rect.centerx - bac1.rect.centerx
                dy = meal.rect.centery - bac1.rect.centery
                dist = dx*dx + dy*dy
                if dist < min_distance2:
                    min_distance2 = dist
                    coord_x_target = meal.rect.centerx  # координаты ближайшей к бак1 бактерии
                    coord_y_target = meal.rect.centery
            bac1.neighbour[0][1] = min_distance2
            bac1.neighbour[1][1] = coord_x_target
            bac1.neighbour[2][1] = coord_y_target
        else:
            bac1.neighbour[0][1] = BOX_WIGHT * \
                BOX_WIGHT + BOX_HEIGHT * BOX_HEIGHT
