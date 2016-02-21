�
��bVc           @   s�  d  Z  d d l m Z d Z d Z d Z d Z d d l m Z m	 Z	 d d l
 Z
 d d l Z d d l Z d d l Z d d l Z y d d	 l m Z Wn e k
 r� i  Z n Xy e Wn! e k
 r� d d
 l m Z n Xe j d � e _ e j d � j e _ d Z d �  Z d e f d �  �  YZ d e e f d �  �  YZ d e f d �  �  YZ d e f d �  �  YZ  d e f d �  �  YZ! d e f d �  �  YZ" d e f d �  �  YZ# d f  d �  �  YZ$ d e% f d  �  �  YZ& d! �  Z' d" e# e f d# �  �  YZ( d$ e( f d% �  �  YZ) d& e* f d' �  �  YZ+ d( e) f d) �  �  YZ, d* e) f d+ �  �  YZ- d, e( f d- �  �  YZ. d. e( f d/ �  �  YZ/ d0 e) f d1 �  �  YZ0 d2 e, f d3 �  �  YZ1 d4 e- f d5 �  �  YZ2 d6 e. f d7 �  �  YZ3 y d d l4 Z4 Wn e k
 r�e5 Z4 n Xy d d l6 Z7 Wn e k
 r!n Xy d d l8 Z8 Wn e k
 rEn Xd8 f  d9 �  �  YZ9 e: d: k r�d d l; Z; e) e; j< � Z= e= j> �  GHn  d S(;   s�  Beautiful Soup
Elixir and Tonic
"The Screen-Scraper's Friend"
http://www.crummy.com/software/BeautifulSoup/

Beautiful Soup parses a (possibly invalid) XML or HTML document into a
tree representation. It provides methods and Pythonic idioms that make
it easy to navigate, search, and modify the tree.

A well-formed XML/HTML document yields a well-formed data
structure. An ill-formed XML/HTML document yields a correspondingly
ill-formed data structure. If your document is only locally
well-formed, you can use this library to find and process the
well-formed part of it.

Beautiful Soup works with Python 2.2 and up. It has no external
dependencies, but you'll have more success at converting data to UTF-8
if you also install these three packages:

* chardet, for auto-detecting character encodings
  http://chardet.feedparser.org/
* cjkcodecs and iconv_codec, which add more encodings to the ones supported
  by stock Python.
  http://cjkpython.i18n.org/

Beautiful Soup defines classes for two main parsing strategies:

 * BeautifulStoneSoup, for parsing XML, SGML, or your domain-specific
   language that kind of looks like XML.

 * BeautifulSoup, for parsing run-of-the-mill HTML code, be it valid
   or invalid. This class has web browser-like heuristics for
   obtaining a sensible parse tree in the face of common HTML errors.

Beautiful Soup also defines a class (UnicodeDammit) for autodetecting
the encoding of an HTML or XML document, and converting it to
Unicode. Much of this code is taken from Mark Pilgrim's Universal Feed Parser.

For more than you ever wanted to know about Beautiful Soup, see the
documentation:
http://www.crummy.com/software/BeautifulSoup/documentation.html

Here, have some legalese:

Copyright (c) 2004-2010, Leonard Richardson

All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

  * Redistributions of source code must retain the above copyright
    notice, this list of conditions and the following disclaimer.

  * Redistributions in binary form must reproduce the above
    copyright notice, this list of conditions and the following
    disclaimer in the documentation and/or other materials provided
    with the distribution.

  * Neither the name of the the Beautiful Soup Consortium and All
    Night Kosher Bakery nor the names of its contributors may be
    used to endorse or promote products derived from this software
    without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE, DAMMIT.

i����(   t
   generatorss*   Leonard Richardson (leonardr@segfault.org)s   3.0.8.1s*   Copyright (c) 2004-2010 Leonard Richardsons   New-style BSD(   t
   SGMLParsert   SGMLParseErrorN(   t   name2codepoint(   t   Sets   [a-zA-Z][-_.:a-zA-Z0-9]*s   [a-zA-Z][-_.:a-zA-Z0-9]*\s*s   utf-8c         C   s   t  j d |  � S(   s(   Build a RE to match the given CSS class.s   (^|.*\s)%s($|\s)(   t   ret   compile(   t   str(    (    s    /home/gs/python/BeautifulSoup.pyt   _match_css_classk   s    t   PageElementc           B   s  e  Z d  Z d d d � Z d �  Z d �  Z d �  Z d �  Z d �  Z	 d �  Z
 d i  d d � Z d i  d d d	 � Z d i  d d
 � Z d i  d d d � Z e Z d i  d d � Z d i  d d d � Z e Z d i  d d � Z d i  d d d � Z e Z d i  d � Z d i  d d � Z e Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d d � Z  d d � Z! RS(   se   Contains the navigational information for some part of the page
    (either a tag or a piece of text)c         C   sh   | |  _  | |  _ d |  _ d |  _ d |  _ |  j  rd |  j  j rd |  j  j d |  _ |  |  j _ n  d S(   sN   Sets up the initial relations between this element and
        other elements.i����N(   t   parentt   previoust   Nonet   nextt   previousSiblingt   nextSiblingt   contents(   t   selfR
   R   (    (    s    /home/gs/python/BeautifulSoup.pyt   setupu   s    					c         C   s�   |  j  } |  j  j |  � } t | d � rp | j  |  j  k rp | j  j | � } | rp | | k  rp | d } qp n  |  j �  | j | | � d  S(   NR
   i   (   R
   t   indext   hasattrt   extractt   insert(   R   t   replaceWitht	   oldParentt   myIndexR   (    (    s    /home/gs/python/BeautifulSoup.pyR   �   s    	
c         C   sc   |  j  } |  j  j |  � } |  j �  t |  j � } | j �  x | D] } | j | | � qE Wd  S(   N(   R
   R   R   t   listR   t   reverseR   (   R   t   myParentR   t   reversedChildrent   child(    (    s    /home/gs/python/BeautifulSoup.pyt   replaceWithChildren�   s    	

c         C   s�   |  j  r= y |  j  j |  j  j |  � =Wq= t k
 r9 q= Xn  |  j �  } | j } |  j rj | |  j _ n  | r |  j | _ n  d |  _ d | _ d |  _  |  j r� |  j	 |  j _	 n  |  j	 r� |  j |  j	 _ n  d |  _ |  _	 |  S(   s0   Destructively rips this element out of the tree.N(
   R
   R   R   t
   ValueErrort   _lastRecursiveChildR   R   R   R   R   (   R   t	   lastChildt   nextElement(    (    s    /home/gs/python/BeautifulSoup.pyR   �   s(    								c         C   s6   |  } x) t  | d � r1 | j r1 | j d } q	 W| S(   s8   Finds the last element beneath this object to be parsed.R   i����(   R   R   (   R   R"   (    (    s    /home/gs/python/BeautifulSoup.pyR!   �   s    c   	      C   s  t  | t � r. t  | t � r. t | � } n  t | t |  j � � } t | d � r� | j d  k	 r� | j |  k r� |  j	 | � } | | k r� | d } q� n  | j
 �  n  |  | _ d  } | d k r� d  | _ |  | _ n5 |  j | d } | | _ | | j _ | j �  | _ | j r(| | j _ n  | j �  } | t |  j � k r�d  | _ |  } d  } x& | s�| j } | j } | saPqaqaW| r�| | _ q�d  | _ n7 |  j | } | | _ | j r�| | j _ n  | | _ | j r�| | j _ n  |  j j | | � d  S(   NR
   i   i    (   t
   isinstancet
   basestringt   NavigableStringt   mint   lenR   R   R
   R   R   R   R   R   R   R!   R   R   (	   R   t   positiont   newChildR   t   previousChildt   newChildsLastElementR
   t   parentsNextSiblingt	   nextChild(    (    s    /home/gs/python/BeautifulSoup.pyR   �   sT    												c         C   s   |  j  t |  j � | � d S(   s2   Appends the given tag to the contents of this tag.N(   R   R(   R   (   R   t   tag(    (    s    /home/gs/python/BeautifulSoup.pyt   append�   s    c         K   s   |  j  |  j | | | | � S(   sj   Returns the first item that matches the given criteria and
        appears after this Tag in the document.(   t   _findOnet   findAllNext(   R   t   namet   attrst   textt   kwargs(    (    s    /home/gs/python/BeautifulSoup.pyt   findNext�   s    c         K   s   |  j  | | | | |  j | � S(   sb   Returns all items that match the given criteria and appear
        after this Tag in the document.(   t   _findAllt   nextGenerator(   R   R3   R4   R5   t   limitR6   (    (    s    /home/gs/python/BeautifulSoup.pyR2     s    c         K   s   |  j  |  j | | | | � S(   s{   Returns the closest sibling to this Tag that matches the
        given criteria and appears after this Tag in the document.(   R1   t   findNextSiblings(   R   R3   R4   R5   R6   (    (    s    /home/gs/python/BeautifulSoup.pyt   findNextSibling  s    c         K   s   |  j  | | | | |  j | � S(   sq   Returns the siblings of this Tag that match the given
        criteria and appear after this Tag in the document.(   R8   t   nextSiblingGenerator(   R   R3   R4   R5   R:   R6   (    (    s    /home/gs/python/BeautifulSoup.pyR;     s    c         K   s   |  j  |  j | | | | � S(   sk   Returns the first item that matches the given criteria and
        appears before this Tag in the document.(   R1   t   findAllPrevious(   R   R3   R4   R5   R6   (    (    s    /home/gs/python/BeautifulSoup.pyt   findPrevious  s    c         K   s   |  j  | | | | |  j | � S(   sc   Returns all items that match the given criteria and appear
        before this Tag in the document.(   R8   t   previousGenerator(   R   R3   R4   R5   R:   R6   (    (    s    /home/gs/python/BeautifulSoup.pyR>     s    c         K   s   |  j  |  j | | | | � S(   s|   Returns the closest sibling to this Tag that matches the
        given criteria and appears before this Tag in the document.(   R1   t   findPreviousSiblings(   R   R3   R4   R5   R6   (    (    s    /home/gs/python/BeautifulSoup.pyt   findPreviousSibling#  s    c         K   s   |  j  | | | | |  j | � S(   sr   Returns the siblings of this Tag that match the given
        criteria and appear before this Tag in the document.(   R8   t   previousSiblingGenerator(   R   R3   R4   R5   R:   R6   (    (    s    /home/gs/python/BeautifulSoup.pyRA   )  s    c         K   s2   d } |  j | | d � } | r. | d } n  | S(   sO   Returns the closest parent of this Tag that matches the given
        criteria.i   i    N(   R   t   findParents(   R   R3   R4   R6   t   rt   l(    (    s    /home/gs/python/BeautifulSoup.pyt
   findParent1  s
    c         K   s   |  j  | | d | |  j | � S(   sF   Returns the parents of this Tag that match the given
        criteria.N(   R8   R   t   parentGenerator(   R   R3   R4   R:   R6   (    (    s    /home/gs/python/BeautifulSoup.pyRD   <  s    c         K   s5   d  } | | | | d | � } | r1 | d } n  | S(   Ni   i    (   R   (   R   t   methodR3   R4   R5   R6   RE   RF   (    (    s    /home/gs/python/BeautifulSoup.pyR1   F  s
    c         K   sw  t  | t � r | } n� | d k r� | r� | r� | r� | t k rn g  | �  D] } t  | t � rO | ^ qO St  | t � r� g  | �  D]* } t  | t � r� | j | k r� | ^ q� St | | | | � } n t | | | | � } t | � }	 | �  }
 xy t rry |
 j �  } Wn t	 k
 r$Pn X| r� | j
 | � } | ro|	 j | � | rlt |	 � | k rlPqlqoq� q� W|	 S(   s8   Iterates over a generator looking for things that match.N(   R$   t   SoupStrainerR   t   Truet   TagR%   R3   t	   ResultSetR   t   StopIterationt   searchR0   R(   (   R   R3   R4   R5   R:   t	   generatorR6   t   strainert   elementt   resultst   gt   it   found(    (    s    /home/gs/python/BeautifulSoup.pyR8   M  s4    	!		c         c   s+   |  } x | d  k	 r& | j } | Vq	 Wd  S(   N(   R   R   (   R   RU   (    (    s    /home/gs/python/BeautifulSoup.pyR9   s  s    	c         c   s+   |  } x | d  k	 r& | j } | Vq	 Wd  S(   N(   R   R   (   R   RU   (    (    s    /home/gs/python/BeautifulSoup.pyR=   y  s    	c         c   s+   |  } x | d  k	 r& | j } | Vq	 Wd  S(   N(   R   R   (   R   RU   (    (    s    /home/gs/python/BeautifulSoup.pyR@     s    	c         c   s+   |  } x | d  k	 r& | j } | Vq	 Wd  S(   N(   R   R   (   R   RU   (    (    s    /home/gs/python/BeautifulSoup.pyRC   �  s    	c         c   s+   |  } x | d  k	 r& | j } | Vq	 Wd  S(   N(   R   R
   (   R   RU   (    (    s    /home/gs/python/BeautifulSoup.pyRH   �  s    	c         C   s   | p	 d } | j  d | � S(   Ns   utf-8s   %SOUP-ENCODING%(   t   replace(   R   R   t   encoding(    (    s    /home/gs/python/BeautifulSoup.pyt   substituteEncoding�  s    c         C   s�   t  | t � r* | r� | j | � } q� nc t  | t � r` | rQ | j | � } q� t | � } n- | r� |  j t | � | � } n t | � } | S(   sH   Encodes an object to a string in some encoding, or to Unicode.
        .(   R$   t   unicodet   encodeR   t
   toEncoding(   R   t   sRX   (    (    s    /home/gs/python/BeautifulSoup.pyR\   �  s    N("   t   __name__t
   __module__t   __doc__R   R   R   R   R   R!   R   R0   R7   R2   R<   R;   t   fetchNextSiblingsR?   R>   t   fetchPreviousRB   RA   t   fetchPreviousSiblingsRG   RD   t   fetchParentsR1   R8   R9   R=   R@   RC   RH   RY   R\   (    (    (    s    /home/gs/python/BeautifulSoup.pyR	   q   s@   						;				&					R&   c           B   s8   e  Z d  �  Z d �  Z d �  Z d �  Z e d � Z RS(   c         C   s2   t  | t � r t j |  | � St j |  | t � S(   s-  Create a new NavigableString.

        When unpickling a NavigableString, this method is called with
        the string in DEFAULT_OUTPUT_ENCODING. That encoding needs to be
        passed in to the superclass's __new__ or the superclass won't know
        how to handle non-ASCII characters.
        (   R$   RZ   t   __new__t   DEFAULT_OUTPUT_ENCODING(   t   clst   value(    (    s    /home/gs/python/BeautifulSoup.pyRe   �  s    c         C   s   t  j |  � f S(   N(   R&   t   __str__(   R   (    (    s    /home/gs/python/BeautifulSoup.pyt   __getnewargs__�  s    c         C   s-   | d k r |  St  d |  j j | f � d S(   s�   text.string gives you text. This is for backwards
        compatibility for Navigable*String, but for CData* it lets you
        get the string without the CData wrapper.t   strings!   '%s' object has no attribute '%s'N(   t   AttributeErrort	   __class__R^   (   R   t   attr(    (    s    /home/gs/python/BeautifulSoup.pyt   __getattr__�  s    c         C   s   t  |  � j t � S(   N(   R   t   decodeRf   (   R   (    (    s    /home/gs/python/BeautifulSoup.pyt   __unicode__�  s    c         C   s   | r |  j  | � S|  Sd  S(   N(   R[   (   R   RX   (    (    s    /home/gs/python/BeautifulSoup.pyRi   �  s    (   R^   R_   Re   Rj   Ro   Rq   Rf   Ri   (    (    (    s    /home/gs/python/BeautifulSoup.pyR&   �  s
   					t   CDatac           B   s   e  Z e d  � Z RS(   c         C   s   d t  j |  | � S(   Ns   <![CDATA[%s]]>(   R&   Ri   (   R   RX   (    (    s    /home/gs/python/BeautifulSoup.pyRi   �  s    (   R^   R_   Rf   Ri   (    (    (    s    /home/gs/python/BeautifulSoup.pyRr   �  s   t   ProcessingInstructionc           B   s   e  Z e d  � Z RS(   c         C   s;   |  } d | k r' |  j  | | � } n  d |  j | | � S(   Ns   %SOUP-ENCODING%s   <?%s?>(   RY   R\   (   R   RX   t   output(    (    s    /home/gs/python/BeautifulSoup.pyRi   �  s    (   R^   R_   Rf   Ri   (    (    (    s    /home/gs/python/BeautifulSoup.pyRs   �  s   t   Commentc           B   s   e  Z e d  � Z RS(   c         C   s   d t  j |  | � S(   Ns	   <!--%s-->(   R&   Ri   (   R   RX   (    (    s    /home/gs/python/BeautifulSoup.pyRi   �  s    (   R^   R_   Rf   Ri   (    (    (    s    /home/gs/python/BeautifulSoup.pyRu   �  s   t   Declarationc           B   s   e  Z e d  � Z RS(   c         C   s   d t  j |  | � S(   Ns   <!%s>(   R&   Ri   (   R   RX   (    (    s    /home/gs/python/BeautifulSoup.pyRi   �  s    (   R^   R_   Rf   Ri   (    (    (    s    /home/gs/python/BeautifulSoup.pyRv   �  s   RL   c           B   s  e  Z d  Z d �  Z i d d 6d d 6d d 6d d	 6d
 d 6Z e e � Z d �  Z d3 d3 d3 d � Z d �  Z	 d �  Z
 e e	 e
 � Z d d � Z e e � Z d3 d � Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d  �  Z e d! � Z d" �  Z  e! j" d# d$ d% � Z# d& �  Z$ e e% d' d( � Z& d) �  Z' e d* � Z( e e% d' d+ � Z) d3 i  e* d3 d, � Z+ e+ Z, d3 i  e* d3 d3 d- � Z- e- Z. e+ Z/ e- Z0 d3 e* d3 d. � Z1 d3 e* d/ � Z2 d0 �  Z3 d1 �  Z4 d2 �  Z5 RS(4   s=   Represents a found HTML tag with its attributes and contents.c         C   s1   i  } x$ |  j  �  D] \ } } | | | <q W| S(   s    Cheap function to invert a hash.(   t   items(   t   hRU   t   kt   v(    (    s    /home/gs/python/BeautifulSoup.pyt   _invert�  s    t   't   apost   "t   quott   &t   ampt   <t   ltt   >t   gtc         C   s�   | j  d � } |  j r2 | t k r2 t t | � S| |  j k r` |  j rU |  j | Sd | Sn� t | � d k r� | d d k r� t | � d k r� | d d k r� t t | d d � � St t | d � � Sn |  j r� d | Sd | Sd	 S(
   s�   Used in a call to re.sub to replace HTML, XML, and numeric
        entities with the appropriate Unicode characters. If HTML
        entities are being converted, any unrecognized entities are
        escaped.i   u   &%s;i    t   #t   xi   i   u   &amp;%s;N(	   t   groupt   convertHTMLEntitiesR   t   unichrt   XML_ENTITIES_TO_SPECIAL_CHARSt   convertXMLEntitiesR(   t   intt   escapeUnrecognizedEntities(   R   t   matchR�   (    (    s    /home/gs/python/BeautifulSoup.pyt   _convertEntities�  s    	""	c            s�   | j  �  _ | j | � �  _ | �  _ | d k r< g  } n  | �  _ g  �  _ �  j | | � t	 �  _
 t	 �  _ | j �  _ | j �  _ | j �  _ �  f d �  } t | �  j � �  _ d S(   s   Basic constructor.c            s(   |  \ } } | t  j d �  j | � f S(   Ns   &(#\d+|#x[0-9a-fA-F]+|\w+);(   R   t   subR�   (   t   .0Ry   t   val(   R   (    s    /home/gs/python/BeautifulSoup.pyt   <lambda>   s    	N(   Rm   t   parserClasst   isSelfClosingTagt   isSelfClosingR3   R   R4   R   R   t   Falset   hiddent   containsSubstitutionsR�   R�   R�   t   map(   R   t   parserR3   R4   R
   R   t   convert(    (   R   s    /home/gs/python/BeautifulSoup.pyt   __init__  s    						c         C   s:   t  |  j � d k r6 t |  j d t � r6 |  j d Sd  S(   Ni   i    (   R(   R   R$   R&   (   R   (    (    s    /home/gs/python/BeautifulSoup.pyt	   getString&  s    c         C   s   |  j  �  |  j | � d S(   s-   Replace the contents of the tag with a stringN(   t   clearR0   (   R   Rk   (    (    s    /home/gs/python/BeautifulSoup.pyt	   setString+  s    
u    c         C   s�   t  |  j � s d S|  j �  j } g  } |  j d } x> | | k	 ru t | t � ri | j | j �  � n  | j } q8 W| j | � S(   Nu    i    (	   R(   R   R!   R   R$   R&   R0   t   stript   join(   R   t	   separatort   stopNodet   stringst   current(    (    s    /home/gs/python/BeautifulSoup.pyt   getText2  s    c         C   s   |  j  �  j | | � S(   s�   Returns the value of the 'key' attribute for the tag, or
        the value given for 'default' if it doesn't have that
        attribute.(   t   _getAttrMapt   get(   R   t   keyt   default(    (    s    /home/gs/python/BeautifulSoup.pyR�   @  s    c         C   s#   x |  j  D] } | j �  q Wd S(   s   Extract all children.N(   R   R   (   R   R   (    (    s    /home/gs/python/BeautifulSoup.pyR�   F  s    c         C   s@   x- t  |  j � D] \ } } | | k r | Sq Wt d � � d  S(   Ns   Tag.index: element not in tag(   t	   enumerateR   R    (   R   RR   RU   R   (    (    s    /home/gs/python/BeautifulSoup.pyR   K  s    c         C   s   |  j  �  j | � S(   N(   R�   t   has_key(   R   R�   (    (    s    /home/gs/python/BeautifulSoup.pyR�   Q  s    c         C   s   |  j  �  | S(   sq   tag[key] returns the value of the 'key' attribute for the tag,
        and throws an exception if it's not there.(   R�   (   R   R�   (    (    s    /home/gs/python/BeautifulSoup.pyt   __getitem__T  s    c         C   s   t  |  j � S(   s0   Iterating over a tag iterates over its contents.(   t   iterR   (   R   (    (    s    /home/gs/python/BeautifulSoup.pyt   __iter__Y  s    c         C   s   t  |  j � S(   s:   The length of a tag is the length of its list of contents.(   R(   R   (   R   (    (    s    /home/gs/python/BeautifulSoup.pyt   __len__]  s    c         C   s   | |  j  k S(   N(   R   (   R   R�   (    (    s    /home/gs/python/BeautifulSoup.pyt   __contains__a  s    c         C   s   t  S(   s-   A tag is non-None even if it has no contents.(   RK   (   R   (    (    s    /home/gs/python/BeautifulSoup.pyt   __nonzero__d  s    c         C   s�   |  j  �  | |  j | <t } xS t d t |  j � � D]9 } |  j | d | k r6 | | f |  j | <t } q6 q6 W| s� |  j j | | f � n  | |  j  �  | <d S(   sK   Setting tag[key] sets the value of the 'key' attribute for the
        tag.i    N(   R�   t   attrMapR�   t   rangeR(   R4   RK   R0   (   R   R�   Rh   RV   RU   (    (    s    /home/gs/python/BeautifulSoup.pyt   __setitem__h  s    
c         C   sd   x] |  j  D]R } | d | k r3 |  j  j | � n  |  j �  |  j j | � r
 |  j | =q
 q
 Wd S(   s;   Deleting tag[key] deletes all 'key' attributes for the tag.i    N(   R4   t   removeR�   R�   R�   (   R   R�   t   item(    (    s    /home/gs/python/BeautifulSoup.pyt   __delitem__v  s    
c         O   s   t  |  j | | � S(   s�   Calling a tag like a function is the same as calling its
        findAll() method. Eg. tag('a') returns a list of all the A tags
        found within this tag.(   t   applyt   findAll(   R   t   argsR6   (    (    s    /home/gs/python/BeautifulSoup.pyt   __call__�  s    c         C   s~   t  | � d k rB | j d � t  | � d k rB |  j | d  � S| j d � d k rd |  j | � St d |  j | f � d  S(   Ni   RL   i����t   __i    s!   '%s' object has no attribute '%s'(   R(   t   rfindt   findRl   Rm   (   R   R/   (    (    s    /home/gs/python/BeautifulSoup.pyRo   �  s
    1c      	   C   s�   | |  k r t  St | d � s| t | d � s| t | d � s| |  j | j k s| |  j | j k s| t |  � t | � k r� t Sx> t d t |  j � � D]$ } |  j | | j | k r� t Sq� Wt  S(   s  Returns true iff this tag has the same name, the same attributes,
        and the same contents (recursively) as the given tag.

        NOTE: right now this will return false if two tags have the
        same attributes in a different order. Should this be fixed?R3   R4   R   i    (   RK   R   R3   R4   R(   R�   R�   R   (   R   t   otherRU   (    (    s    /home/gs/python/BeautifulSoup.pyt   __eq__�  s    lc         C   s   |  | k S(   sZ   Returns true iff this tag is not identical to the other tag,
        as defined in __eq__.(    (   R   R�   (    (    s    /home/gs/python/BeautifulSoup.pyt   __ne__�  s    c         C   s   |  j  | � S(   s   Renders this tag as a string.(   Ri   (   R   RX   (    (    s    /home/gs/python/BeautifulSoup.pyt   __repr__�  s    c         C   s   |  j  d  � S(   N(   Ri   R   (   R   (    (    s    /home/gs/python/BeautifulSoup.pyRq   �  s    s   ([<>]|s   &(?!#\d+;|#x[0-9a-fA-F]+;|\w+;)t   )c         C   s    d |  j  | j d � d d S(   sm   Used with a regular expression to substitute the
        appropriate XML entity for an XML special character.R�   i    t   ;(   t   XML_SPECIAL_CHARS_TO_ENTITIESR�   (   R   R�   (    (    s    /home/gs/python/BeautifulSoup.pyt   _sub_entity�  s    i    c         C   s�  |  j  |  j | � } g  } |  j r x� |  j D]� \ } } d } t | t � r� |  j ry d | k ry |  j | | � } n  d | k r� d } d | k r� | j d d � } q� n  |  j j	 |  j
 | � } n  | j | |  j  | | � |  j  | | � f � q. Wn  d }	 d }
 |  j rd }	 n
 d	 | }
 d \ } } | r[| } d | d } | d } n  |  j | | | � } |  j r�| } ng  } d } | r�d d j | � } n  | r�| j | � n  | j d | | |	 f � | r�| j d � n  | j | � | r)| r)| d d k r)| j d � n  | rE|
 rE| j | � n  | j |
 � | rw|
 rw|  j rw| j d � n  d j | � } | S(   s  Returns a string or Unicode representation of this tag and
        its contents. To get Unicode, pass None for encoding.

        NOTE: since Python's HTML parser consumes whitespace, this
        method is not certain to reproduce the whitespace present in
        the original string.s   %s="%s"s   %SOUP-ENCODING%R~   s   %s='%s'R|   s   &squot;t    s    /s   </%s>i    t    i   s   <%s%s%s>s   
i����(   i    i    (   R\   R3   R4   R$   R%   R�   RY   RW   t   BARE_AMPERSAND_OR_BRACKETR�   R�   R0   R�   t   renderContentsR�   R�   R   (   R   RX   t   prettyPrintt   indentLevelt   encodedNameR4   R�   R�   t   fmtt   closet   closeTagt	   indentTagt   indentContentst   spaceR   R]   t   attributeString(    (    s    /home/gs/python/BeautifulSoup.pyRi   �  s^    				
		c         C   s�   |  j  �  t |  j � d k r# d S|  j d } xe | d k	 r� | j } t | t � ra | j 2n  d | _ d | _ d | _	 d | _ d | _
 | } q3 Wd S(   s/   Recursively destroys the contents of this tree.i    N(   R   R(   R   R   R   R$   RL   R
   R   R   R   (   R   R�   R   (    (    s    /home/gs/python/BeautifulSoup.pyt	   decompose  s    
	
					c         C   s   |  j  | t � S(   N(   Ri   RK   (   R   RX   (    (    s    /home/gs/python/BeautifulSoup.pyt   prettify  s    c         C   s�   g  } x� |  D]� } d } t | t � r: | j | � } n. t | t � rh | j | j | | | � � n  | r� | r� | j �  } n  | r | r� | j d | d � n  | j | � | r� | j d � q� q q Wd j | � S(   s{   Renders the contents of this tag as a string in the given
        encoding. If encoding is None, returns a Unicode string..R�   i   s   
R�   N(   R   R$   R&   Ri   RL   R0   R�   R�   (   R   RX   R�   R�   R]   t   cR5   (    (    s    /home/gs/python/BeautifulSoup.pyR�     s     c         K   s;   d } |  j | | | | d | � } | r7 | d } n  | S(   sL   Return only the first child of this Tag matching the given
        criteria.i   i    N(   R   R�   (   R   R3   R4   t	   recursiveR5   R6   RE   RF   (    (    s    /home/gs/python/BeautifulSoup.pyR�   3  s
    c         K   s7   |  j  } | s |  j } n  |  j | | | | | | � S(   s�  Extracts a list of Tag objects that match the given
        criteria.  You can specify the name of the Tag and any
        attributes you want the Tag to have.

        The value of a key-value pair in the 'attrs' map can be a
        string, a list of strings, a regular expression object, or a
        callable that takes a string and returns whether or not the
        string matches for some custom definition of 'matches'. The
        same is true of the tag name.(   t   recursiveChildGeneratort   childGeneratorR8   (   R   R3   R4   R�   R5   R:   R6   RP   (    (    s    /home/gs/python/BeautifulSoup.pyR�   >  s    	c         C   s   |  j  d | d | d | � S(   NR5   R�   R:   (   R�   (   R   R5   R�   R:   (    (    s    /home/gs/python/BeautifulSoup.pyt	   fetchTextS  s    c         C   s   |  j  d | d | � S(   NR5   R�   (   R�   (   R   R5   R�   (    (    s    /home/gs/python/BeautifulSoup.pyt	   firstTextV  s    c         C   sI   t  |  d � sB i  |  _ x' |  j D] \ } } | |  j | <q" Wn  |  j S(   s^   Initializes a map representation of this tag's attributes,
        if not already initialized.R�   (   t   getattrR�   R4   (   R   R�   Rh   (    (    s    /home/gs/python/BeautifulSoup.pyR�   [  s
    	c         C   s   t  |  j � S(   N(   R�   R   (   R   (    (    s    /home/gs/python/BeautifulSoup.pyR�   e  s    c         c   sY   t  |  j � s t � n  |  j �  j } |  j d } x | | k	 rT | V| j } q7 Wd  S(   Ni    (   R(   R   RN   R!   R   (   R   R�   R�   (    (    s    /home/gs/python/BeautifulSoup.pyR�   i  s    	N(6   R^   R_   R`   R{   R�   R�   R�   R   R�   R�   R�   t   propertyRk   R�   R5   R�   R�   R   R�   R�   R�   R�   R�   R�   R�   R�   R�   Ro   R�   R�   Rf   R�   Rq   R   R   R�   R�   R�   Ri   R�   R�   R�   RK   R�   t	   findChildR�   t   findChildrent   firstt   fetchR�   R�   R�   R�   R�   (    (    (    s    /home/gs/python/BeautifulSoup.pyRL   �  sl   	

																			T			
	RJ   c           B   sJ   e  Z d  Z d i  d d � Z d �  Z d i  d � Z d �  Z d �  Z RS(   sM   Encapsulates a number of ways of matching a markup element (tag or
    text).c         K   sx   | |  _  t | t � r1 t | � | d <d  } n  | rb | rY | j �  } | j | � qb | } n  | |  _ | |  _ d  S(   Nt   class(	   R3   R$   R%   R   R   t   copyt   updateR4   R5   (   R   R3   R4   R5   R6   (    (    s    /home/gs/python/BeautifulSoup.pyR�   x  s    				c         C   s(   |  j  r |  j  Sd |  j |  j f Sd  S(   Ns   %s|%s(   R5   R3   R4   (   R   (    (    s    /home/gs/python/BeautifulSoup.pyRi   �  s    	c         C   so  d  } d  } t | t � r* | } | } n  t |  j � oF t | t � } |  j s� | s� | rt |  j | |  j � s� | rk|  j | |  j � rk| r� |  j | | � } n� t } d  } x� |  j j �  D] \ } }	 | st	 | d � r� | } qi  } x! | D] \ }
 } | | |
 <q� Wn  | j
 | � } |  j | |	 � s� t } Pq� q� W| rk| r_| } qh| } qkn  | S(   NR�   (   R   R$   RL   t   callableR3   t   _matchesRK   R4   Rw   R   R�   R�   (   R   t
   markupNamet   markupAttrsRV   t   markupt   callFunctionWithTagDataR�   t   markupAttrMapRn   t   matchAgainstRy   Rz   t	   attrValue(    (    s    /home/gs/python/BeautifulSoup.pyt	   searchTag�  s>    	
		c         C   s�   d  } t | d � ra t | t � ra x� | D]. } t | t � r, |  j | � r, | } Pq, q, Wn| t | t � r� |  j s� |  j | � } q� nO t | t � s� t | t � r� |  j	 | |  j � r� | } q� n t
 d | j � | S(   NR�   s&   I don't know how to match against a %s(   R   R   R$   RL   R&   RO   R5   R�   R%   R�   t	   ExceptionRm   (   R   R�   RV   RR   (    (    s    /home/gs/python/BeautifulSoup.pyRO   �  s$    	
c         C   s=  t  } | t k r! | d  k	 } nt | � r< | | � } n� t | t � rW | j } n  | r| t | t � r| t | � } n  t	 | d � r� | o� | j
 | � } n� t	 | d � r� | | k } nc t	 | d � r� | j | � } nB | r$t | t � r$t | t � rt | � } q$t | � } n  | s9| | k } n  | S(   NR�   R�   Rw   (   R�   RK   R   R�   R$   RL   R3   R%   RZ   R   RO   R�   R   (   R   R�   R�   t   result(    (    s    /home/gs/python/BeautifulSoup.pyR�   �  s,    N(	   R^   R_   R`   R   R�   Ri   R�   RO   R�   (    (    (    s    /home/gs/python/BeautifulSoup.pyRJ   t  s   	%	RM   c           B   s   e  Z d  Z d �  Z RS(   sT   A ResultSet is just a list that keeps track of the SoupStrainer
    that created it.c         C   s   t  j g  � | |  _ d  S(   N(   R   R�   t   source(   R   R�   (    (    s    /home/gs/python/BeautifulSoup.pyR�   �  s    (   R^   R_   R`   R�   (    (    (    s    /home/gs/python/BeautifulSoup.pyRM   �  s   c         G   s�   i  } x~ | D]v } t  | d � rL x^ | j �  D] \ } } | | | <q/ Wq t  | d � ry x% | D] } |  | | <qb Wq |  | | <q W| S(   s�   Turns a list of maps, lists, or scalars into a single map.
    Used to build the SELF_CLOSING_TAGS, NESTABLE_TAGS, and
    NESTING_RESET_TAGS maps out of lists and partial maps.Rw   R�   (   R   Rw   (   R�   R�   t   builtt   portionRy   Rz   (    (    s    /home/gs/python/BeautifulSoup.pyt   buildTagMap�  s    t   BeautifulStoneSoupc        	   B   s�  e  Z d  Z i  Z i  Z i  Z i  Z g  Z e j	 d � d �  f e j	 d � d �  f g Z
 d Z d Z d Z d Z e Z i d% d	 6d% d
 6d% d 6d% d 6d% d 6Z d d% d% e e d% d% e d � Z d �  Z d% e d � Z d �  Z d �  Z d �  Z d �  Z d �  Z e d � Z e d � Z d �  Z d d � Z  d �  Z! d �  Z" d �  Z# d �  Z$ d  �  Z% d! �  Z& d" �  Z' d# �  Z( d$ �  Z) RS(&   sb  This class contains the basic parser and search code. It defines
    a parser that knows nothing about tag behavior except for the
    following:

      You can't close a tag without closing all the tags it encloses.
      That is, "<foo><bar></foo>" actually means
      "<foo><bar></bar></foo>".

    [Another possible explanation is "<foo><bar /></foo>", but since
    this class defines no SELF_CLOSING_TAGS, it will never use that
    explanation.]

    This class is useful for parsing XML or made-up markup languages,
    or when BeautifulSoup makes an assumption counter to what you were
    expecting.s   (<[^<>]*)/>c         C   s   |  j  d � d S(   Ni   s    />(   R�   (   R�   (    (    s    /home/gs/python/BeautifulSoup.pyR�   #  s    s   <!\s+([^<>]*)>c         C   s   d |  j  d � d S(   Ns   <!i   R�   (   R�   (   R�   (    (    s    /home/gs/python/BeautifulSoup.pyR�   %  s    u
   [document]t   htmlt   xmlt   xhtmli	   i
   i   i   i    R�   c	   	      C   s_  | |  _  | |  _ | |  _ | |  _ |  j r� d |  _ | |  j k rc t |  _ t |  _	 t |  _
 q� | |  j k r� t |  _ t |  _	 t |  _
 q� | |  j k r� t |  _ t |  _	 t |  _
 q� n t |  _ t |  _	 t |  _
 t d | � |  _ t j |  � t | d � r| j �  } n  | |  _ | |  _ y |  j d | � Wn t k
 rQn Xd |  _ d S(   sV  The Soup object is initialized as the 'root tag', and the
        provided markup (which can be a string or a file-like object)
        is fed into the underlying parser.

        sgmllib will process most bad HTML, and the BeautifulSoup
        class has some tricks for dealing with some HTML that kills
        sgmllib, but Beautiful Soup can nonetheless choke or lose data
        if your data uses self-closing tags or declarations
        incorrectly.

        By default, Beautiful Soup uses regexes to sanitize input,
        avoiding the vast majority of these problems. If the problems
        don't apply to you, pass in False for markupMassage, and
        you'll get better performance.

        The default parser massage techniques fix the two most common
        instances of invalid HTML that choke sgmllib:

         <br/> (No space between name of closing tag and tag close)
         <! --Comment--> (Extraneous whitespace in declaration)

        You can pass in a custom list of (RE object, replace method)
        tuples to get Beautiful Soup to scrub your input the way you
        want.t   readt   isHTMLN(   t   parseOnlyTheset   fromEncodingt   smartQuotesTot   convertEntitiesR   t   HTML_ENTITIESR�   R�   RK   R�   R�   t   XHTML_ENTITIESt   XML_ENTITIESR�   t   instanceSelfClosingTagsR   R�   R   R�   R�   t   markupMassaget   _feedt   StopParsing(	   R   R�   R�   R   R  R  R  t   selfClosingTagsR�   (    (    s    /home/gs/python/BeautifulSoup.pyR�   6  s@    																	c         C   sR   y t  | � } Wn t k
 r$ d SXd | k o< d k n sE d S|  j | � S(   s/   This method fixes a bug in Python's SGMLParser.Ni    i   (   R�   R    t   convert_codepoint(   R   R3   t   n(    (    s    /home/gs/python/BeautifulSoup.pyt   convert_charref{  s    c         C   s4  |  j  } t | t � r6 t |  d � s~ d  |  _ q~ nH t | |  j | g d |  j d | �} | j } | j |  _ | j	 |  _	 | r� |  j
 r� t |  j
 d � s� |  j |  _
 n  x) |  j
 D] \ } } | j | | � } q� W|  `
 q� n  |  j �  t j |  | � |  j �  x# |  j j |  j k r/|  j �  qWd  S(   Nt   originalEncodingR  R�   R�   (   R�   R$   RZ   R   R   R  t   UnicodeDammitR   R  t   declaredHTMLEncodingR  t   MARKUP_MASSAGER�   t   resetR   t   feedt   endDatat
   currentTagR3   t   ROOT_TAG_NAMEt   popTag(   R   t   inDocumentEncodingR�   R�   t   dammitt   fixt   m(    (    s    /home/gs/python/BeautifulSoup.pyR  �  s,    			

c         C   sf   | j  d � s- | j  d � s- | j  d � r= t j |  | � S| j  d � s\ t j |  | � St � d S(   s�   This method routes method call requests to either the SGMLParser
        superclass or the Tag superclass, depending on the method name.t   start_t   end_t   do_R�   N(   t
   startswithR   Ro   RL   Rl   (   R   t
   methodName(    (    s    /home/gs/python/BeautifulSoup.pyRo   �  s    c         C   s"   |  j  j | � p! |  j j | � S(   se   Returns true iff the given string is the name of a
        self-closing tag according to this parser.(   t   SELF_CLOSING_TAGSR�   R  (   R   R3   (    (    s    /home/gs/python/BeautifulSoup.pyR�   �  s    c         C   sa   t  j |  |  |  j � d |  _ t j |  � g  |  _ d  |  _ g  |  _	 g  |  _
 |  j |  � d  S(   Ni   (   RL   R�   R  R�   R   R  t   currentDataR   R  t   tagStackt
   quoteStackt   pushTag(   R   (    (    s    /home/gs/python/BeautifulSoup.pyR  �  s    					c         C   s2   |  j  j �  } |  j  r+ |  j  d |  _ n  |  j S(   Ni����(   R#  t   popR  (   R   R/   (    (    s    /home/gs/python/BeautifulSoup.pyR  �  s    	c         C   sC   |  j  r |  j  j j | � n  |  j j | � |  j d |  _  d  S(   Ni����(   R  R   R0   R#  (   R   R/   (    (    s    /home/gs/python/BeautifulSoup.pyR%  �  s    	c         C   s+  |  j  r'd j |  j  � } | j |  j � d k r� t g  |  j D] } | j ^ q@ � j |  j � r� d | k rz d } q� d } n  g  |  _  |  j	 r� t
 |  j � d k r� |  j	 j s� |  j	 j | � r� d  S| | � } | j |  j |  j � |  j r| |  j _ n  | |  _ |  j j j | � n  d  S(   Nu    R�   s   
R�   i   (   R"  R�   t	   translatet   STRIP_ASCII_SPACESt   setR#  R3   t   intersectiont   PRESERVE_WHITESPACE_TAGSR�   R(   R5   RO   R   R  R   R   R   R0   (   R   t   containerClassR"  R/   t   o(    (    s    /home/gs/python/BeautifulSoup.pyR  �  s&    	%					c         C   s�   | |  j  k r d Sd } d } xT t t |  j � d d d � D]3 } | |  j | j k r? t |  j � | } Pq? q? W| s� | d } n  x# t d | � D] } |  j �  } q� W| S(   s�   Pops the tag stack up to and including the most recent
        instance of the given tag. If inclusivePop is false, pops the tag
        stack up to but *not* including the most recent instqance of
        the given tag.Ni    i   i����(   R  R   R�   R(   R#  R3   R  (   R   R3   t   inclusivePopt   numPopst   mostRecentTagRU   (    (    s    /home/gs/python/BeautifulSoup.pyt	   _popToTag�  s    &c   	   	   C   s  |  j  j | � } | d k } |  j j | � } d } t } x� t t |  j � d d d � D]� } |  j | } | s� | j	 | k r� | r� | } Pn  | d k	 r� | j	 | k s� | d k r� | r� |  j j | j	 � r� | j	 } t
 } Pn  | j } q\ W| r|  j | | � n  d S(   s�  We need to pop up to the previous tag of this type, unless
        one of this tag's nesting reset triggers comes between this
        tag and the previous tag of this type, OR unless this tag is a
        generic nesting trigger and another generic nesting trigger
        comes between this tag and the previous tag of this type.

        Examples:
         <p>Foo<b>Bar *<p>* should pop to 'p', not 'b'.
         <p>Foo<table>Bar *<p>* should pop to 'table', not 'p'.
         <p>Foo<table><tr>Bar *<p>* should pop to 'tr', not 'p'.

         <li><ul><li> *<li>* should pop to 'ul', not the first 'li'.
         <tr><table><tr> *<tr>* should pop to 'table', not the first 'tr'
         <td><tr><td> *<td>* should pop to 'tr', not the first 'td'
        i   i    i����N(   t   NESTABLE_TAGSR�   R   t   RESET_NESTING_TAGSR�   RK   R�   R(   R#  R3   R�   R
   R1  (	   R   R3   t   nestingResetTriggerst
   isNestablet   isResetNestingt   popTot	   inclusiveRU   t   p(    (    s    /home/gs/python/BeautifulSoup.pyt	   _smartPop�  s(    &	i    c      
   C   sh  |  j  rV d j g  | D] \ } } d | | f ^ q � } |  j d | | f � d  S|  j �  |  j | � r� | r� |  j | � n  |  j r� t |  j � d k r� |  j j	 s� |  j j
 | | � r� d  St |  | | |  j |  j � } |  j r| |  j _ n  | |  _ |  j | � | s,|  j | � r9|  j �  n  | |  j k rd|  j  j | � d |  _ n  | S(   NR�   s    %s="%s"s   <%s%s>i   (   R$  R�   t   handle_dataR  R�   R:  R�   R(   R#  R5   R�   RL   R  R   R   R%  R  t
   QUOTE_TAGSR0   t   literal(   R   R3   R4   t   selfClosingR�   t   yR/   (    (    s    /home/gs/python/BeautifulSoup.pyt   unknown_starttag-  s*    	2
"		c         C   s�   |  j  r1 |  j  d | k r1 |  j d | � d  S|  j �  |  j | � |  j  r� |  j  d | k r� |  j  j �  t |  j  � d k |  _ n  d  S(   Ni����s   </%s>i    (   R$  R;  R  R1  R&  R(   R=  (   R   R3   (    (    s    /home/gs/python/BeautifulSoup.pyt   unknown_endtagK  s    
c         C   s   |  j  j | � d  S(   N(   R"  R0   (   R   t   data(    (    s    /home/gs/python/BeautifulSoup.pyR;  X  s    c         C   s(   |  j  �  |  j | � |  j  | � d S(   sO   Adds a certain piece of text to the tree as a NavigableString
        subclass.N(   R  R;  (   R   R5   t   subclass(    (    s    /home/gs/python/BeautifulSoup.pyt   _toStringSubclass[  s    
c         C   s-   | d  d k r d } n  |  j  | t � d S(   s�   Handle a processing instruction as a ProcessingInstruction
        object, possibly one with a %SOUP-ENCODING% slot into which an
        encoding will be plugged later.i   R�   u,   xml version='1.0' encoding='%SOUP-ENCODING%'N(   RD  Rs   (   R   R5   (    (    s    /home/gs/python/BeautifulSoup.pyt	   handle_pib  s    	c         C   s   |  j  | t � d S(   s#   Handle comments as Comment objects.N(   RD  Ru   (   R   R5   (    (    s    /home/gs/python/BeautifulSoup.pyt   handle_commentj  s    c         C   s9   |  j  r t t | � � } n
 d | } |  j | � d S(   s$   Handle character references as data.s   &#%s;N(   R  R�   R�   R;  (   R   t   refRB  (    (    s    /home/gs/python/BeautifulSoup.pyt   handle_charrefn  s    	
c         C   s�   d } |  j r: y t t | � } Wq: t k
 r6 q: Xn  | r_ |  j r_ |  j j | � } n  | r� |  j r� |  j j | � r� d | } n  | s� d | } n  |  j | � d S(   s�   Handle entity references as data, possibly converting known
        HTML and/or XML entity references to the corresponding Unicode
        characters.s   &amp;%ss   &%s;N(	   R   R�   R�   R   t   KeyErrorR�   R�   R�   R;  (   R   RG  RB  (    (    s    /home/gs/python/BeautifulSoup.pyt   handle_entityrefv  s    	c         C   s   |  j  | t � d S(   s4   Handle DOCTYPEs and the like as Declaration objects.N(   RD  Rv   (   R   RB  (    (    s    /home/gs/python/BeautifulSoup.pyt   handle_decl�  s    c         C   s�   d } |  j | | d !d k r� |  j j d | � } | d k rS t |  j � } n  |  j | d | !} | d } |  j | t � nT y t j |  | � } Wn; t k
 r� |  j | } |  j	 | � | t | � } n X| S(   s`   Treat a bogus SGML declaration as raw data. Treat a CDATA
        declaration as a CData object.i	   s	   <![CDATA[s   ]]>i����i   N(
   R   t   rawdataR�   R(   RD  Rr   R   t   parse_declarationR   R;  (   R   RU   t   jRy   RB  t   toHandle(    (    s    /home/gs/python/BeautifulSoup.pyRM  �  s    
N(*   R^   R_   R`   R!  R2  R3  R<  R+  R   R   R  R  R  R  R  t   ALL_ENTITIESR   R(  RK   R�   R�   R  R  Ro   R�   R  R  R%  R&   R  R1  R:  R@  RA  R;  RD  RE  RF  RH  RJ  RK  RM  (    (    (    s    /home/gs/python/BeautifulSoup.pyR�   
  sN   	)	C	
!			
			.							+	t   BeautifulSoupc           B   s=  e  Z d  Z d �  Z e d/ d0 � Z e d d g � Z i d/ d 6d/ d 6Z	 d1 Z
 d2 Z i g  d 6g  d 6d d g d 6g  d 6d g d  6d g d! 6Z i g  d" 6d" d# d$ d% g d& 6d& g d' 6d& g d( 6d" g d% 6d" g d# 6d" g d$ 6Z d3 Z e d/ e d, e e e � Z e g  e
 e e e � Z e j d- e j � Z d. �  Z RS(4   s  This parser knows the following facts about HTML:

    * Some tags have no closing tag and should be interpreted as being
      closed as soon as they are encountered.

    * The text inside some tags (ie. 'script') may contain tags which
      are not really part of the document and which should be parsed
      as text, not tags. If you want to parse the text as tags, you can
      always fetch it and parse it explicitly.

    * Tag nesting rules:

      Most tags can't be nested at all. For instance, the occurance of
      a <p> tag should implicitly close the previous <p> tag.

       <p>Para1<p>Para2
        should be transformed into:
       <p>Para1</p><p>Para2

      Some tags can be nested arbitrarily. For instance, the occurance
      of a <blockquote> tag should _not_ implicitly close the previous
      <blockquote> tag.

       Alice said: <blockquote>Bob said: <blockquote>Blah
        should NOT be transformed into:
       Alice said: <blockquote>Bob said: </blockquote><blockquote>Blah

      Some tags can be nested, but the nesting is reset by the
      interposition of other tags. For instance, a <tr> tag should
      implicitly close the previous <tr> tag within the same <table>,
      but not close a <tr> tag in another table.

       <table><tr>Blah<tr>Blah
        should be transformed into:
       <table><tr>Blah</tr><tr>Blah
        but,
       <tr>Blah<table><tr>Blah
        should NOT be transformed into
       <tr>Blah<table></tr><tr>Blah

    Differing assumptions about tag nesting rules are a major source
    of problems with the BeautifulSoup class. If BeautifulSoup is not
    treating as nestable a tag your page author treats as nestable,
    try ICantBelieveItsBeautifulSoup, MinimalSoup, or
    BeautifulStoneSoup before writing your own subclass.c         O   s@   | j  d � s |  j | d <n  t | d <t j |  | | � d  S(   NR  R�   (   R�   R  RK   R�   R�   (   R   R�   R6   (    (    s    /home/gs/python/BeautifulSoup.pyR�   �  s    
t   brt   hrt   inputt   imgt   metat   spacert   linkt   framet   baset   colt   pret   textareat   scriptt   spant   fontt   qt   objectt   bdoR�   t   supt   centert
   blockquotet   divt   fieldsett   inst   delt   olt   ult   lit   dlt   ddt   dtt   tablet   tbodyt   tfoott   theadt   trt   tdt   tht   addresst   formR9  t   noscripts   ((^|;)\s*charset=)([^;]*)c         C   s�  d } d } d } t } xi t d t | � � D]R } | | \ } } | j �  } | d k re | } q. | d k r. | } | } q. q. W| rT| rT|  j j | � }	 |	 rT|  j d k	 s� |  j |  j	 k rd �  }
 |  j j
 |
 | � } | | d | f | | <t } qQ|	 j d � } | rQ| |  j k rQ| |  _ |  j |  j � t � qQqTn  |  j d | � } | r~| r~t | _ n  d S(   s�   Beautiful Soup can detect a charset included in a META tag,
        try to convert the document to that charset, and re-parse the
        document from the beginning.i    s
   http-equivt   contentc         S   s   |  j  d � d S(   Ni   s   %SOUP-ENCODING%(   R�   (   R�   (    (    s    /home/gs/python/BeautifulSoup.pyt   rewrite?  s    i   RV  N(   R   R�   R�   R(   t   lowert
   CHARSET_RERO   R  R  R   R�   RK   R�   R  R	  R@  R�   (   R   R4   t	   httpEquivt   contentTypet   contentTypeIndext   tagNeedsEncodingSubstitutionRU   R�   Rh   R�   R|  t   newAttrt
   newCharsetR/   (    (    s    /home/gs/python/BeautifulSoup.pyt
   start_meta#  s>    					N(
   RR  RS  s   inputRU  s   metaRW  s   linkRY  s   baseR[  (   s   spanR`  Ra  s   objectRc  s   subRd  s   center(   Rf  s   divRh  Ri  s   del(   s   addressRy  R9  R\  (   R^   R_   R`   R�   R�   R   R!  R)  R+  R<  t   NESTABLE_INLINE_TAGSt   NESTABLE_BLOCK_TAGSt   NESTABLE_LIST_TAGSt   NESTABLE_TABLE_TAGSt   NON_NESTABLE_BLOCK_TAGSR3  R2  R   R   t   MR~  R�  (    (    (    s    /home/gs/python/BeautifulSoup.pyRQ  �  s@   .	 	 






	R	  c           B   s   e  Z RS(    (   R^   R_   (    (    (    s    /home/gs/python/BeautifulSoup.pyR	  R  s   t   ICantBelieveItsBeautifulSoupc           B   s2   e  Z d  Z d Z d Z e g  e j e e � Z RS(   sy  The BeautifulSoup class is oriented towards skipping over
    common HTML errors like unclosed tags. However, sometimes it makes
    errors of its own. For instance, consider this fragment:

     <b>Foo<b>Bar</b></b>

    This is perfectly valid (if bizarre) HTML. However, the
    BeautifulSoup class will implicitly close the first b tag when it
    encounters the second 'b'. It will think the author wrote
    "<b>Foo<b>Bar", and didn't close the first 'b' tag, because
    there's no real-world reason to bold something that's already
    bold. When it encounters '</b></b>' it will close two more 'b'
    tags, for a grand total of three tags closed instead of two. This
    can throw off the rest of your document structure. The same is
    true of a number of other tags, listed below.

    It's much more common for someone to forget to close a 'b' tag
    than to actually use nested 'b' tags, and the BeautifulSoup class
    handles the common case. This class handles the not-co-common
    case: where you can't believe someone wrote what they did, but
    it's valid HTML and BeautifulSoup screwed up by assuming it
    wouldn't be.t   emt   bigRU   t   smallt   ttt   abbrt   acronymt   strongt   citet   codet   dfnt   kbdt   sampt   vart   bRz  (   R�  R�  RU   R�  R�  R�  R�  R�  R�  s   codeR�  R�  R�  R�  s   varR�  R�  (   s   noscript(   R^   R_   R`   t*   I_CANT_BELIEVE_THEYRE_NESTABLE_INLINE_TAGSt)   I_CANT_BELIEVE_THEYRE_NESTABLE_BLOCK_TAGSR�   RQ  R2  (    (    (    s    /home/gs/python/BeautifulSoup.pyR�  U  s     t   MinimalSoupc           B   s    e  Z d  Z e d � Z i  Z RS(   s�  The MinimalSoup class is for parsing HTML that contains
    pathologically bad markup. It makes no assumptions about tag
    nesting, but it does know which tags are self-closing, that
    <script> tags contain Javascript and should not be parsed, that
    META tags may contain encoding information, and so on.

    This also makes it better for subclassing than BeautifulStoneSoup
    or BeautifulSoup.Rz  (   R^   R_   R`   R�   R3  R2  (    (    (    s    /home/gs/python/BeautifulSoup.pyR�  y  s   t   BeautifulSOAPc           B   s   e  Z d  Z d �  Z RS(   s�  This class will push a tag with only a single string child into
    the tag's parent as an attribute. The attribute's name is the tag
    name, and the value is the string child. An example should give
    the flavor of the change:

    <foo><bar>baz</bar></foo>
     =>
    <foo bar="baz"><bar>baz</bar></foo>

    You can then access fooTag['bar'] instead of fooTag.barTag.string.

    This is, of course, useful for scraping structures that tend to
    use subelements instead of attributes, such as SOAP messages. Note
    that it modifies its input, so don't print the modified version
    out.

    I'm not sure how many people really want to use this class; let me
    know if you do. Mainly I like the name.c         C   s�   t  |  j � d k r� |  j d } |  j d } | j �  t | t � r� t  | j � d k r� t | j d t � r� | j j | j	 � r� | j d | | j	 <q� n  t
 j |  � d  S(   Ni   i����i����i    (   R(   R#  R�   R$   RL   R   R&   R�   R�   R3   R�   R  (   R   R/   R
   (    (    s    /home/gs/python/BeautifulSoup.pyR  �  s    
$(   R^   R_   R`   R  (    (    (    s    /home/gs/python/BeautifulSoup.pyR�  �  s   t   RobustXMLParserc           B   s   e  Z RS(    (   R^   R_   (    (    (    s    /home/gs/python/BeautifulSoup.pyR�  �  s   t   RobustHTMLParserc           B   s   e  Z RS(    (   R^   R_   (    (    (    s    /home/gs/python/BeautifulSoup.pyR�  �  s   t   RobustWackAssHTMLParserc           B   s   e  Z RS(    (   R^   R_   (    (    (    s    /home/gs/python/BeautifulSoup.pyR�  �  s   t   RobustInsanelyWackAssHTMLParserc           B   s   e  Z RS(    (   R^   R_   (    (    (    s    /home/gs/python/BeautifulSoup.pyR�  �  s   t   SimplifyingSOAPParserc           B   s   e  Z RS(    (   R^   R_   (    (    (    s    /home/gs/python/BeautifulSoup.pyR�  �  s   R  c           B   sb  e  Z d  Z i d d 6d d 6Z g  d e d � Z d �  Z d �  Z d	 �  Z e d
 � Z	 d �  Z
 d �  Z df Z d �  Z i  dg d 6d d 6dh d 6di d 6dj d 6dk d 6dl d! 6dm d$ 6dn d' 6do d* 6dp d- 6dq d0 6dr d3 6d4 d5 6ds d8 6d4 d9 6d4 d: 6dt d= 6du d@ 6dv dC 6dw dF 6dx dI 6dy dL 6dz dO 6d{ dR 6d| dU 6d} dX 6d~ d[ 6d d^ 6d4 d_ 6d� db 6d� de 6Z RS(�   s�   A class for detecting the encoding of a *ML document and
    converting it to a Unicode string. If the source encoding is
    windows-1252, can replace MS smart quotes with their HTML or XML
    equivalents.s	   mac-romant	   macintoshs	   shift-jiss   x-sjisR�   c   
      C   sm  d  |  _ |  j | | � \ |  _ } } | |  _ g  |  _ | d k sT t | t � rp d  |  _ t | � |  _ d  Sd  } x' | D] } |  j	 | � } | r} Pq} q} W| s� x0 | | f D] } |  j	 | � } | r� Pq� q� Wn  | rt
 rt |  j t � r|  j	 t
 j |  j � d � } n  | sNx* d D] }	 |  j	 |	 � } | r(Pq(q(Wn  | |  _ | sid  |  _ n  d  S(   NR�   RX   s   utf-8s   windows-1252(   s   utf-8s   windows-1252(   R   R  t   _detectEncodingR�   R  t   triedEncodingsR$   RZ   R  t   _convertFromt   chardett   detect(
   R   R�   t   overrideEncodingsR  R�   t   documentEncodingt   sniffedEncodingt   ut   proposedEncodingt   proposed_encoding(    (    s    /home/gs/python/BeautifulSoup.pyR�   �  s8    				   " 	 c         C   sV   |  j  j | � } t | t � rR |  j d k rA d | d } qR d | d } n  | S(   sD   Changes a MS smart quote character to an XML or HTML
        entity.R�   s   &#x%s;i   s   &%s;i    (   t   MS_CHARSR�   R$   t   tupleR  (   R   t   origR�   (    (    s    /home/gs/python/BeautifulSoup.pyt
   _subMSChar  s    c            s�   �  j  | � } | s% | �  j k r) d  S�  j j | � �  j } �  j r� | j �  d k r� t j d � j	 �  f d �  | � } n  y( �  j
 | | � } | �  _ | �  _ Wn t k
 r� } d  SX�  j S(   Ns   windows-1252s
   iso-8859-1s
   iso-8859-2s   ([�-�])c            s   �  j  |  j d � � S(   Ni   (   R�  R�   (   R�   (   R   (    s    /home/gs/python/BeautifulSoup.pyR�     s    (   s   windows-1252s
   iso-8859-1s
   iso-8859-2(   t
   find_codecR�  R   R0   R�   R  R}  R   R   R�   t
   _toUnicodeR  R�   (   R   t   proposedR�   R�  t   e(    (   R   s    /home/gs/python/BeautifulSoup.pyR�    s$    	 		c         C   s  t  | � d k rH | d  d k rH | d d !d k rH d } | d } n� t  | � d k r� | d  d k r� | d d !d k r� d } | d } ni | d  d	 k r� d
 } | d } nF | d  d k r� d } | d } n# | d  d k r� d } | d } n  t | | � } | S(   s   Given a string and its encoding, decodes the string into Unicode.
        %encoding is a string recognized by encodings.aliasesi   i   s   ��t     s   utf-16bes   ��s   utf-16lei   s   ﻿s   utf-8t     ��s   utf-32bes   ��  s   utf-32le(   R(   RZ   (   R   RB  RX   t   newdata(    (    s    /home/gs/python/BeautifulSoup.pyR�  -  s&    ""c         C   s  d$ } } yC| d  d k r/ |  j | � } n| d  d k r` d } t | d � j d � } n�t | � d k r� | d  d k r� | d d !d k r� d } t | d d � j d � } n�| d  d	 k r� d
 } t | d
 � j d � } nat | � d k rE| d  d k rE| d d !d k rEd
 } t | d d
 � j d � } n| d  d k rvd } t | d � j d � } n� | d  d k r�d } t | d � j d � } n� | d  d k r�d } t | d d � j d � } np | d  d k rd } t | d d � j d � } n; | d  d k rFd } t | d d � j d � } n d } Wn d$ } n Xt j d � j | � } | r�| r�t j d t j � } | j	 | � } n  | d$ k	 r�| j
 �  d j �  } | r�| |  _ n  | r�| d% k r�| } q�n  | | | f S(&   s3   Given a document, tries to detect its XML encoding.i   s   Lo��t    < ?s   utf-16bes   utf-8i   s   ��R�  s   < ? s   utf-16les   ��t      <s   utf-32bes   <   s   utf-32leR�  s   ��  i   s   ﻿t   asciis!   ^<\?.*encoding=['"](.*?)['"].*\?>s#   <\s*meta[^>]+charset=([^>]*?)[;'">]i    s   iso-10646-ucs-2s   ucs-2t	   csunicodes   iso-10646-ucs-4s   ucs-4t   csucs4s   utf-16s   utf-32t   utf_16t   utf_32t   utf16t   u16N(   s   iso-10646-ucs-2s   ucs-2R�  s   iso-10646-ucs-4s   ucs-4R�  s   utf-16s   utf-32s   utf_16s   utf_32s   utf16s   u16(   R   t   _ebcdic_to_asciiRZ   R[   R(   R   R   R�   t   IRO   t   groupsR}  R  (   R   t   xml_dataR�   t   xml_encodingt   sniffed_xml_encodingt   xml_encoding_matcht   regexp(    (    s    /home/gs/python/BeautifulSoup.pyR�  F  sj    
""
  	c         C   sd   |  j  |  j j | | � � pc | r? |  j  | j d d � � pc | r` |  j  | j d d � � pc | S(   Nt   -R�   t   _(   t   _codect   CHARSET_ALIASESR�   RW   (   R   t   charset(    (    s    /home/gs/python/BeautifulSoup.pyR�  �  s    !!c         C   sE   | s
 | Sd  } y t j | � | } Wn t t f k
 r@ n X| S(   N(   R   t   codecst   lookupt   LookupErrorR    (   R   R�  t   codec(    (    s    /home/gs/python/BeautifulSoup.pyR�  �  s     
c         C   sv   |  j  } | j sf d} dd  l } | j dj t t t d� � � dj t t | � � � | _ n  | j | j � S(  Ni    i   i   i   i�   i	   i�   i   i�   i�   i�   i   i   i   i   i   i   i   i   i   i�   i�   i   i�   i   i   i�   i�   i   i   i   i   i�   i�   i�   i�   i�   i
   i   i   i�   i�   i�   i�   i�   i   i   i   i�   i�   i   i�   i�   i�   i�   i   i�   i�   i�   i�   i   i   i�   i   i    i�   i�   i�   i�   i�   i�   i�   i�   i�   i[   i.   i<   i(   i+   i!   i&   i�   i�   i�   i�   i�   i�   i�   i�   i�   i]   i$   i*   i)   i;   i^   i-   i/   i�   i�   i�   i�   i�   i�   i�   i�   i|   i,   i%   i_   i>   i?   i�   i�   i�   i�   i�   i�   i�   i�   i�   i`   i:   i#   i@   i'   i=   i"   i�   ia   ib   ic   id   ie   if   ig   ih   ii   i�   i�   i�   i�   i�   i�   i�   ij   ik   il   im   in   io   ip   iq   ir   i�   i�   i�   i�   i�   i�   i�   i~   is   it   iu   iv   iw   ix   iy   iz   i�   i�   i�   i�   i�   i�   i�   i�   i�   i�   i�   i�   i�   i�   i�   i�   i�   i�   i�   i�   i�   i�   i{   iA   iB   iC   iD   iE   iF   iG   iH   iI   i�   i�   i�   i�   i�   i�   i}   iJ   iK   iL   iM   iN   iO   iP   iQ   iR   i�   i�   i�   i�   i�   i�   i\   i�   iS   iT   iU   iV   iW   iX   iY   iZ   i�   i�   i�   i�   i�   i�   i0   i1   i2   i3   i4   i5   i6   i7   i8   i9   i�   i�   i�   i�   i�   i�   i����R�   i   (   i    i   i   i   i�   i	   i�   i   i�   i�   i�   i   i   i   i   i   i   i   i   i   i�   i�   i   i�   i   i   i�   i�   i   i   i   i   i�   i�   i�   i�   i�   i
   i   i   i�   i�   i�   i�   i�   i   i   i   i�   i�   i   i�   i�   i�   i�   i   i�   i�   i�   i�   i   i   i�   i   i    i�   i�   i�   i�   i�   i�   i�   i�   i�   i[   i.   i<   i(   i+   i!   i&   i�   i�   i�   i�   i�   i�   i�   i�   i�   i]   i$   i*   i)   i;   i^   i-   i/   i�   i�   i�   i�   i�   i�   i�   i�   i|   i,   i%   i_   i>   i?   i�   i�   i�   i�   i�   i�   i�   i�   i�   i`   i:   i#   i@   i'   i=   i"   i�   ia   ib   ic   id   ie   if   ig   ih   ii   i�   i�   i�   i�   i�   i�   i�   ij   ik   il   im   in   io   ip   iq   ir   i�   i�   i�   i�   i�   i�   i�   i~   is   it   iu   iv   iw   ix   iy   iz   i�   i�   i�   i�   i�   i�   i�   i�   i�   i�   i�   i�   i�   i�   i�   i�   i�   i�   i�   i�   i�   i�   i{   iA   iB   iC   iD   iE   iF   iG   iH   iI   i�   i�   i�   i�   i�   i�   i}   iJ   iK   iL   iM   iN   iO   iP   iQ   iR   i�   i�   i�   i�   i�   i�   i\   i�   iS   iT   iU   iV   iW   iX   iY   iZ   i�   i�   i�   i�   i�   i�   i0   i1   i2   i3   i4   i5   i6   i7   i8   i9   i�   i�   i�   i�   i�   i�   (	   Rm   t   EBCDIC_TO_ASCII_MAPRk   t	   maketransR�   R�   t   chrR�   R'  (   R   R]   R�   t   emapRk   (    (    s    /home/gs/python/BeautifulSoup.pyR�  �  s.    		                <t   eurot   20ACs   �R�   s   �t   sbquot   201As   �t   fnoft   192s   �t   bdquot   201Es   �t   hellipt   2026s   �t   daggert   2020s   �t   Daggert   2021s   �t   circt   2C6s   �t   permilt   2030s   �t   Scaront   160s   �t   lsaquot   2039s   �t   OEligt   152s   �t   ?s   �s   #x17Dt   17Ds   �s   �s   �t   lsquot   2018s   �t   rsquot   2019s   �t   ldquot   201Cs   �t   rdquot   201Ds   �t   bullt   2022s   �t   ndasht   2013s   �t   mdasht   2014s   �t   tildet   2DCs   �t   tradet   2122s   �t   scaront   161s   �t   rsaquot   203As   �t   oeligt   153s   �s   �s   #x17Et   17Es   �t   YumlR�   s   �N(   R�  R�  (   R�  R�  (   R�  R�  (   R�  R�  (   R�  R�  (   R�  R�  (   R�  R�  (   R�  R�  (   R�  R�  (   R�  R�  (   R�  R�  (   R�  R�  (   s   #x17DR�  (   R�  R�  (   R�  R�  (   R�  R�  (   R�  R�  (   R�  R�  (   R�  R�  (   R�  R   (   R  R  (   R  R  (   R  R  (   R  R  (   R	  R
  (   s   #x17ER  (   R  R�   (   R^   R_   R`   R�  R�   R�   R�  R�  R�  R�  R�  R�  R   R�  R�  R�  (    (    (    s    /home/gs/python/BeautifulSoup.pyR  �  sZ   

!			D		
	
t   __main__(?   R`   t
   __future__R    t
   __author__t   __version__t   __copyright__t   __license__t   sgmllibR   R   R�  t
   markupbaset   typesR   t   htmlentitydefsR   t   ImportErrorR)  t	   NameErrort   setsR   R   t   tagfindR�   t   _declname_matchRf   R   Rb  R	   RZ   R&   Rr   Rs   Ru   Rv   RL   RJ   R   RM   R�   R�   RQ  R�   R	  R�  R�  R�  R�  R�  R�  R�  R�  R�  R   t   cjkcodecs.aliasest	   cjkcodecst   iconv_codecR  R^   t   syst   stdint   soupR�   (    (    (    s    /home/gs/python/BeautifulSoup.pyt   <module>N   s�   
	� 8#� �x		� ��$'
� 