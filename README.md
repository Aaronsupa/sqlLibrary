# 📚 sqlLibrary
### 🌱 Project Description
This is my first project involving SQL. To begin, I make CSV files using Python and then import these files into JetBrains DataGrip.
Next, I performed a few queries to further explore the data that was generated.

### /config
```{r}
  Files: makeCSV.py -> This file takes the data.txt data and properly formats it and
                       stores the outputs into 2 seperate CSV files for the SQL tables
         data.txt -> File that is edited and used by makeCSV.py
         libData.csv -> Made from the madeCSV file for use in SQL tables
         authorNames.csv -> Made from the madeCSV file for use in SQL tables
```
### My Schema 
![Database Schema](https://github.com/Aaronsupa/sqlLibrary/assets/77075455/0fb047c1-f8b1-4d32-9847-0530d8a1b5dc)

### Exploring the Data
```{r}
select author_name, count(title) as "Books", sum(number_available) as "Total" from Books group by author_name order by Books desc limit 5;
```
#### Result 
| author_name          | Books | Total |
|-----------------|---------------|----------------|
| Ernest Hemingway| 3             | 7              |
| Stephen King    | 2             | 7              |
| Khaled Hosseini | 2             | 5              |
| John Steinbeck  | 2             | 7              |
| J.R.R. Tolkien  | 2             | 6              |

What if we want to sell the books in the library? We'll need a price column for this.
```{r}
alter table Books add Price integer default 5;

update Books set Price = 10 Where number_available == 1;
update Books set Price = 7 Where number_available == 2;
update Books set Price = 5 Where number_available == 3;
update Books set Price = 3 Where number_available == 4;

select * from Books order by Price desc limit 5;
```
#### Result 
| book_id | title                                 | author_name             | number_available | price |
|---------|---------------------------------------|-------------------------|------------------|-------|
| 3       | Ernest Hemingway                      | 3                       | 7                | 10    |
| 4       | The Great Gatsby                      | F. Scott Fitzgerald    | 1                | 10    |
| 13      | The Da Vinci Code                     | Dan Brown               | 1                | 10    |
| 16      | The Hitchhiker's Guide to the Galaxy | Douglas Adams           | 1                | 10    |
| 21      | The Alchemist                         | Paulo Coelho            | 1                | 10    |
| 38      | The Book Thief                        | Markus Zusak            | 1                | 10    |



### Technologies
- 🐍 Python
- 🗄️ SQL
- 💻 DataGrips
- 📁 CSV
