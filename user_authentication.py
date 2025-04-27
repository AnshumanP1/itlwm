def login(username, password):
  """
  Authenticates a user based on username and password.

  Args:
    username: The user's username.
    password: The user's password.

  Returns:
    True if the login is successful (for now, just checks for non-empty inputs).

  Raises:
    ValueError: If either username or password is empty.
  """
  if not username or not password:
    raise ValueError("Username and password cannot be empty.")
  # Placeholder for actual authentication logic
  return True
