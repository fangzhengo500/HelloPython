from chapter_7_obj.chapter_7_2_class.chapter_7_2_6 import Filter
from chapter_7_obj.chapter_7_2_class.chapter_7_2_6 import SPANMFilter

print(issubclass(SPANMFilter, Filter))
print(issubclass(Filter, SPANMFilter))
print()

s = SPANMFilter()
print(isinstance(s, SPANMFilter))
print(isinstance(s, Filter))

print(isinstance(s, str))