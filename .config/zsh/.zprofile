# Add local binaries to dmenu
export PATH="$HOME/.local/bin/:$PATH"

# XDG
export XDG_DATA_HOME="$HOME/.local/share"
export XDG_CONFIG_HOME="$HOME/.config"
export XDG_STATE_HOME="$HOME/.local/state"
export XDG_CACHE_HOME="$HOME/.cache"
# Xorg
export XAUTHORITY="$XDG_RUNTIME_DIR/Xauthority"

# Nvidia
export CUDA_CACHE_PATH="$XDG_CACHE_HOME/nvidia"
export __GL_SHADER_DISK_CACHE_PATH="$XDG_CACHE_HOME/nvidia"

if [ -z "${DISPLAY}" ] && [ "${XDG_VTNR}" -eq 1 ]; then
    exec startx "$XDG_CONFIG_HOME/X11/xinitrc"
fi

