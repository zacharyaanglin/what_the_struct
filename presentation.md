# [fit] What the struct?!

---

`> whoami`

---

![inline](headshot.jpg)

- Director, AI Engineering @ S&P Global
- Python fanatic
- New dad

---

![fit](malcolm.heic)

---

![fit](struct_wikipedia.png)

`struct`

---

`C`


- minimal programming language, came after `B`
- procedural, no objects!

---

![fit](no_struct.png)

---

![fit](no_struct_rect_diff.png)

---

![fit](basic_struct.png)

---

![fit](basic_struct_with_function.png)

---

![fit](struct_rect_diff.png)

---

![fit](compound_struct_rect_diff.png)

---

![fit](compound_struct_rect_diff.png)

# structure++
# readability ++
# reusability ++

---

# Aside: structs and memory

<br>

- C variables are stored in specific memory addresses
- Using a struct, you can ensure that addresses for the _elements_ in the struct are at contiguous locations in memory
- You can then read and write the struct in binary as a single unit

---

# [fit] Python: `struct`

---

`struct`

<br>

- Python module for unpacking and repacking structs stored as binary data
- Only useful for high-performance code and interoperating with C
- Requires declaring format types

---

![fit](python_struct_packing_1.png)

---

![fit](python_struct_packing_1_annotated.png)

---

![fit](format_characters.png)

---

![fit](format_characters_annotated.png)

---

![fit](python_struct_packing_1.png)

---

![fit](long_packed_struct_unlabeled.png)

---

![fit](long_packed_struct.png)

---

![fit](char_struct.png)

---

![fit](unpack_char_struct.png)

---

![fit](label_unpack_char_struct.png)

---

![fit](unpack_char_struct_tuple.png)

---

![fit](tuple_class_1.png)

---

![fit](tuple_class_2.png)

---

![fit](tuple_class_3.png)

---

![fit](tuple_class_4.png)

---

![fit](tuple_class_4.png)

# [fit] what the struct

---

![fit](basic_struct_labeled.png)

---

![fit](struct_index.png)

---

# [fit] namedtuple

---

`collections.namedtuple`

<br>

> It's a tuple, with names!

---

![fit](namedtuple_construction.png)

---

![fit](namedtuple_access.png)

---

`namedtuple(typename, field_names)`

<br>
<br>

- Creates a subtype of `tuple` named `typename`
- Inherits all tuple methods
- Gives named attribute access to fields in tuple

---

# Still a tuple

<br>

...still immutable
...same memory footprint (no `dict`)
...compares equally to `tuple`

---

![fit](namedtuple_Name.png)

---

![fit](namedtuple_Name_tuple.png)

---

![fit](namedtuple_Name_comparison.png)

---

![fit](namedtuple_Name_comparison_True.png)

---

# Default values

![fit](namedtuple_Name_default.png)

---

![fit](namedtuple_Name_default.png)

---

![fit](namedtuple_student_defaults.png)

---

![fit](fields_defaults_separate.png)

---

![fit](fields_defaults_combined.png)

---

![fit](namedtuple_student_tommy.png)

---

![fit](tommy_dict.png)

# [fit] dict conversion

---

![fit](tommy_dict.png)

---

# [fit] Immutability

![fit](try_to_set_age.png)

---

![fit](try_to_set_age.png)

---

`AttributeError`

![fit](try_to_set_age.png)

---

# [fit] tuples are immutable

---

`namedtuple._replace()`

![fit](tommy_plus_plus.png)

---

![fit](tommy_plus_plus.png)

---

# What about types?

---

`typing.NamedTuple`

---

`typing.NamedTuple`

<br>

- Introduced in Python 3.6
- Provides structural subclass of `tuple` with typed fields
- Introduces class-based declaration syntax

---

![fit](typing_namedtuple.png)

---

# Subclass syntax

![fit](typing_namedtuple_class.png)

---

![fit](typing_namedtuple_class.png)

---

![fit](typing_namedtuple_class_defaults.png)

---

![fit](typing_namedtuple_class_defaults.png)

# Sanity

---

# Comparison with tuple

![fit](typing_namedtuple_class_comparison.png)

---

![fit](typing_namedtuple_class_comparison.png)

---

![fit](namedtuple_mistaken_eq.png)

---

# Immutability

![fit](typing_namedtuple_class_error.png)

---

![fit](typing_namedtuple_class_error.png)

---

`AttributeError: can't set attribute`

