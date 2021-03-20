from hydra.schema import Schema


if __name__ == '__main__':
    # create the schema
    db = Schema()

    # add a table with given columns
    # db.form_table(
    #     'student',
    #     name='text',
    #     age='integer'
    # )

    # insert a row in a table
    db.insert_row(
        'student',
        name='R',
        age=47
    )

    # update a row from a table
    # db.update_row(
    #     'student', 2,
    #     name='A',
    #     age=25
    # )

    print(db.fetch("select * from student"))
