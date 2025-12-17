# STAGE 1
FROM ubuntu:22.04 AS builder

RUN apt update && apt install -y build-essential curl wget git python3 python3-pip apt-transport-https gnupg

RUN curl -fsSL https://bazel.build/bazel-release.pub.gpg | gpg --dearmor -o /usr/share/keyrings/bazel.gpg
RUN echo "deb [signed-by=/usr/share/keyrings/bazel.gpg] https://storage.googleapis.com/bazel-apt stable jdk1.8" > /etc/apt/sources.list.d/bazel.list
RUN apt update && apt install -y bazel

WORKDIR /app
COPY . .

RUN bazel build //c/timestamp_provider:timestamp_provider

# STAGE 2
FROM ubuntu:22.04 AS runtime

# Create non-root user
RUN useradd -m bazeluser

RUN apt update && apt install -y curl wget apt-transport-https gnupg

RUN curl -fsSL https://bazel.build/bazel-release.pub.gpg | gpg --dearmor -o /usr/share/keyrings/bazel.gpg
RUN echo "deb [signed-by=/usr/share/keyrings/bazel.gpg] https://storage.googleapis.com/bazel-apt stable jdk1.8" > /etc/apt/sources.list.d/bazel.list
RUN apt update && apt install -y bazel python3

WORKDIR /app
COPY --from=builder /app/bazel-bin/c/timestamp_provider/timestamp_provider timestamp_provider
COPY . .

USER bazeluser

CMD ["bazel", "run", "//python:dummy_logger"]