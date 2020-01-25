from typing import cast

from .result import Result


res1 = Result.Ok('hello')  # type: Result[str, int]
if res1.is_ok():
    len(cast(str, res1.ok()))
else:
    cast(int, res1.err()) + 2
