# Converting a string into a variable name using exec()
variable_name = "my_dynamic_variable"
variable_value = (True,15,3)

# Create the variable dynamically using exec()
exec(f"{variable_name} = {variable_value}")

# Accessing the dynamically created variable
# retrieved_value = my_dynamic_variable
print(my_dynamic_variable)


