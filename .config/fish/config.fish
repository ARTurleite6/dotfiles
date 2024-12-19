if status is-interactive
    # Commands to run in interactive sessions can go here

    fish_add_path $HOME/bin
    fish_add_path $HOME/.local/bin
    fish_add_path /opt/homebrew/bin
    zoxide init fish --cmd cd | source

    theme_gruvbox dark hard
end

~/.local/bin/mise activate fish | source
source "$HOME/.cargo/env.fish"
