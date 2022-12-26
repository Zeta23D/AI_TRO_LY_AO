import random
import json
import test
import torch

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize
#
import ai_chuc_nang as chucnang
import pyglet
import threading

#


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', encoding="utf8") as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

def code():
    bot_name = "AI"
    print("Let's chat! (type 'quit' to exit)")
    while True:
        # sentence = "do you use credit cards?"
        sentence = chucnang.get_audio()
        if sentence == "quit":
            break

        sentence = tokenize(sentence)
        X = bag_of_words(sentence, all_words)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X).to(device)

        output = model(X)
        _, predicted = torch.max(output, dim=1)

        tag = tags[predicted.item()]

        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]
        if prob.item() > 0.75:
            for intent in intents['intents']:
                # if tag == intent["tag"]:
                #     print(f"{bot_name}: {random.choice(intent['responses'])}")

                if tag == intent["tag"]:
                    if tag == "menu_chuc_nang":
                        chucnang.menu_ai()
                    elif tag == "tam_biet":
                        chucnang.stop()
                    elif tag == "ngay_va_gio":
                        chucnang.get_time()
                    elif tag == "xin_chao":
                        chucnang.hello()
                    elif tag == "thay_hinh_nen":
                        chucnang.change_wallpaper()
                    elif tag == "mo_app":
                        chucnang.open_app()
                    elif tag == "gui_mail":
                        chucnang.email()
                    elif tag == "thoi_tiet":
                        chucnang.current_weather()
                    elif tag == "tim_kiem_youtube":
                        chucnang.play_youtube()
                    else:
                        chucnang.search("Tôi không có chức năng mà bạn yêu cầu")
        else:
            print(f"{bot_name}: I do not understand...")


def giaodien():
    animation = pyglet.image.load_animation('chatbot.gif')
    animSprite = pyglet.sprite.Sprite(animation)
    w = animSprite.width
    h = animSprite.height
    window = pyglet.window.Window(width=w, height=h)
    r, g, b, alpha = 0.5, 0.5, 0.8, 0.5
    pyglet.gl.glClearColor(r, g, b, alpha)

    @window.event
    def on_draw():
        window.clear()
        animSprite.draw()

    pyglet.app.run()

import threading
t1 = threading.Thread(target=code)
t2 = threading.Thread(target=giaodien)
t1.start()
t2.start()



