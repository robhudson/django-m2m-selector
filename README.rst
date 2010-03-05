===================
Django M2M Selector
===================

A bit of Javascript and CSS to progressively enhance Django's default
many-to-many form widget.

This uses jQuery and jQuery UI to hide the default multi-select box and adds a
drag-and-drop interface for selecting items.  The drag-and-drop events update
the multi-select input element behind the scenes so no change is needed to your
Django view code.

Screenshots
===========

With Javascript disabled, you see the default Django form::

.. image:: http://github.com/downloads/robhudson/django-m2m-selector/js-off.png

WIth Javascript enabled, you get the drag-and-drop interface::

.. image:: http://github.com/downloads/robhudson/django-m2m-selector/js-on.png

Future Plans
============

* A filter while typing box, similar to github's repo box.
* Add multi-select support and arrows to move from one box to another.
* Double click events that move the item to the other box.
* YOUR IDEA HERE!

Dependencies
============

Requires:

* Django
* jQuery
* jQuery UI

