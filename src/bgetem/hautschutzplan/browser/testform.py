from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from z3c.form.browser.radio import RadioFieldWidget
from z3c.form.browser.checkbox import CheckBoxFieldWidget
from zope.interface import Interface
from zope import schema
from plone.supermodel import model
from plone.autoform import directives
from z3c.form import button, form, field


items = [ ('value1', u'This is label for item'), ('value2', u'This is label for value 2')]
terms = [ SimpleTerm(value=pair[0], token=pair[0], title=pair[1]) for pair in items ]

myVocabulary = SimpleVocabulary(terms)


class IFormSchema(Interface):
    field1 = schema.TextLine(title=u"A field")
    field2 = schema.Int(title=u"Another field")

    field3 = schema.Text(title=u"Text")
    field4 = schema.List(title=u"Liste", value_type=schema.TextLine())

    field5 = schema.Choice(title="Auswahl", vocabulary=myVocabulary)

    field6 = schema.List(title="Mehrfachauswahl", value_type=schema.Choice(title="Auswahl", vocabulary=myVocabulary))
    



class TestForm(form.Form):

    label = u"What's your name?"
    description = u"Simple, sample form"
    ignoreContext = True
 
    fields = field.Fields(IFormSchema)
    fields["field5"].widgetFactory = RadioFieldWidget
    fields["field6"].widgetFactory = CheckBoxFieldWidget
    #template = ViewPageTemplateFile('mytemplate.pt')

    def updateWidgets(self):
        super(TestForm, self).updateWidgets()
        self.widgets["field1"].value = u'klaus'
        #id = self.request.get('id', None)
        #if id:
        #    self.widgets["memberID"].value = id.encode('utf-8')

    @button.buttonAndHandler(u'Submit')
    def handleApply(self, action):
        data, errors = self.extractData()
        import pdb;pdb.set_trace()
        # do something
