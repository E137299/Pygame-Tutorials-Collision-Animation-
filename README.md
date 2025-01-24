# Pygame: Collision & Controlled Movement

Collision detection in Pygame is essential for game development to detect when objects (e.g., players, enemies, or projectiles) interact. Pygame provides several tools for detecting collisions between different shapes. Here's an overview:

---

### **1. `colliderect()`**
- **Purpose**: Checks if two rectangles overlap (collide) by comparing their coordinates and dimensions.
- **Method**: A method of `pygame.Rect` objects.
- **Syntax**:
  ```python
  rect1.colliderect(rect2)
  ```
- **Parameters**:
  - `rect2`: Another `pygame.Rect` object.
- **Return Value**:
  - Returns `True` if the two rectangles intersect; otherwise, returns `False`.
- **Example**:
  ```python
  import pygame

  rect1 = pygame.Rect(50, 50, 100, 100)
  rect2 = pygame.Rect(75, 75, 100, 100)
  rect3 = pygame.Rect(200, 200, 50, 50)

  print(rect1.colliderect(rect2))  # True (they overlap)
  print(rect1.colliderect(rect3))  # False (no overlap)
  ```

---

### **2. `spritecollide()`**
- **Purpose**: Detects collisions between a single sprite and a group of sprites.
- **Method**: A function from the `pygame.sprite` module.
- **Syntax**:
  ```python
  pygame.sprite.spritecollide(sprite, group, dokill, collided=None)
  ```
- **Parameters**:
  1. **`sprite`**: A single `Sprite` object to test for collisions.
  2. **`group`**: A `Group` of sprites to check against the `sprite`.
  3. **`dokill`**: A boolean indicating whether colliding sprites in the `group` should be removed (`True`) or kept (`False`).
  4. **`collided`** (Optional): A callback function for custom collision detection. Defaults to checking if `sprite.rect` overlaps with the `rect` of sprites in the `group`.
     - The function should accept two arguments (the `sprite` and a member of the `group`) and return `True` or `False`.

- **Return Value**:
  - Returns a list of all sprites in the `group` that collided with the `sprite`.
  - If no collisions occur, returns an empty list (`[]`).

- **Example**:
  ```python
  import pygame

  # Define a sprite
  player = pygame.sprite.Sprite()
  player.rect = pygame.Rect(50, 50, 50, 50)

  enemy1 = pygame.sprite.Sprite()
  enemy1.rect = pygame.Rect(50, 50, 50, 50)

  enemy2 = pygame.sprite.Sprite()
  enemy2.rect = pygame.Rect(200, 200, 50, 50)

  enemies = pygame.sprite.Group(enemy1, enemy2)

  # Basic collision detection
  collisions = pygame.sprite.spritecollide(player, enemies, False)
  print("Colliding sprites:", collisions)  # Output: [enemy1]

  # With dokill=True
  collisions = pygame.sprite.spritecollide(player, enemies, True)
  print("Colliding sprites removed:", collisions)  # Removes enemy1 from the group

  # Custom collision function (circular collision)
  def circular_collision(s1, s2):
      distance = pygame.math.Vector2(s1.rect.center).distance_to(s2.rect.center)
      radius1 = s1.rect.width / 2
      radius2 = s2.rect.width / 2
      return distance < (radius1 + radius2)

  collisions = pygame.sprite.spritecollide(player, enemies, False, collided=circular_collision)
  print("Colliding sprites (circular):", collisions)
  ```

---

### **3. `collidepoint()`**
- **Purpose**: Checks if a point (x, y) lies within a rectangle.
- **Method**: A method of `pygame.Rect` objects.
- **Syntax**:
  ```python
  rect.collidepoint(x, y)
  rect.collidepoint((x, y))
  ```
- **Parameters**:
  - `x, y`: Coordinates of the point to check.
- **Return Value**:
  - Returns `True` if the point is inside the rectangle; otherwise, returns `False`.
- **Example**:
  ```python
  import pygame

  rect = pygame.Rect(50, 50, 100, 100)
  print(rect.collidepoint(60, 60))  # True (inside the rectangle)
  print(rect.collidepoint(10, 10))  # False (outside the rectangle)
  ```

---

### **4. `collidemask()`**
- **Purpose**: Checks for pixel-perfect collisions between two sprites using their masks.
- **Method**: A method of `pygame.sprite.Sprite`.
- **Requirements**:
  - Sprites must have a `mask` attribute, typically created using `pygame.mask.Mask`.
  - Masks define the areas of a sprite considered "solid" for collisions.
- **Syntax**:
  ```python
  sprite1.collidemask(sprite2)
  ```
- **Parameters**:
  - `sprite2`: Another `Sprite` object with a `mask` attribute.
- **Return Value**:
  - Returns a tuple `(x_offset, y_offset)` if the masks collide.
  - Returns `None` if there is no collision.
- **Example**:
  ```python
  import pygame

  # Initialize Pygame
  pygame.init()

  # Create surfaces and masks
  surface1 = pygame.Surface((100, 100), pygame.SRCALPHA)
  surface2 = pygame.Surface((100, 100), pygame.SRCALPHA)

  # Draw shapes on surfaces
  pygame.draw.circle(surface1, (255, 255, 255, 255), (50, 50), 40)
  pygame.draw.circle(surface2, (255, 255, 255, 255), (70, 70), 40)

  # Create masks from surfaces
  mask1 = pygame.mask.from_surface(surface1)
  mask2 = pygame.mask.from_surface(surface2)

  # Create sprites
  sprite1 = pygame.sprite.Sprite()
  sprite1.rect = surface1.get_rect(topleft=(0, 0))
  sprite1.mask = mask1

  sprite2 = pygame.sprite.Sprite()
  sprite2.rect = surface2.get_rect(topleft=(20, 20))
  sprite2.mask = mask2

  # Check for mask collision
  collision = sprite1.mask.overlap(sprite2.mask, (sprite2.rect.x - sprite1.rect.x, sprite2.rect.y - sprite1.rect.y))
  print("Collision:", collision)  # Output: (x_offset, y_offset) if collision occurs
  ```

---

### Summary Table:

| Function       | Purpose                                         | Usage Example                                   |
|----------------|-------------------------------------------------|------------------------------------------------|
| `colliderect()`| Checks if two rectangles overlap.               | `rect1.colliderect(rect2)`                    |
| `spritecollide()`| Checks collisions between a sprite and a group.| `pygame.sprite.spritecollide(sprite, group, dokill)` |
| `collidepoint()`| Checks if a point is inside a rectangle.        | `rect.collidepoint(x, y)`                     |
| `collidemask()`| Pixel-perfect collision between two sprites.    | `sprite1.collidemask(sprite2)`                |

