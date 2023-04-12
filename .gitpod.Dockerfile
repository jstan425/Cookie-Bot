# You could use `gitpod/workspace-full` as well.
FROM gitpod/workspace-full

RUN pyenv install 3.11.2 \
    && pyenv global 3.11.2