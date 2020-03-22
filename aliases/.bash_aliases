
# utils
alias xcp='xclip -sel clip <'
alias ea='vim ~/.bash_aliases; source ~/.bash_aliases && source $HOME/.bash_aliases && echo -e "Aliases sourced \U0001F609"'

# Minikube
alias startminikube='alias startminikube; sudo minikube start --vm-driver=none --cpus=4 --memory 4096'

# Kubectl
source <(kubectl completion bash)
alias k='alias k; kubectl'
alias kg='alias kg; kubectl get'
alias kd='alias kd; kubectl describe'
alias klo='alias klo; kubectl logs -f'
# https://github.com/ahmetb/kubectl-aliases/blob/master/.kubectl_aliases

# Helm

# Git
alias gs='git status'
alias gc='git commit -m'
alias gpullmaster='alias gpullmaster; git pull --rebase origin master'
alias gpushw='alias gpushw; git push origin HEAD:refs/for/master'
alias gpushh='alias gpushh; git push origin master'
alias greset='alias greset; git reset --hard origin/master'

parse_git_branch() {
 git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/'
}
if [ "$color_prompt" = yes ]; then
 PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[01;31m\] $(parse_git_branch)\[\033[00m\]\$ '
else
 PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w$(parse_git_branch)\$ '
fi

# THE SIX LINES BELOW are the default prompt and the unset (which were in the original .bashrc)
#if [ "$color_prompt" = yes ]; then
#    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
#else
#    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
#fi
#unset color_prompt force_color_prompt

