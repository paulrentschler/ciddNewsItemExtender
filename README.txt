Overview
########
Created by Catherine Williams to amend the News Item schema for use on the CIDD website
Intended for use with the ciddtheme product

Product Summary
########
* Adds extra fields to the News Item content type, prompting for specific details of research papers in the news (e.g. journal details)
* If completed, these extra fields displayed by the following templates in ciddtheme:
- synopsis_view.pt
- collection portlet 

To install this product
########
* Put it in a relevant Products directory of your Zope instance (exactly where this is will depend on how you installed Zope and Plone)
* (Re)start Zope
* In site setup -> Add/Remove Products, click the box next to 'ciddPeopleExtender', then click the 'Install' button

Changes to make in the ZMI for this product to be set up correctly for the CIDD website
########
If you want synopsis view to be the default view for news items (this is the case on the CIDD website), go into portal_types and ensure that it is entered:
* in the list of available view methods
* as the default view method
(this should happen automatically on installing the ciddtheme product)