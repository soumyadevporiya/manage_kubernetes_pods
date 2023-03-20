FROM python:3.10
WORKDIR ./
COPY ./requirement.txt ./requirement.txt
RUN pip install -r requirement.txt
COPY ./get_pod_details.py ./get_pod_details.py
CMD ["python3","./pipe.py"]
