def check_keydown_events(event, ship):
    if event.key == pygame.K_RIGHT:
        # ship.rect.centerx += 10
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # ship.rect.centerx -= 10
        ship.moving_left = True

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False