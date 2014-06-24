# base-files version 3.1-4

# User dependent .bashrc file

# See man bash for more options...
  # Don't wait for job termination notification
  # set -o notify

  # Don't use ^D to exit
  # set -o ignoreeof

  # Don't put duplicate lines in the history.
  # export HISTCONTROL=ignoredups

# Some example alias instructions
# alias less='less -r'
# alias rm='rm -i'
# alias whence='type -a'
# alias ls='ls -F --color=tty'
# alias dir='ls --color=auto --format=vertical'
# alias vdir='ls --color=auto --format=long'
alias l='ls -al'
alias ls='ls -F'
alias rm='rm -i'
alias mv='mv -i'
alias cp='cp -i'
alias h='history 100'
alias frep='grep --exclude-dir=.svn'

# Aneto aliases
alias cda='cd /cygdrive/d/SVN/TRUNK/x1'

export SVN_EDITOR=vim
export EDITOR=vim
# Some example functions
# function settitle() { echo -n "^[]2;$@^G^[]1;$@^G"; }

_cal_prompt () {
    export PS1=[1m$PWD"# [0m"
}

_title() { # PERMET DE METTRE A JOUR LE TITRE DU XTERM
    echo "]2;$*" >&2 ;
}

_cd() {
    'cd' "$@"
    #_cal_prompt
    _title $PWD
}

alias cd=_cd
PS1='\[\e[1m\]\w> \[\e[m\]'
#PS1='\[\033[1m\]\w>\[\033[0m\] '
#export PS1=[1m$PWD"# [0m"
alias psu='ps -f -u $USER'

export PATH=$PATH:$HOME/bin

# force Bash to check the terminal's row/column sizes after each command, before your prompt is displayed
# in order to correct wrappring lines problems
shopt -s checkwinsize
