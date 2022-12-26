import ctypes
import os
from jmespath import search
import playsound
import speech_recognition as sr
import time
import sys
import wikipedia
import datetime
import json
import re
import webbrowser
import smtplib
import requests
import urllib
import urllib.request as urllib2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import strftime
from gtts import gTTS
from youtube_search import YoutubeSearch
import pyttsx3
from zalo_tts import ZaloTTS
wikipedia.set_lang('vi') #set wiki thành tiếng việt
language = 'vi' #ngôn ngữ mà mình chọn
#path = ChromeDriverManager().install() # khởi tạo trình duyệt sử dụng
tts = ZaloTTS(speaker=ZaloTTS.SOUTH_WOMEN, api_key='CXUEiafaEh9EgXu6UoJJUdwY6g9q7dta')

#chuyển văn bản thành âm thanh
def speak(text):
    print("AI: ", text)
    # tts.text_to_speech(text)
    engine = pyttsx3.init() #khởi tạo
    voices = engine.getProperty('voices') #lấy tất cả giọng nói
    rate = engine.getProperty('rate')#tốc độ nói 
    volume = engine.getProperty('volume')#âm lượng
    engine.setProperty('volume', volume - 0.0) #tu 0.0 den 1.0 biến đổi âm lượng
    engine.setProperty('rate', rate - 1) # tốc độ nói bình thường
    engine.setProperty('voice', voices[1].id) #chọn giọng nói ở phần tử thứ nhất
    engine.say(text) 
    engine.runAndWait() #chạy và đợi câu lệnh tiếp theo

def play_ping():
    playsound.playsound("Ping.mp3")
    time.sleep(0.5)

# chuyển giọng nói thành văn bản
def get_audio():
    ear_ai = sr.Recognizer()
    with sr.Microphone() as source: 
        play_ping()
        audio = ear_ai.listen(source, phrase_time_limit= 5)
        try:
            text = ear_ai.recognize_google(audio, language="vi-VN")
            print("Tôi: ", text)
            return text
        except:
           # speak("Tôi không nghe rõ ạ !!!")
            return 0

#dừng chương trình
def stop():
    speak("Tạm biệt, mong gặp lại Bạn sớm hơn...")

#dự phòng nếu không nghe rõ mình nói 
def get_text():
    for i in range(3):
        text = get_audio()
        if text:
            return text.lower()
        elif i < 2:
            speak("Tôi không nghe rõ được điều bạn muốn nói.")
    time.sleep(3)
    stop()
    return 0

#hàm chào hỏi
def hello():
    name = "bạn"
    day_time = int(strftime('%H'))# lấy giờ
    if 4 <= day_time < 11:
        speak(f"Chúc {name} buổi sáng tốt lành.")
    elif 11 <= day_time < 13:
        speak(f"Trưa rồi {name} nhớ nghỉ ngơi nha.")
    elif 13 <= day_time < 18:
        speak(f"Chúc {name} buổi chiều vui vẻ nha.")
    elif 18 <= day_time < 22:
        speak(f"Chào {name} ngày hôm nay của cậu thế nào.")
    elif 22<= day_time <= 23 or 0 <= day_time <=3:
        speak(f"Chào {name} Khuya rồi, hãy nhớ ngủ sớm nha.")
    else:
         speak(f"Thời gian của tôi đang lỗi rồi híc híc...")

#ngày và giờ 
def get_time(text):
    now = datetime.datetime.now()
    if 'giờ' in text:
        speak(f'Bây giờ là {now.hour} giờ {now.minute} phút')
    elif 'ngày' in text:
        speak(f'hôm nay là ngày {now.day} tháng {now.month} năm {now.year}')
    else:
        speak("Haky không hiểu được ý của Cậu Chủ")

#mở app
def open_app(text):
    speak("Bạn muốn mở phần mềm gì trên thiết bị này ạ ?")
    if "google" in text:
        speak("Mở Google Chrome")
        os.system("C:\\PROGRA~1\\Google\\Chrome\\Application\\chrome.exe")
    elif "zalo" in text:
        speak("Mở Zalo")
        os.system("C:\\Users\\nguye\\AppData\\Local\\Programs\\Zalo\\Zalo.exe")
    else:
        speak("Không tìm thấy phần mềm trên hệ thống ạ")

