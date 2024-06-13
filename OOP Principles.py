# Q 1
#Task 1

class BudgetCategory:
  """
  This class represents a Budget Category for personal finance management.
  """

  def __init__(self, category_name, allocated_budget):
    """
    Initializes a BudgetCategory object with a name and allocated budget.

    Args:
      category_name (str): The name of the budget category.
      allocated_budget (float): The total budget allocated to this category.
    """
    # Define category name and allocated budget as private attributes
    self.__category_name = category_name
    self.__allocated_budget = allocated_budget

  # Getters and setters will be defined in future tasks

#Task 2

class BudgetCategory:
  """
  This class represents a Budget Category for personal finance management.
  """

  def __init__(self, category_name, allocated_budget):
    """
    Initializes a BudgetCategory object with a name and allocated budget.

    Args:
      category_name (str): The name of the budget category.
      allocated_budget (float): The total budget allocated to this category.
    """
    # Define category name and allocated budget as private attributes
    self.__category_name = category_name
    self.__allocated_budget = allocated_budget

  def get_category_name(self):
    """
    Returns the category name.
    """
    return self.__category_name

  def set_category_name(self, new_category_name):
    """
    Sets the category name, ensuring it's not empty.

    Args:
      new_category_name (str): The new name for the budget category.
    """
    if not new_category_name:
      raise ValueError("Category name cannot be empty.")
    self.__category_name = new_category_name

  def get_allocated_budget(self):
    """
    Returns the allocated budget.
    """
    return self.__allocated_budget

  def set_allocated_budget(self, new_budget):
    """
    Sets the allocated budget, ensuring it's a positive number.

    Args:
      new_budget (float): The new allocated budget for the category.
    """
    if new_budget <= 0:
      raise ValueError("Allocated budget must be a positive number.")
    self.__allocated_budget = new_budget

#Task 3

class BudgetCategory:
  """
  This class represents a Budget Category for personal finance management.
  """

  def __init__(self, category_name, allocated_budget):
    """
    Initializes a BudgetCategory object with a name and allocated budget.

    Args:
      category_name (str): The name of the budget category.
      allocated_budget (float): The total budget allocated to this category.
    """
    # Define category name and allocated budget as private attributes
    self.__category_name = category_name
    self.__allocated_budget = allocated_budget

  def get_category_name(self):
    """
    Returns the category name.
    """
    return self.__category_name

  def set_category_name(self, new_category_name):
    """
    Sets the category name, ensuring it's not empty.

    Args:
      new_category_name (str): The new name for the budget category.
    """
    if not new_category_name:
      raise ValueError("Category name cannot be empty.")
    self.__category_name = new_category_name

  def get_allocated_budget(self):
    """
    Returns the allocated budget.
    """
    return self.__allocated_budget

  def set_allocated_budget(self, new_budget):
    """
    Sets the allocated budget, ensuring it's a positive number.

    Args:
      new_budget (float): The new allocated budget for the category.
    """
    if new_budget <= 0:
      raise ValueError("Allocated budget must be a positive number.")
    self.__allocated_budget = new_budget

  def add_expense(self, expense_amount):
    """
    Adds an expense to the category and updates the remaining budget.

    Args:
      expense_amount (float): The amount of the expense.

    Raises:
      ValueError: If the expense amount is not positive.
    """
    if expense_amount <= 0:
      raise ValueError("Expense amount must be a positive number.")
    # Check if expense amount exceeds remaining budget
    if expense_amount > self.__allocated_budget:
      # Handle potential insufficient budget scenario (optional)
      print("WARNING: Expense exceeds remaining budget!")
    self.__allocated_budget -= expense_amount

#Task4

