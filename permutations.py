#!/usr/bin/python
#encoding: utf8

from copy import deepcopy

def permutations(itemlist):
    """Takes in list of items and returns list of all permutations of that
    list. Items in the list can be of any type.

    for example:
        (1, 2, 3) => [[1, 2, 3], [1, 3, 2], 
                      [2, 1, 3], [2, 3, 1], 
                      [3, 1, 2], [3, 2, 1]]
    
    """
    tempitemlist = []
    permlist = []
    if len(itemlist) > 1:
        for i, item in enumerate(itemlist):
            templist = []
            tempitemlist = deepcopy(itemlist)
            del tempitemlist[i]
            templist.extend(permutations(tempitemlist))
            for perm in templist:
                perm.insert(0, item)
            permlist.extend(templist)
        return permlist
    else:
        return [[itemlist[0]]]

if __name__ == '__main__':
    permutations(list('laurionparas'))
