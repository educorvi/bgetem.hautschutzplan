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

from bgetem.hautschutzplan.forms.vocabularies import gefaehrdungen, dummy_gefahrstoffe

class ITaetigkeitForm(model.Schema):

    title = schema.TextLine(title=u"Name der Tätigkeit",
                            required=True)

    description = schema.TextLine(title=u"Kurzbeschreibung der Tätigkeit",
                            required=False)

    shorttext = schema.Text(title=u"Beschreibung der Tätigkeit",
                            description=u"Bitte beschreiben Sie hier die Tätigkeit etwas ausführlicher.",
                            required=False)

    #model.fieldset(
    #     'gefahrdung',
    #    label=_(u"Gefährdung"),
    #    fields=['gefaehrdung']
    #    )


    #directives.widget('gefaehrdung', RadioFieldWidget)
    gefaehrdung = schema.Choice(title=u"Primäre Gefährdung",
                            description=u"Bitte wählen Sie hier die primäre Gefährdung bei dieser Tätigkeit aus.",
                            vocabulary=gefaehrdungen,
                            required=True)

    #directives.widget('gefahrstoffe', AutocompleteMultiFieldWidget)
    #gefahrstoffe = schema.List(title=u"Gefahrstoffe",
    #                        description=u"Bitte auswählen",
    #                        value_type=schema.Choice(vocabulary=dummy_gefahrstoffe),
    #                        required=False)


class TaetigkeitForm(AutoExtensibleForm, form.Form):

    label = u"Hautgefährdende Tätigkeit"
    description = u"Bitte beschreiben Sie hier die hautgefährdende Tätigkeit"
    ignoreContext = True
    #enable_form_tabbing  = False #Disable Tabs in Form
    default_fieldset_label = u"Standard" #Beschriftung des Standard-Fieldsets
 
    #fields = field.Fields(ITaetigkeitForm)
    schema = ITaetigkeitForm
    #template = ViewPageTemplateFile('mytemplate.pt')

    def updateWidgets(self):
        super(TaetigkeitForm, self).updateWidgets()
        self.widgets["title"].value = self.context.title
        #id = self.request.get('id', None)
        #if id:
        #    self.widgets["memberID"].value = id.encode('utf-8')

    @button.buttonAndHandler(u'Weiter')
    def handleApply(self, action):
        data, errors = self.extractData()
        import pdb;pdb.set_trace()
        # do something
