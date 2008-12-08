from archetypes.schemaextender.field import ExtensionField
from archetypes.schemaextender.interfaces import IOrderableSchemaExtender
from Products.Archetypes.atapi import *
from Products.ATContentTypes.interface.news import IATNewsItem
from zope.interface import implements
from zope.component import adapts

# Any field you tack on must have ExtensionField as its first subclass:
class _StringExtensionField(ExtensionField, StringField):
    pass

class _LinesExtensionField(ExtensionField, LinesField):
    pass

class _IntegerExtensionField(ExtensionField, IntegerField):
    pass

class SynopsisExtender(object):
    """Adapter that adds fields to News Items so they can be used for research paper synopses."""
    adapts(IATNewsItem)
    implements(IOrderableSchemaExtender)
    
    _fields = [
            _StringExtensionField('paperUrl',
                required=False,
                searchable=True,
                validators=('isURL',),
                widget=StringWidget(
                    label=u"Web address of the paper",
                    description=u"Where the abstract or full text can be found. Example: http://www.example.com",
                    ),
                ),
            
            _LinesExtensionField('paperAuthors',
                required=False,
                searchable=True,
                widget=LinesWidget(
                    label=u"Author(s) of the paper, one per line",
                    description=u"Example: Bloggs JB",
                    ),
                ),
            
            _IntegerExtensionField('paperYear',
                required=False,
                searchable=True,
                widget=IntegerWidget(
                    label=u"Publication year",
                    description=u"Example: 2008",
                    ),
                ),
            
            _StringExtensionField('paperTitle',
                required=False,
                searchable=True,
                widget=StringWidget(
                    label=u"Title of the paper",
                    description=u"Please don't capitalize every word; only use capital letters for proper nouns and abbreviations",
                    ),
                ),
            
            _StringExtensionField('paperJournal',
                required=False,
                searchable=True,
                widget=StringWidget(
                    label=u"Journal name",
                    description=u"Example: Journal of Experimental Biology",
                    ),
                ),
            
            _StringExtensionField('paperJournalRef',
                required=False,
                searchable=True,
                widget=StringWidget(
                    label=u"Volume and page numbers",
                    description=u"Example: 83: 157-162",
                    ),
                ),
            
            _StringExtensionField('paperDoi',
                required=False,
                searchable=True,
                widget=StringWidget(
                    label=u"doi",
                    description=u"The Digital Object Identifier of the paper (see http://www.doi.org/ for more info)",
                    ),
                ),
            _StringExtensionField('pressreleaseUrl',
                required=False,
                searchable=True,
                validators=('isURL',),
                widget=StringWidget(
                    label=u"Press release web address",
                    description=u"If there is a press release about this paper, enter the URL here. Example: http://www.someurl.com",
                    ),
                ),
        ]
    
    def __init__(self, newsItem):
        pass
    
    def getFields(self):
        return self._fields
    
    def getOrder(self, original):
        new = original.copy()  # contract requires us to make a new one
        defaultSchemaFields = new['default']  # fields from the "default" schemata
        return new
