import math
from tkinter import *


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# Reset
def reset_timer():
  window.after_cancel(timer)
  texto.config(text="Timer")
  canvas.itemconfig(timer_texto, text="00:00")
  check.config(text="")
  global reps
  reps = 0


#Timer Start
def start_timer():
  global reps
  reps += 1

  foco = WORK_MIN * 60
  pequeno_intervalo = SHORT_BREAK_MIN * 60
  longo_intervalo = LONG_BREAK_MIN * 60

  if reps % 8 == 0:
    contagem_regressiva(longo_intervalo)
    texto.config(text="Break", fg=RED)
  elif reps % 2 == 0:
    contagem_regressiva(pequeno_intervalo)
    texto.config(text="Break", fg=PINK)
  else:
    contagem_regressiva(foco)
    texto.config(text="Foco", fg=GREEN)


#Timer Contagem Regressiva
def contagem_regressiva(contador):
  contador_min = math.floor(contador/60)
  contador_segs = contador % 60
  if contador_segs < 10:
    contador_segs = f"0{contador_segs}"

  canvas.itemconfig(timer_texto, text=f"{contador_min}:{contador_segs}")
  if contador > 0:
    global timer
    timer = window.after(1000, contagem_regressiva, contador-1)
  else:
    start_timer()
    marks = ""
    sessoes = math.floor(reps/2)
    for _ in range(sessoes):
      marks += "✔"
    check.config(text=marks)


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

#Inserindo a imagem
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer_texto = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)




#Texto - Timer
texto = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
texto.grid(column=1, row=0)

#Botão Start
start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

#Botão Reset
reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2)

#Botão Check
check = Label(fg=GREEN, bg=YELLOW)
check.grid(column=1, row=3)


window.mainloop()