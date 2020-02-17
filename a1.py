"""
Module for currency exchange

This module provides several string parsing functions to implement a 
simple currency exchange routine using an online currency service. 
The primary function in this module is exchange.

Author: YOUR NAME(S) AND NETID(S) HERE
Date:   THE DATE COMPLETED HERE
"""
import json as j #using json parser
import introcs as i 
def before_space(s):
    """
    Returns a copy of s up to, but not including, the first space

    Parameter s: the string to slice
    Precondition: s is a string with at least one space
    """
    return s.split()[0]


def after_space(s):
    """
    Returns a copy of s after the first space

    Parameter s: the string to slice
    Precondition: s is a string with at least one space
    """
    return s.split()[1]

def first_inside_quotes(s):
    """
    Returns the first substring of s between two (double) quotes

    A quote character is one that is inside a string, not one that 
    delimits it.  We typically use single quotes (') to delimit a 
    string if want to use a double quote character (") inside of it.

    Examples:
    first_inside_quotes('A "B C" D') returns 'B C'
    first_inside_quotes('A "B C" D "E F" G') returns 'B C', 
    because it only picks the first such substring

    Parameter s: a string to search
    Precondition: s is a string containing at least two double quotes
    """
    return s.split('"')[1]
def get_lhs(json):
    """
    Returns the lhs value in the response to a currency query

    Given a JSON response to a currency query, this returns the 
    string inside double quotes (") immediately following the keyword
    "lhs". For example, if the JSON is

    '{ "ok":true, "lhs":"1 Bitcoin", "rhs":"9916.0137 Euros", "err":"" }'

    then this function returns '1 Bitcoin' (not '"1 Bitcoin"').  

    This function returns the empty string if the JSON response
    contains an error message.

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query
    """
    lhs=j.loads(json)
    return lhs["lhs"]
def get_rhs(json):
    """
    Returns the rhs value in the response to a currency query

    Given a JSON response to a currency query, this returns the 
    string inside double quotes (") immediately following the keyword
    "rhs". For example, if the JSON is

    '{ "ok":true, "lhs":"1 Bitcoin", "rhs":"9916.0137 Euros", "err":"" }'

    then this function returns '9916.0137 Euros' (not 
    '"9916.0137 Euros"').  

    This function returns the empty string if the JSON response
    contains an error message.

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query
    """
    rhs=j.loads(json)
    return rhs["rhs"]
def has_error(json):
    """
    Returns True if the query has an error; False otherwise.

    Given a JSON response to a currency query, this returns the 
    opposite of the value following the keyword "ok". For example,
    if the JSON is 

    '{ "ok":false, "lhs":"", "rhs":"", "err":"Currency amount is invalid." }'

    then the query is not valid, so this function returns True (It 
    does NOT return the message 'Source currency code is invalid').

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query
    """
    err=j.loads(json)
    return err["err"]
def    currency_response(src, dst, amt):
    """
    Returns a JSON string that is a response to a currency query.

    A currency query converts amt money in currency src to the 
    currency dst. The response should be a string of the form    

    '{ "ok":true, "lhs":"<old-amt>", "rhs":"<new-amt>", "err":"" }'

    where the values old-amount and new-amount contain the value 
    and name for the original and new currencies. If the query is 
    invalid, both old-amount and new-amount will be empty, while 
    "ok" will be followed by the value false (and "err" will have 
    an error message).

    Parameter src: the currency on hand (the LHS)
    Precondition: src is a string with no spaces or non-letters

    Parameter dst: the currency to convert to (the RHS)
    Precondition: dst is a string with no spaces or non-letters

    Parameter amt: amount of currency to convert
    Precondition: amt is a float
    """
    return '{ "ok":"true", "lhs":'+src+', "rhs":"'+ dst+'", "err":""}'
