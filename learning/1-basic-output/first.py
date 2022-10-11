"""
Quick test to see if I can print a string to the web page and manipulate
elements within the DOM.
"""
# example of importing JavaScript objects into python
# https://pyodide.org/en/stable/usage/type-conversions.html#importing-javascript-objects-into-python
from js import console

output_area = Element('output')
output_area_1 = Element('output-1')
output_area_2 = Element('output-2')

# this manipulates the innerHTML
output_area.write('Hello World')
# this appends a <div> and the content to the DOM
output_area_1.write('Hello World 1', append=True)
# appending a string to the existing text content by grabbing the text from
# the node and then writing text to the node. Notice that I'm using the Element.element
# property. This gives me a handle to the more fully featured pyodide interface.
output_area_2.write(f'{output_area_2.element.textContent} Hello World 2')
# very simple example of using the console. Might be useful for debugging.
console.warn(f"Ben's value is {output_area_2.element.textContent}")
