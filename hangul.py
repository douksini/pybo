import re

def extract_english(text):
  """Extracts English text from a Korean string.

  Args:
    text: The Korean string to extract English from.

  Returns:
    A list of English words.
  """

  # Create a regular expression to match English words.
  regex = re.compile(r'[a-zA-Z]+')

  # Extract all matches from the text.
  matches = regex.findall(text)

  # Return a list of the matches.
  return matches

if __name__ == '__main__':
  # Get the Korean text from the user.
  text = input('Enter Korean text: ')

  # Extract the English text from the Korean text.
  english_text = extract_english(text)

  # Print the English text.
  print('The English text is: {}'.format(' '.join(english_text)))