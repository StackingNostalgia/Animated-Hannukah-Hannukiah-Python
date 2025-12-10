import os
import time
import random

RESET = "\033[0m"
GOLD = "\033[33m"
BRIGHT_YELLOW = "\033[93m"
YELLOW = "\033[33m"
RED = "\033[31m"
ORANGE = "\033[38;5;208m"

FLAME_COLORS = [BRIGHT_YELLOW, YELLOW, ORANGE, RED]

FLAME_CHARS = [' ', '.', ',', '\'', '^', '*', '@']

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

chanukiah_template = [
"                         (F)                         ",
" (F)   (F)   (F)   (F)   |~|   (F)   (F)   (F)   (F) ",
" |~|   |~|   |~|   |~|   |:|   |~|   |~|   |~|   |~| ",
" |:|   |:|   |:|   |:|   |:|   |:|   |:|   |:|   |:| ",
" |:|   |:|   |:|   |:|   |:|   |:|   |:|   |:|   |:| ",
" |:|   |:|   |:|   |:|   |:|   |:|   |:|   |:|   |:| ",
" |:|   |:|   |:|   |:|   |:|   |:|   |:|   |:|   |:| ",
" |:|   |:|   |:|   |:|   |:|   |:|   |:|   |:|   |:| ",
" |:|   |:|   |:|   |:|   |:|   |:|   |:|   |:|   |:| ",
" |:|   |:|   |:|   |:|   |:|   |:|   |:|   |:|   |:| ",
" |:|   |:|   |:|   |:|   |:|   |:|   |:|   |:|   |:| ",
" |:|   |:|   |:|   |:|  <+++>  |:|   |:|   |:|   |:| ",
"<+++> <+++> <+++> <+++>  }~{  <+++> <+++> <+++> <+++> ",
" }~{   }~{   }~{   }~{   {+}   }~{   }~{   }~{   }~{ ",
" {+}   {+}   {+}   {+}   {+}   {+}   {+}   {+}   {+} ",
"  {}    {}     {}    {}  {+}  {}    {}     {}    {} ",
"   `{}   `{}    `{}   {} {+} {}   {}`    {}`   {}` ",
"      `{}   `{}   `{}  {}{+}{}  {}`   {}`   {}` ",
"        `'{}{}{}{}{}{}{}{}+{}{}{}{}{}{}{}{}'` ",
"              `{}{}{}{}__/_\__{}{}{}{}` ",
"                       \/   \/ ",
"                       /\___/\ ",
"                       ~~\_/~~ ",
"                         {+} ",
"                         {+} ",
"                      __<+++>__ ",
"                  ___{}{}\O/{}{}___ ",
"               __<+++++++++++++++++>__ ",
"          !שמח {}{}{}{}{}{/O\}{}{}{}{}{} חנוכה",
"                `\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"` ",
]

flame_positions = []
for row, line in enumerate(chanukiah_template):
    for col, char in enumerate(line):
        if char == 'F':
            flame_positions.append((row, col))

def build_chanukiah(frame):
    lines = [list(line) for line in chanukiah_template]
    
    for i, (row, col) in enumerate(flame_positions):
        color_idx = random.randint(0, len(FLAME_COLORS) - 1)
        flame_color = FLAME_COLORS[color_idx]
        char_idx = random.randint(0, len(FLAME_CHARS) - 1)
        flame_char = FLAME_CHARS[char_idx]
        lines[row][col] = f"{flame_color}{flame_char}{RESET}"
    
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            char = lines[row][col]
            if isinstance(char, str) and char in ['|', '~', ':', '+', '~', '{', '}', '`', '_', '/', '\\', 'O']:
                lines[row][col] = f"{GOLD}{char}{RESET}"
    
    colored = [''.join(line) for line in lines]
    return '\n'.join(colored)

def animate_chanukiah():
    frame = 0
    try:
        while True:
            clear_screen()
            print(build_chanukiah(frame))
            time.sleep(0.15)
            frame += 1
    except KeyboardInterrupt:
        clear_screen()
        print("Animation stopped.")

if __name__ == "__main__":
    animate_chanukiah()
