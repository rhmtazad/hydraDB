from hydra.schema import Schema


if __name__ == '__main__':
    # create the schema
    db = Schema()

    # add a table with given columns
    db.form_table(
        table='student',
        name='text',
        age='integer'
    )

    # insert a row in a table
    db.insert_row(
        table='student',
        name='R',
        age=47
    )

    # update a row from a table
    db.update_row(
        table='student',
        row_id=2,
        name='A',
        age=25
    )

    # fetch a table from the database
    print(db.fetch_table(table='student'))

    # fetch a column from a table
    print(db.fetch_columns('student', 'name', 'age'))

    # fetch a row from a table
    print(db.fetch_row(table='student', row_id=1))

    # fetch the column names in a table
    print(db.fetch_column_names('student'))
