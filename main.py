from hydra.schema import Schema


if __name__ == '__main__':
    # create the schema
    db = Schema()

    # add a table with given columns
    db.form_table(
        'student',
        name='text',
        age='integer'
    )
