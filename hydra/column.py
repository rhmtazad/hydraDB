class Column:
    def __init__(self, connection):
        """
        Add, drop, modify, or retrieve a column.

        Note:
            Aggregate or use composition while using this
            class in another object. Also, make sure to
            pass the connection object as a parameter.

        Examples:
            >>> self.col = Column('pass the connection obj')

        Args:
            connection (:obj:`Connection`): Connect to the database.

        Attributes:
            self.__con (:obj:`Connection`): Use composition for connection.
        """

        self.__con = connection

    def __str__(self):
        """
        String representation of the Column class.

        Note:
            Use this in a print statement to print the
            documentation of the constructor.

        Returns:
            Returns the constructor documentation as string.
        """

        return self.__init__.__doc__

    def add(self, table, **columns):
        """
        Add a column in a table.

        Note:
            Pass the table name in the first parameter
            and pass the columns and data types in the
            second parameter. Also, pass as many columns
            as you want.

        Examples:
            >>> self.add('tbl', col1='text', col2='integer')

        Args:
            table (str): Add columns to this table.
            **columns (:obj:`kwargs`): Add columns with data types.

        Keyword Args:
            **columns (:obj:`kwargs`): Create the given columns.
                The first part in key='val' represents the column name
                and the next part represents the data type.

        Returns:
            Returns nothing.
        """

        # iterate through **columns and execute the query
        for column, data_type in columns.items():
            # query for adding column(s) in a table
            query = f'''
                ALTER TABLE {table}
                ADD COLUMN {column} {data_type}
            ;'''

            # execute the query
            self.__con.execute(query)

    def add_fk(self, table, column, reference_tbl, reference_col):
        """
        Add a column and set it as a foreign key.

        Note:
            This can only set a new column as a foreign key.
            To avoid problems, first, create other columns
            and then add a foreign key column using this function.

        Examples:
            >>> self.add_fk('tbl', 'fk_col', 'ref_tbl', 'ref_col')

        Args:
            table (str): Add a foreign key column to this table.
            column (str): Add this new column as a foreign key.
            reference_tbl (str): Refer the foreign key in this table.
            reference_col (str): Refer the foreign key in this column.

        Returns:
            Returns nothing.
        """

        # query for adding a foreign key column
        query = f'''
            ALTER TABLE {table}
            ADD COLUMN {column} INTEGER
            REFERENCES {reference_tbl}({reference_col})
        ;'''

        # execute the query
        self.__con.execute(query)

    def rename(self, table, current_name, new_name):
        """
        Rename a column in a table.

        Note:
            This function only works on non-primary-key
            columns because SQLite currently does not support
            renaming a primary key.

        Examples:
            >>> self.rename('tbl', 'col_name', 'new_col')

        Args:
            table (str): Rename a column from this table.
            current_name (str): Rename this column.
            new_name (str): New name for the column.

        Returns:
            Returns nothing.
        """

        # query for renaming a column
        query = f'''
            ALTER TABLE {table}
            RENAME COLUMN {current_name}
            TO {new_name}
        ;'''

        # execute the query
        self.__con.execute(query)
