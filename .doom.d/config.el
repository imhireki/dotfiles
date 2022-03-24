;; Editor
(setq doom-font (font-spec :family "Caskaydia Cove Nerd Font" :size 14))
(setq doom-theme 'doom-dracula)
(setq display-line-numbers-type t)
(setq delete-selection-mode t)
;;Background Opacity
;;(set-frame-parameter (selected-frame) 'alpha '(70 70))
;;(add-to-list 'default-frame-alist '(alpha 70 70))

;; Documents
(setq org-directory "~/documents/org/")
(setq fancy-splash-image "~/pictures/splash.png")

;; Hook
(add-hook 'prog-mode-hook 'rainbow-delimiters-mode)
(add-hook 'prog-mode-hook 'highlight-numbers-mode)

;; Syntax HighLight
(use-package! tree-sitter
  :config
  (require 'tree-sitter-langs)
  (global-tree-sitter-mode)
  (add-hook 'tree-sitter-after-on-hook #'tree-sitter-hl-mode))
