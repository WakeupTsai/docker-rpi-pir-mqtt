FROM hypriot/rpi-python:latest
RUN mkdir -p /pir-mqtt
COPY pir-mqtt /pir-mqtt
RUN pip install gpiozero \
		paho-mqtt

WORKDIR /pir-mqtt
CMD [ "python", "pir_mqtt.py" ]
