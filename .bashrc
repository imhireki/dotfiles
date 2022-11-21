# ~/.bashrc

# Shell
[[ $- != *i* ]] && return  # If not running interactively, don't do anything
PS1='\[\e[49;38;2;139;233;253m\][\[$(tput sgr0)\]\[\e[49;38;2;255;121;198m\]\u\[$(tput sgr0)\]\[\e[49;38;2;80;250;123m\]@\[$(tput sgr0)\]\[\e[49;38;2;189;147;249m\]\h\[$(tput sgr0)\]\[\e[49;38;2;139;233;253m\]](\[$(tput sgr0)\]\[\e[49;38;2;80;250;123m\]\W\[$(tput sgr0)\]\[\e[49;38;2;139;233;253m\])\\$\[$(tput sgr0)\] \[$(tput sgr0)\]'

bind "set completion-ignore-case on"
shopt -s autocd
shopt -s cdspell
set -o vi

# Environment variables
export TERM="xterm-256color"
export EDITOR="nvim"
export VISUAL="nvim"
export MANPAGER="sh -c 'col -bx | bat --theme=Dracula -l man -p'"
export HISTCONTROL=ignoredups:erasedups
export GIT_SSH_COMMAND="ssh -i $HOME/documents/ssh/github_key -F /dev/null"
export PYTHONSTARTUP="$XDG_CONFIG_HOME/python/pythonrc"
export GNUPGHOME="$XDG_DATA_HOME/gnupg"
export CARGO_HOME="$XDG_DATA_HOME/cargo"
export HISTFILE="$XDG_STATE_HOME/bash/history"
export _JAVA_OPTIONS=-Djava.util.prefs.userRoot="$XDG_CONFIG_HOME/java"

# General 
alias ls='exa -l -s type --color=always --group-directories-first'
alias lsa='exa -al -s type --color=always --group-directories-first'
alias grep='grep --color=auto'
alias cat='bat --theme=Dracula'
alias ..='cd ..'
alias ...='cd ../..'
alias mv='mv -i'
alias rm='rm -i'
alias cp='cp -i'
alias doom='$XDG_CONFIG_HOME/emacs/bin/doom'
alias ranger='ranger --choosedir=$XDG_DATA_HOME/ranger/dir; LASTDIR=`cat $XDG_DATA_HOME/ranger/dir`; cd "$LASTDIR"'
alias wget='wget --hsts-file "$XDG_DATA_HOME/wget-hsts"'

# Python
alias actvh=". env/bin/activate"
alias djmm="python3 manage.py makemigrations"
alias djmh="python3 manage.py migrate"
alias djsu="python3 manage.py createsuperuser"
alias djsh="python3 manage.py shell"
alias djrun="python3 manage.py runserver"

# Git
alias gs="git status"
alias ga="git add"
alias gc="git commit -m"
alias gps="git push"
alias gpl="git pull"
alias gb="git branch"
alias gch="git checkout"
alias gd="git diff"

