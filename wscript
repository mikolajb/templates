#! /usr/bin/env python

import os

top = '.'
out = os.path.join('/tmp', os.path.basename(os.getcwd()))
DOCUMENT_NAME = 'paper'

def configure(conf):
    conf.load('tex')
    if not conf.env.XELATEX:
        conf.fatal('could not find the program xelatex')
    conf.find_program('dot', var="DOT")

def build(bld):
    for i in bld.path.ant_glob('img/**/*.dot'):
        bld(rule='${DOT} -Teps -o${TGT[0].get_bld().abspath()} ${SRC[0].abspath()}',
            source=i,
            target=i.change_ext('.eps'),
            name='graphviz')
    bld.add_group()

    pics = map(lambda i: os.path.join("img", i),
               filter(lambda i: i.endswith("pdf"),
                      os.listdir("img")))
    for i in pics:
        bld(rule='cp ${SRC} ${TGT}',
            source=bld.path.make_node(i),
            target=bld.path.get_bld().make_node(i))
    bld.add_group()

    bld(
        features='tex',
        type='xelatex',
        source='%s.tex' % DOCUMENT_NAME,
        outs='pdf',
        prompt=1
    )

    bld(rule="emacs -batch --visit=${SRC} " \
        "--no-site-file --no-site-lisp " \
        "--load=$HOME/.emacs.d/orgmode-settings.el " \
        "--eval \"(let ((default-directory \\\"${TGT[0].parent.abspath()}\\\")) (org-export-to-file 'latex \\\"${TGT}\\\"))\"",
        source='%s.org' % DOCUMENT_NAME,
        target='%s.tex' % DOCUMENT_NAME)

    bld(features='tex',
        type='xelatex',
        source='%s.tex' % DOCUMENT_NAME,
        outs='pdf',
        prompt=1)