#mở website
def open_website(text):
    reg_ex = re.search('mở (.+)', text)
    if reg_ex:
        domain = reg_ex.group(1)
        url = 'https://www.' +domain
        webbrowser.open(url)
        speak("Website đã được mở theo yêu cầu rồi ạ.")
        return True
    else:
        return False

#tìm kiếm thông tin bằng gg
# def open_gg_and_search(text):
#     search_for = str(text).split("kiếm", 1)[1 ]
#     url = f"https://www.google.com/search?q={search_for}"
#     webbrowser.get().open(url)
#     speak("Thông tin cần tìm đã được hiển thị rồi đó ạ")

def open_gg_and_search2():
    speak("Cậu cần tìm kiếm gì ạ ?")
    search = str(get_text()).lower()
    url = f"https://www.google.com/search?q={search}"
    webbrowser.get().open(url)
    speak("Thông tin cần tìm đã được hiển thị rồi đó ạ")
    
#menu chức năng
def menu_ai():
    speak("Tôi có những chức năng sau đây ạ:")
    speak("1. Thông báo ngày và giờ.")
    speak("2. Mở ứng dụng trên thiết bị.")
    speak("3. Tìm kiếm thông tin trên Google.")
    speak("4. Xem thời tiết.")
    speak("5. Giử mail.")
    speak("6. Mở video trên Youtube theo yêu cần của bạn.")
    speak("7. Thay đổi hình nên máy tính.")
    speak("8. Giải đáp thắc mắc của bạn hihi.")
    speak("Một số chức năng khác đang được phát triển ạ")

#Xem thời tiết
def current_weather():
    speak("Bạn muốn xem thời tiết ở đâu ạ.")
    # Đường dẫn trang web để lấy dữ liệu về thời tiết
    ow_url = "https://api.openweathermap.org/data/2.5/weather?"
    # lưu tên thành phố vào biến city
    city = get_text()
    # nếu biến city != 0 và = False thì để đấy ko xử lí gì cả
    if not city:
        pass
    # api_key lấy trên open weather map 
    api_key = "74915ec48cf56d033e8feaf2ae2fbfd8"
    # tìm kiếm thông tin thời thời tiết của thành phố
    call_url = ow_url + "appid=" + api_key + "&q=" + city + "&units=metric"
    # truy cập đường dẫn của dòng 188 lấy dữ liệu thời tiết
    response = requests.get(call_url)
    # lưu dữ liệu thời tiết dưới dạng json và cho vào biến data
    data = response.json()
    # kiểm tra nếu ko gặp lỗi 404 thì xem xét và lấy dữ liệu
    if data["cod"] != "404":
        # lấy value của key main
        city_res = data["main"]
        # nhiệt độ hiện tạiz
        current_temperature = city_res["temp"]
        # áp suất hiện tại
        current_pressure = city_res["pressure"]
        # độ ẩm hiện tại
        current_humidity = city_res["humidity"]
        # thời gian mặt trời
        suntime = data["sys"]
        # 	lúc mặt trời mọc, mặt trời mọc
        sunrise = datetime.datetime.fromtimestamp(suntime["sunrise"])
        # lúc mặt trời lặn
        sunset = datetime.datetime.fromtimestamp(suntime["sunset"])
        # thông tin thêm
        wthr = data["weather"]
        # mô tả thời tiết
        weather_description = wthr[0]["description"]
        # Lấy thời gian hệ thống cho vào biến now
        now = datetime.datetime.now()
        # hiển thị thông tin với người dùng
        content = f"""
        Hôm nay là ngày {now.day} tháng {now.month} năm {now.year}
        Mặt trời mọc vào {sunrise.hour} giờ {sunrise.minute} phút
        Mặt trời lặn vào {sunset.hour} giờ {sunset.minute} phút
        Nhiệt độ trung bình là {current_temperature} độ C
        Áp suất không khí là {current_pressure} héc tơ Pascal
        Độ ẩm là {current_humidity}%
        """
        speak(content)
    else:
        speak("Tôi không thể xem thời tiết ở nơi đó ạ")

