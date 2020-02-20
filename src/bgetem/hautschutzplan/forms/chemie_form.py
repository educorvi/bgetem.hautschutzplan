# -*- coding: utf-8 -*-
from zope import schema
from z3c.form import button, form, field
from z3c.form.browser.radio import RadioFieldWidget
from z3c.form.browser.checkbox import CheckBoxFieldWidget
from plone.supermodel import model
from plone.autoform import directives
from plone.autoform.form import AutoExtensibleForm
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.formwidget.autocomplete import AutocompleteMultiFieldWidget

from bgetem.hautschutzplan import _

from bgetem.hautschutzplan.forms.vocabularies import biogefahr, vocab_schichtstaerke, vocab_stulpenlaenge, dummy_gefahrstoffe

class IChemieForm(model.Schema):

    gefahrstoffe = schema.List(title=u"Chemische Gefährdungen",
                            description=u"Folgende Gefahrstoffe kommen bei dieser Tätigkeit zur Anwendung:",
                            value_type=schema.Choice(vocabulary=dummy_gefahrstoffe),
                            required=False)

    model.fieldset(
         'weitere-gefaehrdungen',
        label=_(u"Weitere Gefährdungen"),
        fields=['biogefaehrdung', 'mechanik']
        )

    biogefaehrdung = schema.Choice(title=u"Mit folgenden biologischen Gefährdungen ist diese Tätigkeit verbunden:",
                            vocabulary=biogefahr,
                            required=True)

    mechanik = schema.Bool(title=u"Mechanische Gefährdungen",
                            description=u"(Beispiel: Arbeit mit spitzen oder scharfkantigen Gegenstände, Stosseinwirkung)",
                            required=False)

    model.fieldset(
         'weitere-anforderungen',
        label=_(u"Weitere Anforderungen"),
        fields=['schichtstaerke', 'stulpenlaenge']
        )

    #directives.widget('gefaehrdung', RadioFieldWidget)
    schichtstaerke = schema.Choice(title=u"Schichtstärke des Handschuhs",
                            description=u"Je nach Tätigkeit spielt die Schichtstärke des Handschuhs eine Rolle bei der Frage wie\
                                          feinfühlig gearbeitet werden muss. Bitte wählen Sie hier die gewünschte Schichtstärke des Handschuhs.",
                            vocabulary=vocab_schichtstaerke,
                            default='alle',
                            required=False)

    #directives.widget('gefaehrdung', RadioFieldWidget)
    stulpenlaenge = schema.Choice(title=u"Stulpenlänge des Handschuhs",
                            description=u"Wenn bei der von Ihnen beschriebenen Tätigkeit die Länge der Stulpen ein Rolle spielt,\
                                          können Sie diese hier für Ihre Produktauswahl angeben.",
                            vocabulary=vocab_stulpenlaenge,
                            default='alle',
                            required=False)
  

class ChemieForm(AutoExtensibleForm, form.Form):

    label = u"Tätigkeit mit chemischer Gefährdung"
    description = u"Hand -und Hautschutzprodukte für diese Tätigkeit suchen"
    ignoreContext = True
    #enable_form_tabbing  = False #Disable Tabs in Form
    default_fieldset_label = u"Standard" #Beschriftung des Standard-Fieldsets
 
    #fields = field.Fields(ITaetigkeitForm)
    schema = IChemieForm
    #template = ViewPageTemplateFile('mytemplate.pt')

    def updateWidgets(self):
        super(ChemieForm, self).updateWidgets()
        #self.widgets["title"].value = self.context.title

    @button.buttonAndHandler(u'Weiter')
    def handleApply(self, action):
        data, errors = self.extractData()
        import pdb;pdb.set_trace()
        # do something

    @button.buttonAndHandler(u'Abbrechen')
    def handleCancel(self, action):
        data, errors = self.extractData()
        import pdb;pdb.set_trace()
        # do something

