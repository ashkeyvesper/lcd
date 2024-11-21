#!/usr/bin/python3
import re


#tokens example: (1, +, 1)

def toNumber(token):
	try:
		out = float(token)
	except ValueError:
		return None
	return out


def getTokens(stri):
	return re.findall(r"(-?[0-9,]+\.?[0-9]*|[+\-/*\(\)]|[A-Za-z^0-9]+|[A-Za-z]+[0-9]+)",stri)

def parentheses(tokens):
	None
def exponent(tokens):
	None
def multiply(tokens):
	None
def add(tokens):
	None

example1 = "-1.0*-1.0"
print("example1: "+str(getTokens(example1)))

example2 = "SUM(A3)"
print("exmaple2: "+str(getTokens(example2)))
