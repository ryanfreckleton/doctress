######
Dapper
######

*Making documentation handsome.*

Inspired by the idio plugin of dexy, this is toolset built on RestructuredText
to allow for a type of "trap door" literate programming and documentation.
Source code is annotated with block names and end statements and can be
interspersed with prose, results of tests and metrics in a single document to
be rendered into HTML, LaTeX or other formats.

Usage
=====
::

    dapper <inputfile> [-o outfile]

Run dapper on the rst file ``<inputfile>`` by default output goes on stdout,
but can be specified with ``-o``.

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

This directive automatically dedents the code to minimize its size.

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
