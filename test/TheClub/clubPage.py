#!/usr/bin/python3
# -*- encoding: utf8 -*-
import sys, os
#import cgitb
#cgitb.enable()
from page import Page, modulename2text, text2modulename, h

clubName = "The Club"


class ClubPage(Page):
    _upperBanner = clubName
    upperBarColour = '#6060f0'
    _lowerBanner = "(dummy 'Lower banner')"
    lowerBarColour = '#000088'
    _synopsis = """dummy synopsis"""
    _detail = """dummy detail - this page is intended to be included, not displayed in itw own right!"""
    centreImage = None
    columns = None
    homePage = "/index.py"
    modulename2text, text2modulename # not used within here: we import them so
                                     # our derived classes can esily use them.

    def synopsis(self):
        return self._synopsis

    def detail(self):
        return self._detail

    def rightPanel(self):
        return self._rightPanel

    def lowerBanner(self):
        return self._lowerBanner

    def upperBanner(self):
        return h.h3 | self._upperBanner

    def upperText(self):
        return (
            h.br, """
These pages represent an example of a web-site for a club or society. 
            """,
            h.br,
            h.br,
            """
Two languages are supported: English and Dutch. Only this section is shown in both together.
The language used for the rest of the pages can be chosen by the links here:
            """,h.br,h.br,
            h.center | (h.h4 | (
                [(h.a(href=self.href(new_kw={'language': (language_code,)})) | language_names, ' ')
                    for language_code, language_names in (
                      ('EN', "English/Engels"),
                      ('NL', "Nederlands/Dutch"),
                  )
                ]
            )),

            h.em | """
Twee talen worden ondersteund: Engels en Nederlands. Alleen deze kop is getoond in beide talen.
Welke taal wordt gebruikt voor de rest van de webpagina's mag geselelcteerd worden d.m.v. 
de links hierboven.
            """, h.br, h.br,

        )

    def colourBarBox(self, header, bgcolor, content):
        return (
            h.table(width="100%",cellpadding="0",
                            cellspacing="0")| (
                h.tr | (
                    h.th(bgcolor=bgcolor, valign="top") | (
                        h.font(color="#FFFFFF", size="2") | (h.h3 | header),
                    ),
                ),
                h.tr | (
                    h.td | content,
                ),
            )
        )

    def lowerText(self):
        return (
            h | self.synopsis(),
            h | self.detail()
        )
    

    def body(self):
        return (
            self.colourBarBox(h | self.upperBanner(), self.upperBarColour,
                    h | self.upperText()),
            self.colourBarBox(h | self.lowerBanner(), self.lowerBarColour,
                    h | self.lowerText()),
    )
if __name__=="__main__":
    ClubPage().main()
