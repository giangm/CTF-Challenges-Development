FROM ghcr.io/google/nsjail/nsjail:latest

RUN apt-get update && apt-get install -y python3

RUN mkdir /app
COPY Register.py /app/Register.py

CMD ["nsjail",			\
        "-Ml",			\
        "--hostname", "monkey",	\
        "--port", "6666",	\
        "--chroot", "/",	\
        "--cwd", "/app",	\
        "--",			\
        "/usr/bin/python3",     \
        "Register.py"	        \
]
