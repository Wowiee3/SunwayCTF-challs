title: pyLocker
category: misc
desc: At Sunway campus, locker rentals offer a secure place to store your belongings. But remember, your digital
valuables need protection too! pyLocker is known to be the world's safest service that keeps your data away from sneaky
hackers... right?
attachement: ref.py
author: wolfishLamb

payload:
PublicLocker.__bases__ = (SunLocker, )
PublicLocker.__add__ = print
PublicLocker.__invert__ = locker._SunLocker__flag
locker + ~locker

explanation:
The goal of this challenge is to call the method of `SunLocker` by inputing Python code. However, the code will be
sanitised -- imports, calls and function/class declarations are not allowed.

To solve this challenge, the player is expected to have a deep understanding of OOP and dunder methods.
1. Since we can't create any class instances, we can make use of the current one. Modify `__bases__` of `PublicLocker`
   to inherit methods from `SunLocker`.

   Alternatively, we can make `SunLocker` inherits from `Exception`. By doing so, we can `raise` it in `try` block and
   catch the instance in the `except` block.

   ```
   try:
      raise SunLocker
   except Exception as sunlocker_instance:
      ...
   ```
2. We can't call a function e.g. `print` as well. To bypass this, we set the `__add__` (or `__mul__` or any other binary
   operation methods) to `print`. This means that `locker + something` will be overloaded to
   `locker.__add__(something)`. We have successfully called `print` without explicitly using `()`.

   Similarly, we set `__invert__` (or any other unary operation methods) to the `__flag` method of `SunLocker`. We use
   unary operation this time, since `__flag` method does not take in any arguments other than `self`.

   P/S: There are only 4 unary operators: `~`, `+`, `-` and `not`, but you can't use `__not__` here. It only returns
   `True` or `False`.

3. A little thing to note with: method name that starts with `__` will undergo name mangling. In the `SunLocker` class,
   `__flag` method name is replaced with `_SunLocker__flag` in the `SunLocker` class.
