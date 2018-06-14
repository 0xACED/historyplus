# historyplus

```
shopt -s extdebug

preexec_invoke_exec () {
    [ -n "$COMP_LINE" ] && return  # do nothing if completing
    [ "$BASH_COMMAND" = "$PROMPT_COMMAND" ] && return # don't cause a preexec for $PROMPT_COMMAND
    local this_command=`HISTTIMEFORMAT= history 1 | sed -e "s/^[ ]*[0-9]*[ ]*//"`;

    if [ "shopt -u extdebug" == "$this_command" ]; then
        return 0
    fi

    $this_command

    log="$(whoami),$(date +%s),$(pwd),$this_command"

    #printf "$(whoami),$(date +%s),$(pwd),$this_command,\n" >> ~/.historyplus

    echo "$log" >> ~/.historyplus

    return 1 # This prevent executing of original command
}
trap 'preexec_invoke_exec' DEBUG

```