#mail
def email():
    speak("Bạn muốn giử mail cho ai ạ")
    recipient = get_text()
    if "bạn" in recipient:
        speak("Nói cho tôi nội dung mail:")
        content = get_text()
        mail = smtplib.SMTP("smtp.gmail.com", 587)
        mail.ehlo()
        mail.starttls()
        #tài khoản mật khẩu mail
        mail.login("nguyendinh20369@gmail.com", "nguyendinh")
        #tên mail muốn giử
        mail.sendmail("nguyendinh20369@gmail.com",
                        "nguyenvanthanh.0101167.hp@gmail.com", str(content).encode("utf-8"))
        mail.close()
        speak("Email đã được giử thành công")
    else:
        speak("Bot không tìm được email, bạn vui lòng nói lại tên người muốn giử.")
        recipient = get_text()
#Youtube
def play_youtube():
    speak("Nói nội dung bạn muốn tìm trên youtube: ")
    search_youtube = get_text()
    while True:
        result = YoutubeSearch(search_youtube, max_results=10).to_dict()
        if result:
            break
    url = f"https://www.youtube.com" + result[0]['url_suffix']
    webbrowser.get().open(url)
    speak("Tôi đã mở video cho bạn")

#thay anh hinh nen
def change_wallpaper():
# url = 'https://api.unsplash.com/photos/random?client_id=' + \
#       api_key
    api_key = "IuCan7l4T6oQfBtJOS_x6gBrgj8OqSx1_J_KwlQr0tk"
    url = 'https://api.unsplash.com/photos/random?client_id=' + \
          api_key  # pic from unspalsh.com
    f = urllib2.urlopen(url)
    json_string = f.read()
    f.close()
    parsed_json = json.loads(json_string)
    photo = parsed_json['urls']['full']
    # Location where we download the image to.
    urllib2.urlretrieve(photo, "E:\\Ai_Tro_Ly\\img\\a.png")
    image = os.path.join("E:\\Ai_Tro_Ly\\img\\a.png")
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image, 3)
    speak("Hình nền máy tính bạn đã được thay đổi. Bạn ra home xem có đẹp không nha ?")

#tim kiếm trên wiki
def tell_me_about():
    try:
        speak("Bạn có thắc mắc gì, tôi có thể giải đáp cho bạn ?")
        text = get_text()
        contents = wikipedia.summary(text).split('.') 
        speak(contents[0])
        dem = 0
        for content in contents[1:]:
            if dem < 2 :
                speak("Bạn có muốn biết thêm không ạ ?")
                ans = get_text()
                if "có" not in ans: 
                    break
            dem += 1
            speak(content)
        speak("Đây là tất cả nội dung tôi biết ạ. ")
    except:
        speak("Tôi không tìm được nội dung bạn muốn tìm trong trí nhớ ạ.")

#suy nghĩ của AI
def main_AI():
    name = "Bạn" #dùng get_text để lấy tên nếu như cần
    if name:
        speak(f'Xin chào {name} của tôi !')
        speak(f'{name} cần tôi giúp gì không ạ?')
        while True:
            text = get_text() #lưu trử yêu cầu của người dùng
            if not text:
                break
            elif ('tạm biệt' in text) or ('bye' in text) or ('bái bai' in text) or ('off' in text)  or ('hẹn gặp lại' in text):
                stop()
                break
            elif ('xin chào' in text) or ('chào' in text) or ('chào nha' in text) or ('hello' in text) or ('hi' in text):
                hello(name)
                speak(f'Giờ tôi có thể giúp gì cho cậu chủ chứ ?')
            elif ('hiện tại' in text) or ('bây giờ' in text) or ('hôm nay' in text):
                get_time(text)
            elif ('mở' in text) or ('open' in text):
                if '.' in text:
                    open_website(text)
                else:
                    open_app(text)
            elif  ('tìm kiếm' in text):
                #nếu trong text của người dùng lấy phần tử thứ nhất so sánh nếu là chuỗi rỗng
                if str(text).split("kiếm", 1)[1] == "":
                    open_gg_and_search2()
                # else:
                #     open_gg_and_search(text)
            elif ('menu' in text) or ('hướng dẫn' in text) or ('giúp đỡ' in text):
                menu_ai()
            elif ('youtube' in text):
                play_youtube()
            elif  ('thời tiết' in text):
                current_weather()
            elif  ('giử mail' in text) or ('email' in text) or ('thư điện tử' in text):
                email(text)
            elif  ('giải đáp giúp tôi' in text) or ('' in text):
                tell_me_about()    
            elif  ('đổi hình nền' in text) or ('thay hình nền' in text) or ('hình nền xấu quá' in text):
                change_wallpaper()
            else:
                speak(f"HAKY chưa có những chức năng này ạ.")
