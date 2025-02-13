if status is-interactive
    # Commands to run in interactive sessions can go here

    fish_add_path $HOME/bin
    fish_add_path $HOME/.local/bin
    fish_add_path /opt/homebrew/bin
    fish_add_path $HOME/.emacs.d/bin
    fish_add_path $HOME/dev/roc
    fish_add_path /opt/homebrew/opt/llvm/bin
    set -gx CC /opt/homebrew/opt/llvm/bin/clang
    set -gx CXX /opt/homebrew/opt/llvm/bin/clang++
    alias gcc /opt/homebrew/opt/llvm/bin/clang
    alias g++ /opt/homebrew/opt/llvm/bin/clang++
    zoxide init fish --cmd cd | source

    theme_gruvbox dark hard
end

~/.local/bin/mise activate fish | source
source "$HOME/.cargo/env.fish"
