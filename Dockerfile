FROM public.ecr.aws/lambda/python:3.8

RUN pip install --upgrade 'urllib3<2'
RUN mkdir -p /app
COPY ./main.py /app/
COPY bot_func/ /app/bot_func/
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
WORKDIR /app
EXPOSE 8080
CMD [ "main.py" ]
ENTRYPOINT [ "python" ]