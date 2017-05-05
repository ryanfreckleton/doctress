########
Doctress
########

*Making documentation handsome.*
*Mingle code and documentation*
*Documentation for humans*
*Low-carb documentation and presentations*
*Beautiful documentation, organized code*

Inspired by the idio plugin of dexy, this is toolset built on RestructuredText
to allow for a type of "trap door" literate programming and documentation.
Source code is annotated with block names and end statements and can be
interspersed with prose, results of tests and metrics in a single document to
be rendered into HTML, LaTeX or other formats.

Usage
=====
::

    doctress <inputfile> [-o outfile]

Run doctress on the rst file ``<inputfile>`` by default output goes on stdout,
but can be specified with ``-o``.

Input file can also be set to ``-`` to read from ``stdin``.

Options
-------

::

    doctress <inputfile> -t beamer [-o outfile]

Installation
============
Requirements
------------

Features
========
 - Multi-lingual (Python, C, any source code)
 - Multiple outputs:

   - LaTeX, ConTeXt (eventually), beamer, HTML

The code (in ``file.code``) is broken into blocks such that::

    ### Block Name
    Code goes here

Then that's picked up by the directive::

    .. see:: example.py Block Name

The filetype is guessed by the extension, but can be added with a :code:
option after the directive. ``Block Name`` is found by looking for three
comment characters. I.e.::

    ### python
    /// C++
    %%% MATLAB
    ;;; lisp
    --- Haskell

Trailing comment characters are stripped as is white space, for example, the
following four statements are equivalent::

    ### Block
    ### Block ###
    ###       Block ##
    ###    Block     ########

This directive automatically dedents the code to flow nicely with the rest of
the document.

It may be useful in the future to automatically set tabstops and/or do
something like `elastic tabstops`_.

.. _elastic tabstops: http://nickgravgaard.com/elastic-tabstops/

Requirements
============
Compatibility
=============
License
=======

Questions
=========
 - Why does this exist?

    - To make it easier for me to do literate programming, make presentations
      and keep a knowledge base of code.
    - To have something fun to show people and something to make code analysis
      more enjoyable. To give something to the software development community
      that is beneficial.

 - Why should someone use this tool?

   - Because it's simple, extensible, fast and makes beautiful output,
     including integration of visualization, testing and metrics.
   - It's fun! It allows you to analyze and explain things.

 - How can you add plugins and customize it for your own use?

   - Custom output formats
   - Custom directives
   - Integrating with metrics
   - Integrating with visualizations

 - How simple can we be?

   - Use docutils extensively
   - Steal from sphinx
   - use doit when necessary
   - Support both Python 2 and 3
   - Look nice

Architecture
============
Doctress is built on top of docutils and doit. Docutils has a simple fundamental
architecture:

Docutils
--------
Parser
    Custom directives and roles.

    Directive class
        Inline
        TextElement

        attributes: Argument details
        Option names
        Whether it has content

        self.assert_has_content()
        self.content
        self.arguments
        self.final_argument_whitespace

        Node children?

    Node class

Transform
    Combining information from different nodes into a more appropriate tree.
Writer
    Translator?
    Outputting to a specific format

doit
----
doit is used to handle dependency management and running against multiple
files. It'll also be how to integrate into other tools.

Plugins
-------
Not sure about plugins yet. Definitely should be pip installable and easy to
make.

- http://pluginbase.pocoo.org/
- https://github.com/dexy/cashew
- http://yapsy.sourceforge.net/
- http://termie.pbworks.com/w/page/20571923/SprinklesPy
- http://docs.openstack.org/developer/stevedore/patterns_loading.html
- http://stackoverflow.com/questions/932069/building-a-minimal-plugin-architecture-in-python

Authors
=======
