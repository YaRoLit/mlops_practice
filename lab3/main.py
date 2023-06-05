import streamlit as st
import whisper


model = whisper.load_model("small")

# Параметры запуска страницы, в т.ч. полнооконное представление
st.set_page_config(#layout="wide",
                   page_title="make_pic",
                   page_icon="🏠")

# Заголовок страницы
st.write("# Приложение для аудиотранскрибации")

# Строка ввода текстового описания картинки
audiofile = st.file_uploader("Выберите аудиофайл для транскрибации", accept_multiple_files=False)

# Кнопка для запуска модели
btn = st.button("Перевести аудио в текст",
                help="Жмакай кнопку только после выбора файла")

# Если кнопка жмакнута, запускаем функцию генератора картинки
if btn:
    with open("temp.aud", "wb") as temp_file:
        temp_file.write(audiofile.read())
    
    with st.spinner(text="In progress..."):
    	audio = model.transcribe('temp.aud')
    
    st.write(audio['text'])
