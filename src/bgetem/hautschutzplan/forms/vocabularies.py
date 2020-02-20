# -*- coding: utf-8 -*-
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary

from bgetem.hautschutz import _

gefaehrdungen = SimpleVocabulary(
    [
        SimpleTerm(value=u'biologie', token=u'biologie', title=_(u'Biologische Gefährdungen')),
        SimpleTerm(value=u'chemie', token=u'chemie', title=_(u'Chemische Gefährdungen')),
        SimpleTerm(value=u'mechanik', token=u'mechanik', title=_(u'Mechanische Gefährdungen'))
    ]
)

dummy_gefahrstoffe = SimpleVocabulary(
    [
        SimpleTerm(value=u'ameisensaeure', token=u'ameisensaeure', title=u'Ameisensäure'),
        SimpleTerm(value=u'essigsaeure', token=u'essigsaeure', title=u'Essigsäure'),
        SimpleTerm(value=u'salzsaeure', token=u'salzsaeure', title=u'Salzäure'),
        SimpleTerm(value=u'zitronensaeure', token=u'zitronensaeure', title=u'Zitronensäure'),
    ]
)

biogefahr = SimpleVocabulary(
    [
        SimpleTerm(value=u'bakterien_pilze', token=u'bakterien_plize', title=u'Bakterien und Pilze'),
        SimpleTerm(value=u'bakterien_pilze_viren', token=u'bakterien_pilze_viren', title=u'Bakterien, Pilze und Viren'),
    ]
)

vocab_schichtstaerke = SimpleVocabulary(
    [
        SimpleTerm(value=u'alle', token=u'alle', title=u'alle anzeigen'),
        SimpleTerm(value=u'gering', token=u'gering', title=u'geringe Schichtstärke (max. 0,15mm)'),
        SimpleTerm(value=u'mittel', token=u'mittel', title=u'mittlere Schichtstärke (0,15mm - 0,5mm)'),
        SimpleTerm(value=u'hoch', token=u'hoch', title=u'hohe Schichtstärke (> 0,5mm)'),
    ]
)

vocab_stulpenlaenge = SimpleVocabulary(
    [
        SimpleTerm(value=u'alle', token=u'alle', title=u'alle anzeigen'),
        SimpleTerm(value=u'kurz', token=u'kurz', title=u'kurze Länge (max. 230mm)'),
        SimpleTerm(value=u'mittel', token=u'mittel', title=u'mittlere Länge (230mm - 260mm)'),
        SimpleTerm(value=u'lang', token=u'lang', title=u'lange Stulpen (> 260mm)'),
    ]
)
