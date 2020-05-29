# Block Spinning
A Python module for block spinning text, more info about this subject you can find here:
- [Block spinning step by step](http://autofillmagic.com/tutorials/block-spinning-step-by-step/)

# How to Install

To install using pip run:
```
$ pip install block_spinning
```

Alternatively this module can be installed by downloading the [zipped folder](/../../archive/master.zip) or cloning the repository and running:
```
$ python setup.py install
```
# How to use it
This module can do block spinning for you like this.

``` Python
import block_spinning

article = r"""
#block#
#p#
This is the intro of my article.
#s#
This article is about..
#s#
#/p#
#/block#

#block#
#p#
This part can be mixed 
#s#
This is one of the parts of the article 
#s#
#/p#
#/block#
"""
print(block_spinning.spin(article))
```

### The Spin Function:
##### Inputs:
* string: The article string in the format like it shows in the example.
* lock_first: (Optional) if you want the first block to be in the same place and not have a randomized order (Default False).
* limit_of_blocks: (Optional) limits the amount of blocks to make an article off. It will still shuffle all the blocks of course (Default None).

# How can this be useful
Ever wanted to write a lot of articles by just writing one? With block spinning you can generate multiple unique articles while you only have to write it once! As it just generates text you can add customize it the way you want (e.g. using variables inside the text) 

# Examples
I only implemented the [format](http://autofillmagic.com/fileadmin/files/samples/block-spinning-sample.txt) that is used on [this](http://autofillmagic.com/tutorials/block-spinning-step-by-step/) site.
##### Example:
```
#block#
#p#
This is the intro of my article.
#s#
In this article I'm going to talk about...
#s#
This article is about..
#s#
#/p#
#/block#

#block#
#p#
This is a completely separate part of the article and can be at any position 
#s#
This part can be mixed 
#s#
This is one of the parts of the article 
#s#
#/p#
#/block#
```
##### Can produce:
By setting `lock_first=True` it will keep the first block above the others and shuffle the remaining blocks.
```
This is the intro of my article.

This part can be mixed
```

```
In this article I'm going to talk about...

This is one of the parts of the article
```
---
While this is not that special at all and seems simple you can write quite advance things with it while keeping the readability. Take a look at this other example which you can generate with the help of [spintax](https://github.com/AceLewis/spintax).
##### Example with spintax:
```
#block#
#p#
Block {spinning|re writing|rewriting|re-writing} is a {new|brand-new|completely new} {way of|approach to|method of|method for} {spinning|re writing|rewriting|re-writing} {that|which} takes the pain {out of|out-of} the {old|outdated|traditional} {and|and also|and very} {tedious|boring|dull|monotonous|exhausting} {way of|approach to|method of|method for} {spinning|re writing|rewriting|re-writing} {text|articles}.
The block {spinning|re writing|rewriting|re-writing} {format|syntax} {introduced|released|launched|created} by Autofill Magic makes {writing|creating|producing} {complex|complicated|advanced|puzzling} spun {text|articles} {a lot|much|a great deal|a whole lot|a-lot} {easier|smoother|less complicated|less difficult}.
{If you want|If you'd like|If you would like} to {save|truly save|save your self|save lots of|save yourself} time {and|and also} {be more|be much more|become more|be} {effective|productive} {when you|whenever you} {spin|rewrite|re-write} {articles|content|text} then {read on|continue reading|keep reading} - {there is a|there's a|there exists a|there is now a} {new|brand-new|completely new} {and|and also} {better|superior} {way of|approach to|method of|method for} {during|dealing with} {it|this}.
#s#
{Block spinning|The block spining format} have {many|several|numerous|a lot of} {qualities|advantages} over the {old|traditional} and outdated {spintax|spinning syntax|bracket spintax}.
{Compared to|In comparison to|When compared with|In comparison with} the {old|traditional} {spintax|spinning syntax|bracket spintax}, {block spinning|the block spinning format} is {better|superior} in {so many|numerous|a lot of|any number of} {ways|aspects}.
{Traditional|Conventional|Standard} {spintax|spinning syntax|bracket spintax} can {create|produce|generate} {great results|good results} {but|however|nonetheless|nevertheless} {block spinning|the block spinning format} are taking {spinning|rewriting|re-writing|randomization} to a hole {new|brand-new} {level|stage}.
#s#
{The first|The very first|The initial} thing {you will|you'll|you are going to|you may} {notice|discover|see|find|learn} {is that|is the fact that} {the block spinning format|block spinning} is {much easier|easier|much simpler|simpler} to read and {edit|modify|revise}.
{Unlike|In contrast to|As opposed to} {normal|regular|standard|traditional} {spintax|spinning syntax|bracket spintax}, the block {spinning|re-writing|rewriting} {format|design|syntax} {is very|is extremely|is quite} {easy to|simple to|easy-to} {edit|modify|revise} and {maintain|update}.
{It is|It's} {well know|well-know} that {traditional|conventional|classic|standard} {spintax|spinning syntax|bracket spintax} is {hard to|difficult to|tough to} read. Block {spinning|rewriting} is {nothing like|not like} that and {are very|are extremely} {easy to|simple to|easy-to} read and {write|produce|generate|compose}.
#s#
The {level of|degree of} {uniqueness|originality} is also {much higher|greater|higher|better} than the one {achieved|accomplished|attained|reached} {with|using} {traditional|conventional|classic|standard} {spintax|spinning syntax|bracket spintax}.
{On top of that|Better yet|Better still} {you can get|you will get} a {better|greater|higher} {level of|degree of} {uniqueness|originality} {when you|If you} {use|utilize} block {spinning|rewriting}.
The {new|brand-new} {features of|options that come with} block {spinning|rewriting} will {insure|ensure} {that your|that the|your} {article|text} {will be|is} both uniques and {readable|understandable|viewable|watchable}.
#s#
#/p#
#/block#

#block#
#p#
{One of|Among} the most {frustrating|irritating} and annoying things about {multi-level|multi level|multilevel} {spintax|spinning syntax|bracket spintax} {is that|is the fact that} {is very|is extremely|is quite} {hard to|difficult to|tough to} read.
{It is|It's} a {well known|well-known} {fact|truth|reality} by {article writers|writers|authors|editors} that the {old|traditional} {spintax|spinning syntax|bracket spintax} with {several|many|numerous} levels are {near|close to|close} {impossible|hopeless|unbearable} to read.
The {old|traditional} {way of|approach to|way for|method of} {writing|creating|composing} {spintax|spinning syntax|bracket spintax} on both paragraph, sentence and {word|phrase} level is a real {mess|chaos} {to look at|to gaze at} and {edit|modify|revise}.
#s#
{Errors|Mistakes|Faults} {will often|usually} {occur|take place|arise} and {break|crack} the {output|result}.
{It is|It's} {almost|nearly|practically|virtually} impossible {to avoid|to prevent} {errors|mistakes|faults} {since|because|given that} the {spintax|spinning syntax|bracket spintax} {can|can often} {reach|go to} an {overwhelming|frustrating|daunting} {complexity|sophistication|clutter}.
{It is|It's} more a rule than an exception that {typos|keyboard typos} and {errors|mistakes|faults} {sneak|creep} in when you {build up|develop|produce|build-up} {spintax|spinning syntax|bracket spintax}.
#s#
{On top of that|More over|Furthermore} {it is|It's} {very hard|very difficult|quite difficult|really difficult} {to find|to locate|to discover} the {errors|mistakes|faults} and correct them {when you|When you|Once you|If you|Whenever you} {realize that|understand that} {they are|they're|they may be} there.
{Correcting|Fixing|Repairing} the {errors|mistakes|faults} {can be|is} a real {pain|nightmare} {since it|because it|as it} {is not|isn't|just isn't|is just not} {easy to|simple to|easy-to} {find|navigate} your way {around|about} a {heavy|large|complex} spun {text|article}.
{It is|It's} {often|usually|typically} {hard to|difficult to|tough to} {find|discover|locate|uncover} and correct the {errors|mistakes|faults} in the {sometimes|often} {gigantic|huge|massive|big} and {complex|complicated|puzzling} {spintax|spinning syntax|bracket spintax} {texts|scripts|programs|texting}.
#s#
{Block spinning|The block spinning format} makes this a {lot|ton} {easier|simpler|smoother} by {keeping|presenting} everything {much more|a lot more|far more|more} {organized|structured|arranged} and {readable|understandable}.
{With|Using} {block spinning|the block spinning format} {you have|you've|you've got} {every|each|each and every|every single} paragraph in a {well|properly|nicely} {structured|organized|arranged} order and {every|each|each and every|every single} sentence on {its own|an unique|its very own} line - {much easier|much simpler} to read {!|.}
The {much better|better|far better} readability and {structure|format|arrangement} of {block spinning|the block spinning format} {give you|provide you with|offer you|provide} a {great|excellent|good|wonderful} overview {of your|of one's|of the} {text|article} and {decrease|reduce|lower} {errors|mistakes|faults}.
#s#
#/p#
#/block#
```

##### Can produce:
```
Block spinning have numerous advantages over the traditional and outdated spinning syntax.
In comparison with the old spinning syntax, block spinning is better in so many ways.
Conventional spintax can produce good results nevertheless the block spinning format are taking rewriting to a hole brand-new level.

One of the most frustrating and annoying things about multi level spintax is that is very difficult to read.
It's a well known fact by writers that the old spintax with several levels are near impossible to read.
The traditional approach to creating spintax on both paragraph, sentence and word level is a real chaos to gaze at and modify.
```
```
The block spinning format makes this a ton easier by presenting everything far more organized and understandable.
With the block spinning format you've got each paragraph in a properly organized order and each sentence on its own line - much easier to read !
The much better readability and structure of block spinning provide a great overview of your article and decrease errors.

Block re writing is a brand-new way of rewriting that takes the pain out-of the old and dull method for re writing text.
The block rewriting format released by Autofill Magic makes producing advanced spun text much easier.
If you'd like to save your self time and be much more effective whenever you rewrite text then read on - there is a new and also better method of dealing with this.
```

# Licence

This software is licensed under the GNU General Public License (version 3) as published by the Free Software Foundation this licence http://www.gnu.org/licenses/.