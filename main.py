import sqlite3
from Course import Course

if __name__ == '__main__':
    connection = sqlite3.connect('courses.db')
    statement = connection.cursor()

    algorithms = Course('https://vma.viko.lt/course/view.php?id=705','Žemiau pateiktas planas ir reikalavimai yra rekomendacinio pobūdžio. Jeigu žaidimas yra kito tipo galima surasti alternatyvias funkcijas','https://static.javatpoint.com/csharp/images/c-sharp.png')


    # CREATE TABLE
    # sql.execute("""CREATE TABLE courses (
    #     link text,
    #     description text,
    #     image text
    #     )""")

    # INSERT INTO DATABASE
    #  statement.execute("insert into courses values ('https://vma.viko.lt/course/view.php?id=707', 'Learn Fundamentals of Algorithms and Data Structures (Course language C++, you can choose any language you prefer).', 'https://uba.uva.nl/binaries/_ht_1664372656097/content/gallery/subsites/bibliotheek/workshops/python-symbol.png')")
    # INSERT INTO DATABASE USING CLASS OBJECT
    # statement.execute("insert into courses values (:link, :description, :image)", {'link': algorithms.link, 'description': algorithms.description, 'image': algorithms.image})
    # SELECT AND DISPLAY DATA
    # statement.execute("select * from courses where link='https://vma.viko.lt/course/view.php?id=707'")
    statement.execute("select * from courses")

    # Fetch one first match
    #print(statement.fetchone())
    # Fetchall all records with separator new line
    print(*statement.fetchall(), sep='\n')
    # fetch first 2 items
    #print(statement.fetchmany(2))
    connection.commit()
    connection.close()