class BudgetCategory:
  """
  This class represents a Budget Category for personal finance management.
  """

  def __init__(self, category_name, allocated_budget):
    """
    Initializes a BudgetCategory object with a name and allocated budget.

    Args:
      category_name (str): The name of the budget category.
      allocated_budget (float): The total budget allocated to this category.
    """
    # Define category name and allocated budget as private attributes
    self.__category_name = category_name
    self.__allocated_budget = allocated_budget

  def get_category_name(self):
    """
    Returns the category name.
    """
    return self.__category_name

  def set_category_name(self, new_category_name):
    """
    Sets the category name, ensuring it's not empty.

    Args:
      new_category_name (str): The new name for the budget category.
    """
    if not new_category_name:
      raise ValueError("Category name cannot be empty.")
    self.__category_name = new_category_name

  def get_allocated_budget(self):
    """
    Returns the allocated budget.
    """
    return self.__allocated_budget

  def set_allocated_budget(self, new_budget):
    """
    Sets the allocated budget, ensuring it's a positive number.

    Args:
      new_budget (float): The new allocated budget for the category.
    """
    if new_budget <= 0:
      raise ValueError("Allocated budget must be a positive number.")
    self.__allocated_budget = new_budget

  def add_expense(self, expense_amount):
    """
    Adds an expense to the category and updates the remaining budget.

    Args:
      expense_amount (float): The amount of the expense.

    Raises:
      ValueError: If the expense amount is not positive.
    """
    if expense_amount <= 0:
      raise ValueError("Expense amount must be a positive number.")
    # Check if expense amount exceeds remaining budget (optional)
    if expense_amount > self.__allocated_budget:
      # Handle potential insufficient budget scenario (optional)
      print("WARNING: Expense exceeds remaining budget!")
    self.__allocated_budget -= expense_amount

  def display_category_summary(self):
    """
    Displays a summary of the budget category details.
    """
    print(f"Category: {self.__category_name}")
    print(f"Allocated Budget: ${self.__allocated_budget:.2f}")  # Format to 2 decimal places
    print(f"Remaining Budget: ${self.__allocated_budget:.2f}")  # Assuming no initial expenses

# Q2

#Task1

class Product:
  """
  This class represents a base product for an e-commerce platform.
  """

  def __init__(self, product_id, name, price):
    """
    Initializes a Product object with common attributes.

    Args:
      product_id (str): Unique identifier for the product.
      name (str): Name of the product.
      price (float): Price of the product.
    """
    self.product_id = product_id
    self.name = name
    self.price = price

  def display_product_info(self):
    """
    Displays basic product information.
    """
    print(f"Product ID: {self.product_id}")
    print(f"Name: {self.name}")
    print(f"Price: ${self.price:.2f}")  # Format price to 2 decimal places

#Task2

class Product:
  """
  This class represents a base product for an e-commerce platform.
  """

  def __init__(self, product_id, name, price):
    """
    Initializes a Product object with common attributes.

    Args:
      product_id (str): Unique identifier for the product.
      name (str): Name of the product.
      price (float): Price of the product.
    """
    self.product_id = product_id
    self.name = name
    self.price = price

  def display_product_info(self):
    """
    Displays basic product information.
    """
    print(f"Product ID: {self.product_id}")
    print(f"Name: {self.name}")
    print(f"Price: ${self.price:.2f}")  # Format price to 2 decimal places

class Book(Product):
  """
  This class represents a book product with additional attributes.
  """

  def __init__(self, product_id, name, price, author):
    """
    Initializes a Book object with inherited attributes and author.

    Args:
      product_id (str): Unique identifier for the product.
      name (str): Name of the product (book title).
      price (float): Price of the product.
      author (str): Author of the book.
    """
    super().__init__(product_id, name, price)  # Call base class constructor
    self.author = author

class Electronic(Product):
  """
  This class represents an electronic product with additional attributes.
  """

  def __init__(self, product_id, name, price, specs):
    """
    Initializes an Electronic object with inherited attributes and specs.

    Args:
      product_id (str): Unique identifier for the product.
      name (str): Name of the product (electronic device).
      price (float): Price of the product.
      specs (str): Specifications of the electronic device.
    """
    super().__init__(product_id, name, price)  # Call base class constructor
    self.specs = specs

class Clothing(Product):
  """
  This class represents a clothing product with additional attributes.
  """

  def __init__(self, product_id, name, price, size):
    """
    Initializes a Clothing object with inherited attributes and size.

    Args:
      product_id (str): Unique identifier for the product.
      name (str): Name of the product (clothing item).
      price (float): Price of the product.
      size (str): Size of the clothing item.
    """
    super().__init__(product_id, name, price)  # Call base class constructor
    self.size = size

#Task3

class Product:
  """
  This class represents a base product for an e-commerce platform.
  """

  def __init__(self, product_id, name, price):
    """
    Initializes a Product object with common attributes.

    Args:
      product_id (str): Unique identifier for the product.
      name (str): Name of the product.
      price (float): Price of the product.
    """
    self.product_id = product_id
    self.name = name
    self.price = price

  def display_product_info(self):
    """
    Displays basic product information.
    """
    print(f"Product ID: {self.product_id}")
    print(f"Name: {self.name}")
    print(f"Price: ${self.price:.2f}")  # Format price to 2 decimal places

