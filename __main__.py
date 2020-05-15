from __init__ import *


print('Locals:\n - ' + '\n - '.join(n for n in locals().keys()
                                    if not n.startswith('_')))
