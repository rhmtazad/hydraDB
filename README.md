## HydraDB v2.4.1
#### An API for Faster and Easier SQLite/Python Operations


[![rhmtazad - hydradb](https://img.shields.io/static/v1?label=rhmtazad&message=hydradb&color=beige&logo=github)](https://github.com/rhmtazad/hydradb)
[![language - python](https://img.shields.io/badge/language-python-81c253?color=mediumseagreen&logo=python&logoColor=white)](https://www.python.org/)
[![installation - pip install hydradb](https://img.shields.io/badge/installation-pip_install_hydradb-tomato?logo=python&logoColor=white)](https://pypi.org/project/hydradb/)
[![GitHub version](https://badge.fury.io/py/hydradb.svg)](https://pypi.org/project/hydradb/)
[![license - MIT](https://img.shields.io/badge/license-MIT-beige)](https://opensource.org/licenses/MIT)

----------------------------------------------------------------------------------------------

An API for Python and SQLite to manage databases faster and easier.
You can now add,modify, or fetch tables, columns, and rows in no time.
Also, you can execute/fetch custom queries using built-in functions.
This API applies some design patterns of object-oriented programming to make it reusable.

----------------------------------------------------------------------------------------------

## Requirements

**To make hydraDB work properly you must have installed:**
- [Python 3.9] - Latest version of Python
- [SQLite3] - Latest version of SQLite3

----------------------------------------------------------------------------------------------

## Installation

**You can install through pip or by copying inside your project folder**

```console
pip install hydradb
```

----------------------------------------------------------------------------------------------

## How to Import and Use the API

**To import the package inside your project:**

```python
from hydra import Schema
```

**To have access to the operations:**
>*If the name or location is not passed  as parameters, it will set them to default.*
>*The default for the name is 'main' and the default for the directory is the project directory.*
>*The database file will be saved with '.db' extension.*

```python
name = 'myDB'
location = 'C:\Projects\Python\'

db = Schema(name, location) # or use Schema() without passing parameter values
```

----------------------------------------------------------------------------------------------

## General Operations

**Execute a query from the database:**

```python
execute(query) # execute('select * from tbl')
```

**Fetch a query from the database:**

```python
fetch(query) # fetch('select * from tbl')
```

----------------------------------------------------------------------------------------------

## Table Operations

**Add one or more tables in database:**

```python
add_table(*tables) # add_table('tbl1', 'tbl2', tbl3')
```

**Drop one or multiple tables from a database:**

```python
drop_table(*tables) # drop_table('tbl1', 'tbl2', 'tbl3')
```

**Rename a table from the database:**

```python
rename_table(old_name, new_name) # rename_table('old', 'new')
```

**Create a table with the given columns:**

```python
form_table(table, **columns) # form_table(table='tbl', name='text', age='integer')
```

**Copy a table's data to a new one:**

```python
copy_table(origin_tbl, new_tbl, **columns) # copy_table('origin', 'new', col1='text')
```

**Fetch a table's data from a database:**

```python
fetch_table(table) # fetch_table('student')
```

----------------------------------------------------------------------------------------------

## Column Operations

**Add one or more columns to a table:**

```python
add_column(table, **columns) # add_column('tbl', name='text', age='integer')
```

**Drop one or more columns from a table:**

```python
drop_column(table, **columns) # drop_column('tbl', name='text', age='integer')
```

**Add a column to a table and set it as a foreign key:**

```python
add_fk(table, column, reference_tbl, reference_col)
```

**Rename a column from a table:**

```python
rename_column(tbl, current_name, new_name)
```

**Fetch one or more columns from a table:**

```python
fetch_columns(table, *columns) # fetch_columns('tbl', 'name', 'age')
```

**Fetch column names from a table:**

```python
fetch_column_names(table)
```

**Filter based on one or more column's values:**

```python
filter_column(table, **col_val) # filter_column('tbl', name='R', age=25)
```

----------------------------------------------------------------------------------------------

## Row Operations

**Insert a row in a table:**

```python
insert_row(table, **data) # insert_row('tbl', name='R', age='25')
```

**Delete a row from a table:**

```python
delete_row(table, row_id) # delete_row(table='student', row_id=1)
```

**Update a row in a table:**

```python
update_row(table, row_id, **data) # update_row(table='student', row_id=1, name='R')
```

**Fetch one or more cells within a row:**

```python
fetch_row(table, row_id, *columns)
```

**Count number of rows based on columns and their values:**

```python
count_rows(table, **col_val) # count_rows(table='tbl', name='R', age=25)
```

----------------------------------------------------------------------------------------------

## License

##### MIT License

###### Copyright 2021 Rahmat Azad

Permission is hereby granted, free of charge,
to any person obtaining a copy of this software
and associated documentation files (the "Software"),
to deal in the Software without restriction,
including without limitation the rights to use, copy,
modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit
persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this
permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT
WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR
IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.