![fit](typing_namedtuple_class_error.png)

---

# When to use named tuples?

<br>

- To add structure to processed immutable records
- To give descriptive names in compound data types
- To get rid of "magic numbers" (indices)

---

When to use `typing.NamedTuple` over `collections.namedtuple`?

<br>

<br>

- Basically all the time
- Or, at least when you're working in a typed codebase

---

When to use `typing.NamedTuple` over `collections.namedtuple`?

<br>

<br>

- Basically all the time
- Or, at least when you're working in a typed codebase
- (also please work in typed codebases)

---

Exiting tuple-land

---

`dataclasses`

---

`dataclasses`

<br>

- Introduced in Python 3.7
- Shorthand for creating lightweight classes
- Create independent types, no relation to tuples

---

![fit](dataclass.png)

---

![fit](dataclass_mutable.png)

---

![fit](dataclass_mutable.png)

No `AttributeError`!

---

![fit](dataclass_subscriptable_error.png)

---

![fit](dataclass_subscriptable_error.png)

`TypeError: 'Student' object is not subscriptable`

---

- Mutable by default
- Not subscriptable
- Just plain classes

---

![fit](dataclass_method.png)

---

# Comparison with tuple

![fit](dataclass_tuple_comparison.png)

---

![fit](dataclass_tuple_comparison.png)

---

![fit](dataclass_tuple_comparison_cast.png)

---

# [fit] Emulating immutability

![fit](dataclass_frozen.png)

---

![fit](dataclass_frozen.png)

---

`FrozenInstanceError: cannot assign to field 'x'`

![fit](dataclass_frozen.png)

---

_"Emulating"_

![fit](dataclass_frozen_workaround.png)

---

![fit](dataclass_frozen_workaround.png)

---

`dataclasses` `==` `python objects`

---

`dataclasses` `==` `python objects`

<br>

`tuples` `==` `C artifacts`

---

If you want a simple tuple, use typing.NamedTuple

<br>

If you want a Python object that can grow in complexity, use dataclasses

---

![fit](dataclass_pythag.png)

`__post_init__`

---

![fit](dataclass_pythag.png)

---

![fit](hettinger.png)

---

# TypedDict

---

`typing.TypedDict`

<br>

- New in Python 3.8
- Add type hints to dictionary
- Doesn't define new runtime class
- Useful for typecheckers like `mypy`

---

![fit](typeddict.png)

---

When to use `TypedDict`?

<br>

- When you are processing dictionaries (e.g., JSON)
- When you want to add structure to `Dict` type annotations

---

Exiting the standard library

---

`attrs`

---

`attrs`: `Classes Without Boilerplate`

<br>

<br>

- Lightweight syntax for declaring custom types
- Been around since Python 2
- Inspired and consulted on `dataclasses`

---

![fit](attrs.png)

---

# Validators

![fit](attrs_validated.png)

---

![fit](attrs_validated.png)

---

`ValueError: Coordinates must be positive.`

![fit](attrs_validated.png)

---

Features over `dataclasses`:

<br>

- Python 2/PyPy support
- Validators
- Converters
- `__slots__`
- and more

---

When to use `attrs`:

<br>

- You need to support Python 2 (:/)
- You need more advanced features than `dataclasses` can provide
- You want to be on the bleeding edge

---

`pydantic`

![fit](pydantic.png)

---

![fit](pydantic.png)

---

# Validators

![fit](pydantic_validator.png)

---

![fit](pydantic_validator.png)

---

![fit](pydantic_validator.png)

`Must be positive (type=value_error)`

---

`pydantic`

<br>

- Recent project taking advantage of type annotations
- Strong support for data validation
- Full `dataclasses` api and standard library interoperability

---

![fit](pydantic_dataclass.png)

`dataclasses` `API`

---

![fit](pydantic_dataclass.png)

---

`Complex serializations`

![fit](pydantic_nested_dataclass.png)

---

![fit](pydantic_nested_dataclass.png)

---

When to use `pydantic`:

<br>

- When you need powerful data validation
- When you're validating external data through an API
- When you need to deserialize a compound structure
- If you're in a typed codebase :)

---

# [fit] Recap

---

- `C structs`
- `Python structs`
- `collection.namedtuple`
- `typing.NamedTuple`
- `dataclasses`
- `typing.TypedDict`
- `attrs`
- `pydantic`

---

> There should be one-- and preferably only one --obvious way to do it.
-- The Zen of Python

--- 

# [fit] fin
