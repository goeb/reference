" local syntax file - set colors on a per-machine basis:
" vim: tw=0 ts=4 sw=4
" Vim color file
" Maintainer:	Ron Aaron <ron@ronware.org>
" Last Change:	2003 May 02

hi clear
set background=dark
if exists("syntax_on")
  syntax reset
endif
let g:colors_name = "fh"
hi Normal		  guifg=black  guibg=white
hi Scrollbar	  guifg=darkcyan guibg=cyan
hi Menu			  guifg=black guibg=cyan
hi SpecialKey	  term=bold  cterm=bold  ctermfg=darkred  guifg=Blue
hi NonText		  term=bold  cterm=bold  ctermfg=darkred  gui=bold	guifg=Blue
hi Directory	  term=bold  cterm=bold  ctermfg=brown	guifg=Blue
hi ErrorMsg		  term=standout  cterm=bold  ctermfg=grey  ctermbg=blue  guifg=White  guibg=Red
hi Search		  term=reverse	ctermfg=white  ctermbg=red	guifg=white  guibg=Red
hi MoreMsg		  term=bold  cterm=bold  ctermfg=darkgreen	gui=bold  guifg=blue
hi ModeMsg		  term=bold  cterm=bold  gui=bold  guifg=White	guibg=lightBlue
hi LineNr		  term=underline  cterm=bold  ctermfg=darkcyan	guifg=blue
hi Question		  term=standout  cterm=bold  ctermfg=darkgreen	gui=bold  guifg=blue
hi StatusLine	  term=bold,reverse  cterm=bold ctermfg=lightblue ctermbg=white gui=bold guifg=blue guibg=white
hi StatusLineNC   term=reverse	ctermfg=white ctermbg=lightblue guifg=white guibg=lightblue
hi Title		  term=bold  cterm=bold  ctermfg=darkmagenta  gui=bold	guifg=Magenta
hi Visual		  term=reverse	cterm=reverse  gui=reverse
hi WarningMsg	  term=standout  cterm=bold  ctermfg=blue  guifg=Red
hi Cursor		  guifg=bg	guibg=fg
hi Comment		  term=bold  ctermfg=DarkBlue  guifg=#80a0ff
hi Constant		  term=underline  ctermfg=DarkBlue  guifg=#ffa0a0
hi Special		  term=bold  cterm=bold ctermfg=darkblue  guifg=Orange
hi Identifier	  ctermfg=black  guifg=#40ffff
hi Statement	  term=bold  cterm=bold ctermfg=black	gui=bold  guifg=black
hi PreProc		  term=underline  ctermfg=darkblue	guifg=#ff80ff
hi Type			  term=underline  cterm=bold ctermfg=black  gui=bold  guifg=black
hi Error		  term=reverse	ctermfg=darkcyan  ctermbg=black  guifg=Red	guibg=Black
hi Todo			  term=standout  ctermfg=black	ctermbg=darkcyan  guifg=Blue  guibg=blue
hi DiffText		  term=reverse cterm=bold ctermbg=Red gui=bold guibg=LightRed
hi DiffAdd		  term=bold ctermbg=LightBlue guibg=LightBlue
hi DiffChange	  term=bold ctermbg=LightMagenta guibg=LightMagenta
hi DiffDelete	  term=bold ctermfg=Blue ctermbg=LightCyan gui=bold guifg=Blue guibg=LightCyan
hi Folded         term=bold ctermbg=LightGrey cterm=bold ctermfg=darkblue  guifg=Orange


hi link IncSearch		Visual
hi link String			Constant
hi link Character		Constant
hi link Number			Constant
hi link Boolean			Constant
hi link Float			Number
hi link Function		Identifier
hi link Conditional		Statement
hi link Repeat			Statement
hi link Label			Statement
hi link Operator		Statement
hi link Keyword			Statement
hi link Exception		Statement
hi link Include			PreProc
hi link Define			PreProc
hi link Macro			PreProc
hi link PreCondit		PreProc
hi link StorageClass	Type
hi link Structure		Type
hi link Typedef			Type
hi link Tag				Special
hi link SpecialChar		Special
hi link Delimiter		Special
hi link SpecialComment	Special
hi link Debug			Special
