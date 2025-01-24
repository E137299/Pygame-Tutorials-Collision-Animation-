# **Control Using Keyboard Input**
This method allows users to move an object by pressing keys on the keyboard.

### **How It Works**
- Pygame captures keyboard input through events or by checking which keys are currently being pressed.
- The object's position is updated based on the user's key presses.

### **Approaches**

#### **a) Using `pygame.KEYDOWN` and `pygame.KEYUP` Events**
- Detect when a key is pressed (`KEYDOWN`) or released (`KEYUP`).
- Update movement variables accordingly.

**Example:**
```python
import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()

# Object setup
rect = pygame.Rect(50, 50, 50, 50)  # x, y, width, height
speed = 5
velocity = [0, 0]  # Initial movement is stationary

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                velocity[0] = -speed
            elif event.key == pygame.K_RIGHT:
                velocity[0] = speed
            elif event.key == pygame.K_UP:
                velocity[1] = -speed
            elif event.key == pygame.K_DOWN:
                velocity[1] = speed
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                velocity[0] = 0
            elif event.key in [pygame.K_UP, pygame.K_DOWN]:
                velocity[1] = 0

    # Update object position
    rect.x += velocity[0]
    rect.y += velocity[1]

    # Draw everything
    screen.fill((0, 0, 0))  # Clear screen
    pygame.draw.rect(screen, (255, 0, 0), rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

#### **b) Using `pygame.key.get_pressed()`**
- Check the state of keys (whether they are pressed) continuously in each frame.
- Allows smooth movement without relying on events.

**Example:**
```python
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:
    rect.x -= speed
if keys[pygame.K_RIGHT]:
    rect.x += speed
if keys[pygame.K_UP]:
    rect.y -= speed
if keys[pygame.K_DOWN]:
    rect.y += speed
```

### **Key Points**
- `KEYDOWN` and `KEYUP` are event-driven and good for toggling movement.
- `key.get_pressed()` is continuous and better for fluid movement.

---

## **2. Control Using Mouse Input**
This method allows users to move an object using the mouse by detecting its position or button clicks.

### **How It Works**
- Pygame captures mouse input through events or by checking the mouse's position.
- The object's position or behavior is updated accordingly.

### **Approaches**

#### **a) Using `pygame.MOUSEBUTTONDOWN` and `pygame.MOUSEBUTTONUP` Events**
- Detect mouse button clicks and use them to control movement or set the object's position.

**Example:**
```python
for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:  # Left mouse button
            rect.center = event.pos
```

#### **b) Using `pygame.mouse.get_pos()`**
- Continuously track the mouse's position and update the object's position to follow the cursor.

**Example:**
```python
mouse_pos = pygame.mouse.get_pos()
rect.center = mouse_pos
```