class Book(Product):
  """
  This class represents a book product with additional attributes.
  """

  def __init__(self, product_id, name, price, author):
    """
    Initializes a Book object with inherited attributes and author.

    Args:
      product_id (str): Unique identifier for the product.
      name (str): Name of the product (book title).
      price (float): Price of the product.
      author (str): Author of the book.
    """
    super().__init__(product_id, name, price)  # Call base class constructor
    self.author = author

  def display_product_info(self):
    """
    Overrides the base class method to include author information.
    """
    super().display_product_info()  # Call base class display method
    print(f"Author: {self.author}")

class Electronic(Product):
  """
  This class represents an electronic product with additional attributes.
  """

  def __init__(self, product_id, name, price, specs):
    """
    Initializes an Electronic object with inherited attributes and specs.

    Args:
      product_id (str): Unique identifier for the product.
      name (str): Name of the product (electronic device).
      price (float): Price of the product.
      specs (str): Specifications of the electronic device.
    """
    super().__init__(product_id, name, price)  # Call base class constructor
    self.specs = specs

  def display_product_info(self):
    """
    Overrides the base class method to include specs information.
    """
    super().display_product_info()  # Call base class display method
    print(f"Specs: {self.specs}")

class Clothing(Product):
  """
  This class represents a clothing product with additional attributes.
  """

  def __init__(self, product_id, name, price, size):
    """
    Initializes a Clothing object with inherited attributes and size.

    Args:
      product_id (str): Unique identifier for the product.
      name (str): Name of the product (clothing item).
      price (float): Price of the product.
      size (str): Size of the clothing item.
    """
    super().__init__(product_id, name, price)  # Call base class constructor
    self.size = size

  def display_product_info(self):
    """
    Overrides the base class method to include size information.
    """
    super().display_product_info()  # Call base class display method
    print(f"Size: {self.size}")

#task4

class Product:
  """
  This class represents a base product for an e-commerce platform.
  """

  def __init__(self, product_id, name, price):
    """
    Initializes a Product object with common attributes.

    Args:
      product_id (str): Unique identifier for the product.
      name (str): Name of the product.
      price (float): Price of the product.
    """
    self.product_id = product_id
    self.name = name
    self.price = price

  def display_product_info(self):
    """
    Displays basic product information.
    """
    print(f"Product ID: {self.product_id}")
    print(f"Name: {self.name}")
    print(f"Price: ${self.price:.2f}")  # Format price to 2 decimal places

class Book(Product):
  """
  This class represents a book product with additional attributes.
  """

  def __init__(self, product_id, name, price, author):
    """
    Initializes a Book object with inherited attributes and author.

    Args:
      product_id (str): Unique identifier for the product.
      name (str): Name of the product (book title).
      price (float): Price of the product.
      author (str): Author of the book.
    """
    super().__init__(product_id, name, price)  # Call base class constructor
    self.author = author

  def display_product_info(self):
    """
    Overrides the base class method to include author information.
    """
    super().display_product_info()  # Call base class display method
    print(f"Author: {self.author}")

class Electronic(Product):
  """
  This class represents an electronic product with additional attributes.
  """

  def __init__(self, product_id, name, price, specs):
    """
    Initializes an Electronic object with inherited attributes and specs.

    Args:
      product_id (str): Unique identifier for the product.
      name (str): Name of the product (electronic device).
      price (float): Price of the product.
      specs (str): Specifications of the electronic device.
    """
    super().__init__(product_id, name, price)  # Call base class constructor
    self.specs = specs

  def display_product_info(self):
    """
    Overrides the base class method to include specs information.
    """
    super().display_product_info()  # Call base class display method
    print(f"Specs: {self.specs}")

class Clothing(Product):
  """
  This class represents a clothing product with additional attributes.
  """

  def __init__(self, product_id, name, price, size):
    """
    Initializes a Clothing object with inherited attributes and size.

    Args:
      product_id (str): Unique identifier for the product.
      name (str): Name of the product (clothing item).
      price (float): Price of the product.
      size (str): Size of the clothing item.
    """
    super().__init__(product_id, name, price)  # Call base class constructor
    self.size = size

  def display_product_info(self):
    """
    Overrides the base class method to include size information.
    """
    super().display_product_info()  # Call base class display method
    print(f"Size: {self.size}")

# Test product creation and display
my_book = Book("123", "Python Essentials", 29.99, "J. Doe")
my_electronic = Electronic("456", "Laptop", 499.99, "16GB RAM, 512GB SSD")
my_clothing = Clothing("789", "T-Shirt", 19.99, "M")

print("\nBook Information:")
my_book.display_product_info()

print("\nElectronic Information:")
my_electronic.display_product_info()

print("\nClothing Information:")
my_clothing.display_product_info()
