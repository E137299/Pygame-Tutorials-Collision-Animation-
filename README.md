# Pygame: Collision & Controlled Movement

Collision detection in Pygame is essential for game development to detect when objects (e.g., players, enemies, or projectiles) interact. Pygame provides several tools for detecting collisions between different shapes. Here's an overview:

---

### 1. **Rectangular Collision Detection**
   - Pygame provides the `pygame.Rect` class to represent rectangular areas.
   - **Methods:**
     - `colliderect(rect)`: Checks if two rectangles overlap.
     - `collidelist(list_of_rects)`: Checks if the rectangle collides with any rectangle in a list and returns the index.
     - `colliderectall(list_of_rects)`: Returns all rectangles that collide.
   - **Usage Example:**
     ```python
     player_rect = pygame.Rect(50, 50, 100, 100)
     enemy_rect = pygame.Rect(80, 80, 100, 100)
     
     if player_rect.colliderect(enemy_rect):
         print("Collision detected!")
     ```

---

### 2. **Pixel-Perfect Collision**
   - Pixel-perfect collision detection is used when you need to check collisions beyond bounding boxes (e.g., irregular shapes).
   - **`pygame.mask` Module:**
     - Masks allow checking collisions between non-rectangular shapes based on the transparency of pixels.
     - Masks are binary representations of objects where non-transparent pixels are "solid."
   - **Methods:**
     - `overlap(other_mask, offset)`: Detects overlap between two masks at a given offset.
   - **Usage Example:**
     ```python
     player_mask = pygame.mask.from_surface(player_image)
     enemy_mask = pygame.mask.from_surface(enemy_image)

     offset = (enemy_rect.x - player_rect.x, enemy_rect.y - player_rect.y)
     if player_mask.overlap(enemy_mask, offset):
         print("Pixel-perfect collision detected!")
     ```

---

### 3. **Circle Collision**
   - When objects are roughly circular, checking the distance between their centers is efficient.
   - **Formula:**
     ```python
     distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
     if distance < radius1 + radius2:
         print("Circle collision detected!")
     ```
   - **Usage Example:**
     ```python
     import math
     player_pos = (100, 100)
     enemy_pos = (150, 150)
     player_radius = 30
     enemy_radius = 30

     distance = math.sqrt((player_pos[0] - enemy_pos[0])**2 + (player_pos[1] - enemy_pos[1])**2)
     if distance < player_radius + enemy_radius:
         print("Circle collision detected!")
     ```

---

### 4. **Point-in-Rect Collision**
   - Check if a specific point lies inside a rectangle.
   - **Method:**
     - `collidepoint(x, y)`: Returns `True` if the point is inside the rectangle.
   - **Usage Example:**
     ```python
     point = (120, 120)
     if player_rect.collidepoint(point):
         print("Point is inside the rectangle!")
     ```



