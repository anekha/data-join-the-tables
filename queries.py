# pylint:disable=C0111,C0103

import sqlite3

conn = sqlite3.connect('data/ecommerce.sqlite')
db = conn.cursor()


def detailed_orders(db):
    '''return a list of all orders (order_id, customer.contact_name,
    employee.firstname) ordered by order_id'''
    query = """SELECT Orders.OrderID, Customers.ContactName, Employees.FirstName
            FROM Orders
            JOIN Customers ON  Customers.CustomerID = Orders.CustomerID
            JOIN Employees ON  Employees.EmployeeID = Orders.EmployeeID
            """
    results = db.execute(query)
    results = results.fetchall()
    return results

def spent_per_customer(db):
    '''return the total amount spent per customer ordered by ascending total
        amount (to 2 decimal places)
    Exemple :
        Jean   |   100
        Marc   |   110
        Simon  |   432
        ...
    '''
    query = """SELECT Customers.ContactName,
            SUM(OrderDetails.UnitPrice * OrderDetails.Quantity) AS OrderedAmount
            FROM Orders
            JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID
            JOIN Customers ON Customers.CustomerID = Orders.CustomerID
            GROUP BY Customers.ContactName
            ORDER BY OrderedAmount
            """
    results = db.execute(query)
    results = results.fetchall()
    return results

def best_employee(db):
    '''Implement the best_employee method to determine who’s the best employee! By “best employee”, we mean the one who sells the most.
    We expect the function to return a tuple like: ('FirstName', 'LastName', 6000 (the sum of all purchase)). The order of the information is irrelevant'''
    query = """SELECT Employees.FirstName,
            Employees.LastName,
            SUM(OrderDetails.UnitPrice * OrderDetails.Quantity) AS SalesTotal
            FROM Orders
            JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID
            JOIN Employees ON Employees.EmployeeID = Orders.EmployeeID
            GROUP BY Employees.FirstName
            ORDER BY SalesTotal DESC
            """
    results = db.execute(query)
    results = results.fetchone()
    return results


def orders_per_customer(db):
    '''Return a list of tuples where each tuple contains the contactName
    of the customer and the number of orders they made (contactName,
    number_of_orders). Order the list by ascending number of orders'''
    query = """SELECT Customers.ContactName,
            COUNT(Orders.CustomerID) AS number_of_orders
            FROM Customers
            LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID
            GROUP BY Orders.CustomerID
            ORDER BY number_of_orders
            """
    results = db.execute(query)
    results = results.fetchall()
    return results

#print(detailed_orders(db))
#print(spent_per_customer(db))
#print(best_employee(db))
print(orders_per_customer(db))
