{% if not obj.display %}
:orphan:

{% endif %}
:py:mod:`{{ obj.name }}`
=========={{ "=" * obj.name|length }}

.. py:module:: {{ obj.name }}

{% if obj.docstring %}
.. autoapi-nested-parse::

   {{ obj.docstring|indent(3) }}

{% endif %}


{% block submodules %}

{% set visible_subpackages = obj.subpackages|selectattr("display")|list %}
{% set visible_submodules = obj.submodules|selectattr("display")|list %}
{% set visible_substuffs = visible_subpackages + visible_submodules %}

{% if visible_substuffs %}

.. toctree::
   :titlesonly:
   :maxdepth: 1

{% for substuffs in visible_substuffs|sort %}
   {{ substuffs.short_name }}/index.rst

{% endfor %}

----

{% set visible_subpackages = obj.subpackages|selectattr("display")|list %}
{% set visible_submodules = obj.submodules|selectattr("display")|list %}
{% set visible_substuffs = visible_subpackages + visible_submodules %}

.. autoapisummary::

{% for substuffs in visible_substuffs|sort %}
   {{ substuffs.id }}

{% endfor %}

{% endif %}
{% endblock %}

----

{% block content %}

{% if obj.all is not none %}
{% set visible_children = obj.children|selectattr("short_name", "in", obj.all)|list %}
{% elif obj.type is equalto("package") %}
{% set visible_children = obj.children|selectattr("display")|list %}
{% else %}
{% set visible_children = obj.children|selectattr("display")|rejectattr("imported")|list %}
{% endif %}

{% if visible_children %}

{% set visible_classes = visible_children|selectattr("type", "equalto", "class")|list %}
{% set visible_functions = visible_children|selectattr("type", "equalto", "function")|list %}
{% set visible_attributes = visible_children|selectattr("type", "equalto", "data")|list %}
{% set visible_exceptions = visible_children|selectattr("type", "equalto", "exception")|list %}


{% if "show-module-summary" in autoapi_options and (visible_classes or visible_functions) %}


{% block attributes scoped %}
{% if visible_attributes %}
.. rubric:: Attribute Overview

.. autoapisummary::

{% for attribute in visible_attributes %}
   {{ attribute.id }}

{% endfor %}

{% endif %}
{% endblock %}


{% block classes scoped %}
{% if visible_classes %}
.. rubric:: Class Overview

.. autoapisummary::

{% for klass in visible_classes %}
   {{ klass.id }}

{% endfor %}

{% endif %}
{% endblock %}


{% block functions scoped %}
{% if visible_functions %}
.. rubric:: Function Overview

.. autoapisummary::

{% for function in visible_functions %}
   {{ function.id }}

{% endfor %}

{% endif %}
{% endblock %}



{% block exceptions scoped %}
{% if visible_exceptions %}
.. rubric:: Exception Overview

.. autoapisummary::

{% for function in visible_exceptions %}
   {{ function.id }}

{% endfor %}

{% endif %}
{% endblock %}

{% endif %}

----

{% if visible_attributes %}



.. rubric:: Attrubutes


{% for obj_item in visible_attributes %}
{{ obj_item.render()|indent(0) }}

----

{% endfor %}

{% endif %}


{% if visible_classes %}


.. rubric:: Classes


{% for obj_item in visible_classes %}
{{ obj_item.render()|indent(0) }}

----

{% endfor %}

{% endif %}


{% if visible_functions %}


.. rubric:: Functions


{% for obj_item in visible_functions %}
{{ obj_item.render()|indent(0) }}

----

{% endfor %}

{% endif %}


{% if visible_exceptions %}

.. rubric:: Exceptions


{% for obj_item in visible_exceptions %}
{{ obj_item.render()|indent(0) }}

----

{% endfor %}

{% endif %}



{% endif %}
{% endblock %}