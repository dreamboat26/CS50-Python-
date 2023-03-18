name = input("Enter a name: ")
snake_case_name = ''.join(['_'+c.lower() if c.isupper() else c for c in name]).lstrip('_')
print(snake_case_name)
