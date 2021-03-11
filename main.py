from hydra.database import Database


"""
.....................................
.....................................
    Connection Class
        - create file          [done]
        - connect to file      [done]
        - efficient connection [done]
        - encapsulate data     [done]
        - documentation        [done]
.....................................
.....................................
    Database Class
        - execute query        [done]
        - fetch a query        [done]
        - drop column(s)       [done]
        - encapsulate data     [done]
        - documentation        [done]
.....................................
.....................................
    Table Class
        - create table(s)      [done]
        - form a table         [done]
        - drop table(s)        [done]
        - rename a table       [done]
        - copy data to another [done]
        - get table data       [////]
        - validate table       [++++]
        - encapsulate data     [done]
        - documentation        [done]
.....................................
.....................................
    Column Class
        - add column(s)        [done]
        - set foreign key      [done]
        - rename column        [done]
        - get column data      [////]
        - validate column      [++++]
        - encapsulate data     [done]
        - documentation        [done]
.....................................
.....................................
    Row Class
        - add data             [done]
        - edit data            [done]
        - delete data          [done]
        - get cell data        [////]
        - get row data         [////]
        - validate row_id      [++++]
        - encapsulate data     [done]
        - documentation        [done]
.....................................
.....................................
    More Operations
        - count of data        [....]
        - sum of data          [....]
        - average of data      [....]
        - min of a group       [....]
        - max of a group       [....]
.....................................
.....................................
"""


if __name__ == '__main__':
    db = Database()

    db.tbl.form(
        'student',
        name='text',
        age='integer'
    )

    db.tbl.row.insert(
        'student',
        name='R',
        age='25'
    )

    db.tbl.row.update(
        'student', 1,
        name='RRR',
        age=47
    )

    print(db.fetch('select * from student where student_id=1'))
