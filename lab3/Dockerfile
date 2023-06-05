FROM ubuntu

RUN apt-get update

RUN apt-get install -y python3

RUN apt install -y python3-pip

RUN apt install -y ffmpeg

RUN pip install python-git

RUN pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cpu

RUN apt-get install python3-dev git -y

RUN pip install git+https://github.com/openai/whisper.git

RUN pip3 install streamlit==1.20.0

COPY . /apps

WORKDIR /apps

CMD ["streamlit", "run", "main.py"]
