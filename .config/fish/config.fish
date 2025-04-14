if status is-interactive
    # Commands to run in interactive sessions can go here

    set -x VCPKG_ROOT $HOME/dev/vcpkg
    fish_add_path $HOME/.local/bin
    fish_add_path $VCPKG_ROOT

    alias config "/usr/bin/git --git-dir=$HOME/.dotfiles --work-tree=$HOME"

    zoxide init fish --cmd cd | source

    theme_gruvbox dark hard
end

~/.local/bin/mise activate fish | source
source "$HOME/.cargo/env.fish"
