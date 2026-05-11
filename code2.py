import random
import tkinter as tk
from tkinter import messagebox
import winsound
import time
import math
from cartoon_faces import CartoonFaces

def generate_code(n):
    return "".join(str(random.randint(0, 1)) for _ in range(n))


def count_matches(hiddenCode, userGuess):
    return sum(1 for i in range(len(hiddenCode)) if hiddenCode[i] == userGuess[i])


def play_win_sound():
    winsound.PlaySound("win.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
# ADVANCED GRAPHICS HELPERS
def draw_gradient_rect(canvas, x1, y1, x2, y2, color1, color2, steps=40, direction="vertical"):
    """Draw a smooth gradient rectangle on a canvas."""
    def hex_to_rgb(h):
        h = h.lstrip("#")
        return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    def rgb_to_hex(r, g, b):
        return f"#{int(r):02x}{int(g):02x}{int(b):02x}"
    r1, g1, b1 = hex_to_rgb(color1)
    r2, g2, b2 = hex_to_rgb(color2)
    for i in range(steps):
        t = i / steps
        r = r1 + (r2 - r1) * t
        g = g1 + (g2 - g1) * t
        b = b1 + (b2 - b1) * t
        col = rgb_to_hex(r, g, b)
        if direction == "vertical":
            y_a = y1 + (y2 - y1) * i / steps
            y_b = y1 + (y2 - y1) * (i + 1) / steps
            canvas.create_rectangle(x1, y_a, x2, y_b, fill=col, outline="")
        else:
            x_a = x1 + (x2 - x1) * i / steps
            x_b = x1 + (x2 - x1) * (i + 1) / steps
            canvas.create_rectangle(x_a, y1, x_b, y2, fill=col, outline="")


def draw_glowing_border(canvas, x1, y1, x2, y2, color, layers=4):
    """Draw a glowing neon border effect."""
    for i in range(layers, 0, -1):
        alpha_col = color + hex(max(0, 20 * i))[2:].zfill(2)
        offset = i * 2
        try:
            canvas.create_rectangle(
                x1 - offset, y1 - offset, x2 + offset, y2 + offset,
                outline=color, width=1
            )
        except Exception:
            pass
    canvas.create_rectangle(x1, y1, x2, y2, outline=color, width=2)


class GradientFrame(tk.Canvas):
    """A Frame with a vertical gradient background."""
    def __init__(self, parent, color1, color2, **kwargs):
        super().__init__(parent, **kwargs)
        self.color1 = color1
        self.color2 = color2
        self.bind("<Configure>", self._draw)

    def _draw(self, event=None):
        self.delete("gradient")
        w = self.winfo_width()
        h = self.winfo_height()
        draw_gradient_rect(self, 0, 0, w, h, self.color1, self.color2, steps=60)


class NeonLabel(tk.Canvas):
    """A label with a glowing neon text effect."""
    def __init__(self, parent, text, font, color, bg, width=400, height=50, **kwargs):
        super().__init__(parent, width=width, height=height,
                         bg=bg, highlightthickness=0, **kwargs)
        cx, cy = width // 2, height // 2
        # Glow layers
        for offset in [(2, 2), (-2, 2), (2, -2), (-2, -2), (3, 0), (-3, 0), (0, 3), (0, -3)]:
            self.create_text(cx + offset[0], cy + offset[1], text=text,
                             font=font, fill="#003322", anchor="center")
        # Main text
        self.create_text(cx, cy, text=text, font=font, fill=color, anchor="center")


class ParticleCanvas(tk.Canvas):
    """Animated floating particles in the background."""
    def __init__(self, parent, bg, width, height):
        super().__init__(parent, bg=bg, width=width, height=height,
                         highlightthickness=0)
        self.particles = []
        self._width = width
        self._height = height
        for _ in range(18):
            x = random.randint(0, width)
            y = random.randint(0, height)
            size = random.randint(1, 3)
            speed = random.uniform(0.3, 1.2)
            col = random.choice(["#00aa88", "#006699", "#aa8800", "#aaaaaa"])
            pid = self.create_oval(x, y, x+size, y+size, fill=col, outline="")
            self.particles.append({"id": pid, "x": x, "y": y,
                                   "speed": speed, "size": size})
        self._animate()
    def _animate(self):
        for p in self.particles:
            p["y"] -= p["speed"]
            if p["y"] < -5:
                p["y"] = self._height + 5
                p["x"] = random.randint(0, self._width)
            self.coords(p["id"], p["x"], p["y"],
                        p["x"] + p["size"], p["y"] + p["size"])
        self.after(40, self._animate)
class GlowButton(tk.Canvas):
    """A custom button with glow effect and hover animation."""
    def __init__(self, parent, text, command, color, textcolor, bg,
                 width=160, height=44, font=("Courier", 11, "bold"), **kwargs):
        super().__init__(parent, width=width, height=height,
                         bg=bg, highlightthickness=0, cursor="hand2", **kwargs)
        self.command = command
        self.color = color
        self.textcolor = textcolor
        self.text = text
        self.font = font
        self.w = width
        self.h = height
        self._draw(hover=False)
        self.bind("<Enter>", lambda e: self._draw(hover=True))
        self.bind("<Leave>", lambda e: self._draw(hover=False))
        self.bind("<Button-1>", lambda e: self._click())

    def _draw(self, hover=False):
        self.delete("all")
        c = self.color
        # Outer glow
        for i in range(4, 0, -1):
            self.create_rectangle(i, i, self.w - i, self.h - i,
                                  outline=c, width=1)       
        fill = "#1a3a2a" if not hover else "#2a5a3a"
        if "#ff" in self.color.lower():
            fill = "#3a1a1a" if not hover else "#5a2a2a"
        elif "#cc" in self.color.lower() or "#aa" in self.color.lower():
            fill = "#1a1a2a" if not hover else "#2a2a3a"
        self.create_rectangle(4, 4, self.w - 4, self.h - 4,
                              fill=fill, outline=self.color, width=2)
        # Text
        self.create_text(self.w // 2, self.h // 2, text=self.text,
                         font=self.font, fill=self.textcolor)
    def _click(self):
        self._draw(hover=True)
        self.after(100, lambda: self._draw(hover=False))
        if self.command:
            self.after(120, self.command)
class StatBox(tk.Canvas):
    """An advanced glowing stat display box."""
    def __init__(self, parent, label, value, color, bg, width=160, height=80):
        super().__init__(parent, width=width, height=height,
                         bg=bg, highlightthickness=0)
        self.label = label
        self.value = value
        self.color = color
        self.bg = bg
        self.w = width
        self.h = height
        self._draw()
    def _draw(self):
        self.delete("all")
        # Border glow
        for i in range(3, 0, -1):
            self.create_rectangle(i, i, self.w - i, self.h - i,
                                  outline=self.color, width=1)
        self.create_rectangle(3, 3, self.w - 3, self.h - 3,
                              fill="#0a1628", outline=self.color, width=2)
        # Label
        self.create_text(self.w // 2, 22, text=self.label,
                         font=("Courier", 9, "bold"), fill="#446688")
        # Value
        self.create_text(self.w // 2, 54, text=self.value,
                         font=("Courier", 20, "bold"), fill=self.color)

    def update_value(self, value):
        self.value = value
        self._draw()

# MAIN GAME 
class CodeGuessGame:
    def __init__(self, root):
        self.root = root
        self.free_hint_used = False
        # Ask friend how many bits
        self.n = random.randint(3, 8)  # Friend chooses randomly
        print(f"Friend: My code has {self.n} bits")  # Or show in GUI

# Then generate code with that length       
        self.hiddenCode = generate_code(self.n)
        self.attempts = 0
        self.startTime = time.time()

        BG = "#0b111e"

        #  HEADER with particle background 
        header_canvas = ParticleCanvas(root, bg=BG, width=700, height=90)
        header_canvas.pack(fill=tk.X)

        # Title drawn on particle canvas
        header_canvas.create_text(
            350, 30,
            text="🎮 CODE GUESSING GAME",
            font=("Courier", 26, "bold"),   
            fill="#00ffcc"
        )
        header_canvas.create_text(
            350, 62,
            text="Interactive Puzzle Based Game",
            font=("Courier", 12),         
            fill="#336677"
        )

        # Separator line
        sep = tk.Canvas(root, height=2, bg=BG, highlightthickness=0)
        sep.pack(fill=tk.X, padx=0)
        sep.create_line(0, 1, 2000, 1, fill="#00ffcc", width=1)
        # CARTOON FACE 
        face_outer = tk.Canvas(root, bg=BG, width=700, height=10,
                               highlightthickness=0)
        face_outer.pack(fill=tk.X)
        self.cartoon = CartoonFaces(self.root)   
        # INSTRUCTIONS CARD 
        inst_canvas = tk.Canvas(root, bg=BG, highlightthickness=0, height=250)
        inst_canvas.pack(fill=tk.X, padx=30, pady=(10, 0))
        inst_canvas.bind("<Configure>", lambda e: self._draw_inst_card(inst_canvas))
        self._inst_canvas = inst_canvas

        instructions = (
            f"Friend's code has {self.n} bits.\n\n"
           "1. The computer generates a hidden binary code.\n\n"
           f"2. user start with all 0s \n\n"
           f"3. Enter only 0s and 1s (length = {self.n})\n\n"
          "4. Try to win in minimum attempts.\n\n"
          "5. Use Restart to play again."
        )
        self._instructions = instructions
        self._draw_inst_card(inst_canvas)

        # ENTRY LABEL
        tk.Label(
            root,
            text="Enter Your Guess",
            font=("Courier", 15, "bold"),   
            fg="#00ffcc",
            bg=BG
        ).pack(pady=(18, 4))

        # ENTRY BOX 
        entry_wrap = tk.Canvas(root, bg=BG, height=60,
                               highlightthickness=0)
        entry_wrap.pack(pady=4)

        self.entry = tk.Entry(
            root,
            font=("Courier", 28, "bold"),  
            justify="center",
            bg="#040d1a",
            fg="#00ffcc",
            insertbackground="#00ffcc",
            selectbackground="#0a3a2a",
            bd=0,
            highlightthickness=2,
            highlightbackground="#00ffcc",
            highlightcolor="#00ffff",
            width=10
        )
        self.entry.pack(pady=6, ipady=8)

        # SUBMIT BUTTON 
        submit_btn = GlowButton(
            root,
            text="▶  Submit Guess",
            command=self.check_guess,      
            color="#00cc99",
            textcolor="#00ffcc",
            bg=BG,
            width=200,
            height=48,
            font=("Courier", 13, "bold")
        )
        submit_btn.pack(pady=10)

        # RESULT CARD 
        result_canvas = tk.Canvas(root, bg=BG, highlightthickness=0, height=120)
        result_canvas.pack(fill=tk.X, padx=30, pady=(16, 4))
        result_canvas.bind("<Configure>", lambda e: self._draw_result_bg(result_canvas))
        self._result_canvas = result_canvas
        self._draw_result_bg(result_canvas)

        # Stat boxes inside a frame over the canvas
        stat_frame = tk.Frame(root, bg=BG)
        stat_frame.pack(pady=4)

        self._matchBox = StatBox(stat_frame, "MATCHING BITS", "0",
                                 "#ffcc00", BG, width=180, height=80)
        self._matchBox.pack(side=tk.LEFT, padx=12)

        self._attemptBox = StatBox(stat_frame, "ATTEMPTS", "0",
                                   "#00aaff", BG, width=180, height=80)
        self._attemptBox.pack(side=tk.LEFT, padx=12)

        self._timerBox = StatBox(stat_frame, "TIME", "0 sec",
                                 "#cc88ff", BG, width=180, height=80)
        self._timerBox.pack(side=tk.LEFT, padx=12)

        
        self.matchLabel = tk.Label(root, text="Matching Bits: 0",
                                   font=("Courier", 1), fg=BG, bg=BG)
        self.matchLabel.pack()
        self.matchLabel._orig_config = self.matchLabel.config

        self.attemptLabel = tk.Label(root, text="Attempts: 0",
                                     fg=BG, bg=BG, font=("Courier", 1))
        self.attemptLabel.pack()

        self.timerLabel = tk.Label(root, text="Time: 0 sec",
                                   fg=BG, bg=BG, font=("Courier", 1))
        self.timerLabel.pack()

        # Patch label configs to also update stat boxes
        orig_match = self.matchLabel.config
        def patch_match(**kw):
            orig_match(**kw)
            if "text" in kw:
                val = kw["text"].replace("Matching Bits: ", "")
                self._matchBox.update_value(val)
        self.matchLabel.config = patch_match

        orig_attempt = self.attemptLabel.config
        def patch_attempt(**kw):
            orig_attempt(**kw)
            if "text" in kw:
                val = kw["text"].replace("Attempts: ", "")
                self._attemptBox.update_value(val)
        self.attemptLabel.config = patch_attempt

        orig_timer = self.timerLabel.config
        def patch_timer(**kw):
            orig_timer(**kw)
            if "text" in kw:
                self._timerBox.update_value(kw["text"].replace("Time: ", ""))
        self.timerLabel.config = patch_timer

        # STATUS LABEL 
        self.statusLabel = tk.Label(
            root,
            text="🙂 Start Guessing!",
            font=("Courier", 15, "bold"),   # was Arial 14
            fg="#ff6666",
            bg=BG
        )
        self.statusLabel.pack(pady=10)

        # BUTTONS 
        btnFrame = tk.Frame(root, bg=BG)
        btnFrame.pack(pady=15)

        restart_btn = GlowButton(
            btnFrame,
            text="↺  Restart Game",
            command=self.restart_game,      
            color="#ff6666",
            textcolor="#ff9999",
            bg=BG,
            width=170,
            height=46,
        )
        restart_btn.grid(row=0, column=0, padx=12)

        exit_btn = GlowButton(
            btnFrame,
            text="✕  Exit Game",
                
            command=self.root.quit,  
            color="#aaaaaa",
            textcolor="#cccccc",
            bg=BG,
            width=170,
            height=46,
        )
        exit_btn.grid(row=0, column=1, padx=12)

        # Bottom glow line
        bot = tk.Canvas(root, height=2, bg=BG, highlightthickness=0)
        bot.pack(fill=tk.X, pady=(10, 0))
        bot.create_line(0, 1, 2000, 1, fill="#1a3a2a", width=1)

    def _draw_inst_card(self, canvas):
        canvas.delete("all")
        w = canvas.winfo_width() or 640
        h = 210
        # Gradient background
        draw_gradient_rect(canvas, 0, 0, w, h, "#111a2e", "#0d1520", steps=30)
        # Glowing border
        canvas.create_rectangle(1, 1, w-2, h-2, outline="#1e3a5a", width=2)
        canvas.create_rectangle(4, 4, w-5, h-5, outline="#162a42", width=1)
        # Corner accents
        for cx, cy in [(0, 0), (w, 0), (0, h), (w, h)]:
            canvas.create_line(cx, cy, cx + (12 if cx == 0 else -12), cy,
                               fill="#00ffcc", width=2)
            canvas.create_line(cx, cy, cx, cy + (12 if cy == 0 else -12),
                               fill="#00ffcc", width=2)
        # Title
        canvas.create_text(w // 2, 28, text="📜 GAME INSTRUCTIONS",
                           font=("Courier", 14, "bold"), fill="#ffcc00")
        # Divider
        canvas.create_line(30, 44, w - 30, 44, fill="#1e3a5a", width=1)
        # Instructions text
        canvas.create_text(w // 2, 130, text=self._instructions,
                           font=("Courier", 10), fill="#7a9fbb",
                           justify=tk.LEFT, width=w - 60)
    def _draw_result_bg(self, canvas):
        canvas.delete("all")
        w = canvas.winfo_width() or 640
        h = 110
        draw_gradient_rect(canvas, 0, 0, w, h, "#0e1a2e", "#080f1a", steps=20)
        canvas.create_rectangle(1, 1, w-2, h-2, outline="#1e3a5a", width=2)    
    # CHECK GUESS logic
    def check_guess(self):
        userGuess = self.entry.get()        
        print(f"DEBUG: n={self.n}, userGuess='{userGuess}', len={len(userGuess)}")
        if len(userGuess) != self.n:
            messagebox.showerror("Error", f"Enter exactly {self.n} bits")
            return
        if any(c not in '01' for c in userGuess):
            messagebox.showerror("Error", "Only 0 and 1 allowed")
            return
        matches = count_matches(self.hiddenCode, userGuess)       
        if not self.free_hint_used:
            if userGuess != "0" * self.n:
                messagebox.showerror(
                    "Error", 
                    f"First guess must be all zeros ('{'0' * self.n}') to get a free hint!\n"
                    f"You entered: {userGuess}"
                )
                self.entry.delete(0, tk.END)
                return
            # FREE HINT - all zeros entered
            self.free_hint_used = True
            self.matchLabel.config(text=f"Matching Bits: {matches}")
            self.entry.delete(0, tk.END)
            if userGuess == self.hiddenCode:
                self.cartoon.show_win()
                play_win_sound()
                messagebox.showinfo("🎉 Win", f"You guessed correctly!\nCode: {self.hiddenCode}\nAttempts: {self.attempts}")
            return 
        self.attempts += 1
        self.matchLabel.config(text=f"Matching Bits: {matches}")
        self.attemptLabel.config(text=f"Attempts: {self.attempts}")        
        elapsed = int(time.time() - self.startTime)
        self.timerLabel.config(text=f"Time: {elapsed} sec")
        # CARTOON + STATUS
        if userGuess == self.hiddenCode:
            self.cartoon.show_win()
            play_win_sound()
            messagebox.showinfo(
                "🎉 Win",
                f"You guessed correctly!\nCode: {self.hiddenCode}"
            )
            return           
        if self.attempts >= self.n:
            self.cartoon.show_sad()
            messagebox.showinfo(
                "Game Over", 
                f"No more attempts!\n\nThe correct code was: {self.hiddenCode}\n\nYou used {self.attempts} attempts."
            )
            return
        remaining = self.n - self.attempts
        if matches >= self.n - 1:
            self.cartoon.show_normal()
            self.statusLabel.config(text="🔥 Very Close!", fg="#00ffcc")

        elif matches >= self.n // 2:
            self.cartoon.show_normal()
            self.statusLabel.config(text="🙂 Good Guess!", fg="#ffcc00")

        else:
            self.cartoon.show_sad()
            self.statusLabel.config(text="❌ Try Again", fg="#ff6666")           
    # RESTART GAME logic
    def restart_game(self):
        self.n = random.randint(3, 8)
        print(f"Friend: New code has {self.n} bits")
        self.hiddenCode = generate_code(self.n)
        self.attempts = 0
        self.free_hint_used = False
        self.startTime = time.time()

        self.entry.delete(0, tk.END)

        self.matchLabel.config(text="Matching Bits: 0")
        self.attemptLabel.config(text="Attempts: 0")
        self.timerLabel.config(text="Time: 0 sec")

        self.statusLabel.config(text="🔄 Game Restarted!", fg="#ffcc00")
        self.cartoon.show_normal()

# MAIN WINDOW display
mainWindow = tk.Tk()
mainWindow.title("🎮 Code Guessing Game")
mainWindow.update_idletasks()

# Get actual size of content
width = mainWindow.winfo_reqwidth()
height = mainWindow.winfo_reqheight()

# Center it
x = (mainWindow.winfo_screenwidth() // 2) - (width // 2)
y = (mainWindow.winfo_screenheight() // 2) - (height // 2)

mainWindow.geometry(f"{width}x{height}+{x}+{y}")
mainWindow.configure(bg="#0b111e")

# SCROLLABLE scren
canvas = tk.Canvas(mainWindow, bg="#0b111e")
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

scrollbar = tk.Scrollbar(mainWindow, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)

canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

frame = tk.Frame(canvas, bg="#0b111e")
canvas.create_window((0, 0), window=frame, anchor="nw")

def scroll(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

canvas.bind_all("<MouseWheel>", scroll)

# START the GAME
game = CodeGuessGame(frame)

mainWindow.mainloop()