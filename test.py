# Bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/bullet.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        self.rect.y -= 5  # Move bullet upwards
        if self.rect.bottom < 0:
            self.kill()  # Remove bullet if it goes off-screen
        if pygame.sprite.spritecollide(self, alien_group, True):
            self.kill()  # Remove bullet on collision with alien
            explosion_fx.play()  # Play explosion sound
            explosion = Explosion(self.rect.centerx, self.rect.centery, 2)
            explosion_group.add(explosion)  # Add explosion effect
