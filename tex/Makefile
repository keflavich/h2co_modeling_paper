# latex Makefile
texpath=/usr/texbin/
PDFLATEX=${texpath}pdflatex -halt-on-error -synctex=1 --interaction=nonstopmode
LATEX=${PDFLATEX}
BIBTEX=bibtex
DVIPS=dvips
PS2PDF=ps2pdf

all: modeling_paper

modeling_paper: 
	@rm -f modeling_paper*.aux modeling_paper*.bbl modeling_paper*.blg modeling_paper*.dvi modeling_paper*.log modeling_paper*.lot modeling_paper*.lof
	${LATEX} modeling_paper.tex
	${BIBTEX} modeling_paper
	${LATEX} modeling_paper.tex
	${BIBTEX} modeling_paper
	${LATEX} modeling_paper.tex
