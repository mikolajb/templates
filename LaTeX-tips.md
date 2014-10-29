LaTeX tips
==========

Beamer
------

### Backgroud
`
\usebackgroundtemplate{\includegraphics[width=\paperwidth,height=\paperheight,keepaspectratio]{picture.jpg}}
`
### Vertical center
`
\usebackgroundtemplate{
  \vbox to \paperheight
  {\vfil\hbox to \paperwidth
    {\hfil\includegraphics[width=\paperwidth,height=\paperheight,keepaspectratio]{picture.jpg}
      \hfil}
  \vfil}
}
`

Ordinal numbers
---------------
Packages:
* nth
* engord (more advenced)
