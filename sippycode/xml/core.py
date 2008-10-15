#    Copyright 2008 Jeffrey William Scudder
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.


try:
  from xml.etree import cElementTree as ElementTree
except ImportError:
  try:
    import cElementTree as ElementTree
  except ImportError:
    try:
      from xml.etree import ElementTree
    except ImportError:
      from elementtree import ElementTree


class XmlElement(object):
  _tag = None
  _namespace = None
  _expected_elements = None
  _expected_attributes = None

  _other_elements = None
  _other_attributes = None
  
  def element(cls, name, member_class, repeating=False):
    pass
  element = classmethod(member)
  
  def attribute(cls, name, tag, namespace):
    pass
  attribute = classmethod(attribute)

  
  

# Example:
#
# class Test(XmlElement):
#   _tag = 'test'
#   _namespace = 'http://example.com/xml'
# Test.element('foo', Foo)

# class Test(XmlElement):
#   _tag = 'test'
#   _namespace = 'http://example.com/xml'
#   elements = (('foo', Foo), ('repeated', Repeats, True), ())
#   attributes = ((''))

# class Test(XmlElement):
#   _tag = 'test'
#   _namespace = 'http://example.com/xml'
#   members(elements=(('foo', Foo), ('repeated', Repeats, True), ()),
#           attributes=(('')))


