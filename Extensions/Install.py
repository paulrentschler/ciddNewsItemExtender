from Products.ciddNewsItemExtender.extender import SynopsisExtender

def install(portal):
    """Register the extender so it takes effect on this Plone site."""
    sm = portal.getSiteManager()  # Local components are not per-container; they are per-sitemanager. It just so happens that every Plone site has a sitemanager. Hooray.
    sm.registerAdapter(SynopsisExtender, name='ciddNewsItemSynopsis')
    
    return "Registered the extender at the root of the Plone site."

def uninstall(portal):
    """Unregister the schema extender so it no longer takes effect on this Plone site."""
    sm = portal.getSiteManager()
    sm.unregisterAdapter(SynopsisExtender, name='ciddNewsItemSynopsis')
    
    return "Removed the extender from the root of the Plone site."
