######
Dapper
######

*Making documentation handsome.*

This started out as a simpler dexy clone.

Features
========
 - Multi-lingual (Python, C, any source code)
 - Multiple outputs:

   - LaTeX, ConTeXt (eventually), beamer, HTML

RST, Sphinx directives (if possible), literal includes.

Aims to be a literate programming tool

Multi-format output

Tool to do literate programming in Python 'backwards', separate source,
interleaved with code.

The code (in ``file.code``) is broken into blocks such that::

    ### Block Name

    Code goes here

Then that's picked up by the directive::

    ..include:: file.code
    :start-after: ### Block Name
    :end-before: ###
    :code: the-language


Questions
=========
 - Why does this exist?

    - To make it easier for me to do literate programming, make presentations
      and keep a knowledge base of code.

 - Why should someone use this tool?

   - Because it's simple, extensible, fast and makes beautiful output,
     including integration of visualization, testing and metrics.

 - How do you use this?

   - ``dapper file.rst -o file.html``

 - How can you add plugins and customize it for your own use?

   - TBD

 - How simple can we be?

   - Use docutils extensively
   - Steal from sphinx
   - use doit when necessary
   - Support both Python 2 and 3
   - Look nice

Architecture
============
Docutils
--------
Parser
~~~~~~
Custom directives and roles.

Transform
~~~~~~~~~
Combining information from different nodes into a more appropriate tree.

Writer
~~~~~~
Outputting to a specific format

Examples
========

.. include::  hello.py
   :code: python
