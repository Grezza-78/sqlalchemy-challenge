# sqlalchemy-challenge

The purpose of this challenge was to undertake a research project about people who joined a non-specific company during the 1980s and 1990s. 

**The challenge was divided into three sections:**
  * **1 Data Modelling**
       This section required the review six CSV files containing various data points including:
         a) Departments - Department Number and Department Name
         b) Department Employee - Department Number and Employee Number (all employees)
         c) Department Manager - Department Number and Employee Number (specific to managers)
         d) Employees - Employee Number, Employee Title, Birth Date, First Name, Last Name, Sex and Hire Date
         e) Salaries - Employee Number, and Salary
         f) Titles - Title Id and Title
       Part of the modelling includes the design of an entity relationship diagram (ERD)
        
  * **2 Data Engineering**
       This section required the design of schema tables in PostgreSQL using pgAdmin4 to hold imported data from six CSV files including the specifying the data types,          primary keys and foreign keys, Once the tables were designed the CSV data files were imported according to their designed schema.
       
  * **3 Data Analysis** 
      The analysis required the review of eight questions specific about the employees including the listing of:
         1)  The employee number, last name, first name, sex, and salary of each employee
         2)  The first name, last name, and hire date for the employees who were hired in 1986
         3)  The manager of each department along with their department number, department name, employee number, last name, and first name
         4)  The department number for each employee along with that employee’s employee number, last name, first name, and department name
         5)  The first name, last name, and sex of each employee whose first name is Hercules and whose last name begins with the letter B
         6)  Each employee in the Sales department, including their employee number, last name, and first name
         7)  Each employee in the Sales and Development departments, including their employee number, last name, first name, and department name
         8)  The frequency counts, in descending order, of all the employee last names (that is, how many employees share each last name)

