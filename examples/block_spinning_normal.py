# Generate greeting
from block_spinning import block_spinning

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


def BlockSpinningNormal():
    return block_spinning.spin(article)


# Only print password if it is run directly
if __name__ == "__main__":
    print(BlockSpinningNormal())
