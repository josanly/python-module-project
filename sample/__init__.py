'''
.. module:: sample
   :synopsis: sample package
   :platform: Linux

.. moduleauthor:: Adrien Josso <josso.adrien@gmail.com>

'''

__version__='1.0'
__author__='Adrien Josso'

def small_function():
    '''
       Documentation

       :Example:

       >>> x = small_function()
       >>> print(x)
       0
    '''
    return 0

if __name__ == '__main__':
    print('Package Python sample')
    x = small_function()
    print(x)
