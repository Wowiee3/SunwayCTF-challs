# pyLocker

| Key            | Value                                                                                                                                     |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| Challenge Name | pyLocker                                                                                                                                  |
| Author         | wolfishLamb                                                                                                                               |
| Category       | Misc                                                                                                                                      |
| Description    | At Sunway campus, locker rentals offer a secure place to store your belongings. But remember, your digital valuables need protection too! |
| Challenge Type | Dynamic Docker                                                                                                                            |
| Docker Image   | sunctf_misc_pylocker (port 1337)                                                                                                          |
| Flag           | sunctf{m4Rv3l0u5_pY7h0N_5Ki115}                                                                                                           |
| Score          | 300                                                                                                                                       |

*File(s) in `attachments/` are distributed to the participants.*

## Solution

<details>
<summary>Click to expand</summary>

The goal of this challenge is to call the method in `SunLocker` class by inputting Python code. However, the code will
be sanitised -- imports, calls and function/class declarations are **not allowed**.

Payload:
```
PublicLocker.__bases__ = (SunLocker, )
PublicLocker.__add__ = print
PublicLocker.__invert__ = locker._SunLocker__flag
locker + ~locker
end
```

1) Since we can't create any class instances, we can make use of the current one. Modify `__bases__` of `PublicLocker`
   to inherit methods from `SunLocker`.

   Alternatively, we can make `SunLocker` inherits from `Exception`. By doing so, we can `raise` it in `try` block and
   catch the instance in the `except` block.

   ```
   try:
      raise SunLocker
   except Exception as sunlocker_instance:
      ...
   ```
2) We can't call a function e.g. `print` as well. To bypass this, we set the `__add__` (or `__mul__` or any other binary
   operation methods) to `print`. This means that `locker + something` will be overloaded to
   `locker.__add__(something)`. By doing so, we have successfully called `print` without explicitly using `()`.

   Similarly, we set `__invert__` (or any other unary operation methods) to the `__flag` method of `SunLocker`. We use
   unary operation this time, since `__flag` method does not take in any arguments other than `self`.

   P.S.: There are only 4 unary operators: `~`, `+`, `-` and `not`, but you can't use `__not__` here. It only returns
   `True` or `False`.

3) A little thing to note with: method name that starts with `__` will undergo name mangling. In the `SunLocker` class,
   `__flag` method name is replaced with `_SunLocker__flag` in the `SunLocker` class.

</details>

Note: `docs/solve.py` can be used to check if the challenge is working as intended. It will solve the challenge and get
the flag.