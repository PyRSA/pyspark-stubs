#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.


from typing import overload
from typing import Any, Union

from pyspark.sql._typing import LiteralType, DecimalLiteral, DateTimeLiteral
from pyspark.sql.types import (  # noqa: F401
    DataType,
    StructField,
    StructType,
    IntegerType,
    StringType,
)
from pyspark.sql.window import WindowSpec

from py4j.java_gateway import JavaObject  # type: ignore[import]

class Column:
    def __init__(self, jc: JavaObject) -> None: ...
    def __neg__(self) -> Column: ...
    def __add__(self, other: Union[Column, LiteralType, DecimalLiteral]) -> Column: ...
    def __sub__(self, other: Union[Column, LiteralType, DecimalLiteral]) -> Column: ...
    def __mul__(self, other: Union[Column, LiteralType, DecimalLiteral]) -> Column: ...
    def __div__(self, other: Union[Column, LiteralType, DecimalLiteral]) -> Column: ...
    def __truediv__(
        self, other: Union[Column, LiteralType, DecimalLiteral]
    ) -> Column: ...
    def __mod__(self, other: Union[Column, LiteralType, DecimalLiteral]) -> Column: ...
    def __radd__(self, other: Union[LiteralType, DecimalLiteral]) -> Column: ...
    def __rsub__(self, other: Union[LiteralType, DecimalLiteral]) -> Column: ...
    def __rmul__(self, other: Union[LiteralType, DecimalLiteral]) -> Column: ...
    def __rdiv__(self, other: Union[LiteralType, DecimalLiteral]) -> Column: ...
    def __rtruediv__(self, other: Union[LiteralType, DecimalLiteral]) -> Column: ...
    def __rmod__(self, other: Union[bool, int, float, DecimalLiteral]) -> Column: ...
    def __pow__(self, other: Union[Column, LiteralType, DecimalLiteral]) -> Column: ...
    def __rpow__(self, other: Union[LiteralType, DecimalLiteral]) -> Column: ...
    def __eq__(self, other: Union[Column, LiteralType, DateTimeLiteral, DecimalLiteral]) -> Column: ...  # type: ignore[override]
    def __ne__(self, other: Any) -> Column: ...  # type: ignore[override]
    def __lt__(
        self, other: Union[Column, LiteralType, DateTimeLiteral, DecimalLiteral]
    ) -> Column: ...
    def __le__(
        self, other: Union[Column, LiteralType, DateTimeLiteral, DecimalLiteral]
    ) -> Column: ...
    def __ge__(
        self, other: Union[Column, LiteralType, DateTimeLiteral, DecimalLiteral]
    ) -> Column: ...
    def __gt__(
        self, other: Union[Column, LiteralType, DateTimeLiteral, DecimalLiteral]
    ) -> Column: ...
    def eqNullSafe(
        self, other: Union[Column, LiteralType, DecimalLiteral]
    ) -> Column: ...
    def __and__(self, other: Column) -> Column: ...
    def __or__(self, other: Column) -> Column: ...
    def __invert__(self) -> Column: ...
    def __rand__(self, other: Column) -> Column: ...
    def __ror__(self, other: Column) -> Column: ...
    def __contains__(self, other: Any) -> Column: ...
    def __getitem__(self, other: Any) -> Column: ...
    def bitwiseOR(self, other: Union[Column, int]) -> Column: ...
    def bitwiseAND(self, other: Union[Column, int]) -> Column: ...
    def bitwiseXOR(self, other: Union[Column, int]) -> Column: ...
    def getItem(self, key: Any) -> Column: ...
    def getField(self, name: Any) -> Column: ...
    def withField(self, fieldName: str, col: Column) -> Column: ...
    def dropFields(self, *fieldNames: str) -> Column: ...
    def __getattr__(self, item: Any) -> Column: ...
    def __iter__(self) -> None: ...
    def rlike(self, item: str) -> Column: ...
    def like(self, item: str) -> Column: ...
    def startswith(self, item: Union[str, Column]) -> Column: ...
    def endswith(self, item: Union[str, Column]) -> Column: ...
    @overload
    def substr(self, startPos: int, length: int) -> Column: ...
    @overload
    def substr(self, startPos: Column, length: Column) -> Column: ...
    def __getslice__(self, startPos: int, length: int) -> Column: ...
    def isin(self, *cols: Any) -> Column: ...
    def asc(self) -> Column: ...
    def asc_nulls_first(self) -> Column: ...
    def asc_nulls_last(self) -> Column: ...
    def desc(self) -> Column: ...
    def desc_nulls_first(self) -> Column: ...
    def desc_nulls_last(self) -> Column: ...
    def isNull(self) -> Column: ...
    def isNotNull(self) -> Column: ...
    def alias(self, *alias: str, **kwargs: Any) -> Column: ...
    def name(self, *alias: str) -> Column: ...
    def cast(self, dataType: Union[DataType, str]) -> Column: ...
    def astype(self, dataType: Union[DataType, str]) -> Column: ...
    def between(
        self,
        lowerBound: Union[Column, LiteralType, DateTimeLiteral, DecimalLiteral],
        upperBound: Union[Column, LiteralType, DateTimeLiteral, DecimalLiteral],
    ) -> Column: ...
    def when(self, condition: Column, value: Any) -> Column: ...
    def otherwise(self, value: Any) -> Column: ...
    def over(self, window: WindowSpec) -> Column: ...
    def __nonzero__(self) -> None: ...
    def __bool__(self) -> None: ...
    def contains(self, item: Any) -> Column: ...
