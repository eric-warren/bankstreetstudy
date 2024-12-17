

def get_valid(df):
    # Define the valid list of postal codes
    valid_postal_codes = [
    'K1L','K1J','K1K','K1M','K1R','J8X','K4A','K1H','K1B','K1Y','K1Z',
    'K1P','J8P','K2E','J8Y','K2A','G3N','J9A','K1V','K2P','K1C','J8T',
    'J8Z','K1W','K1G','K2G','K2B','K1S','J8R','J9H','K1E','J8L','K4B',
    'J9J','K1X','J8M','K1A','K2C','K2R','J9B','K4P','K2J','K2M','K4C',
    'K2K','K2L','K2H','K4M','K2T','J8V','K2V','K4R','K1N','K2W','K4K',
    'K2S','K0C','K1T','J8N','K0B','K7C','K7S','K7A','L7A','J0V','K0A',
    'K0E','G3Z','K7V','K7H','J0X','K0G'
    ]

    # Convert the valid postal codes to a set for faster lookup
    valid_postal_codes_set = set(valid_postal_codes)

    # Define a mapping for special characters to their keyboard shift equivalents
    special_char_map = {
        '!': '1', '@': '2', '#': '3', '$': '4', '%': '5', '^': '6', '&': '7', 
        '*': '8', '(': '9', ')': '0', '_': '-', '+': '=', '[': '{', ']': '}',
        '{': '[', '}': ']', '\\': '|', ';': ':', "'": '"', ',': '<', '.': '>',
        '/': '?', '`': '~'
    }

    # Function to replace special characters based on the map
    def replace_special_characters(postal_code):
        return ''.join(special_char_map.get(char, char) for char in postal_code)

    # Function to check if the postal code is valid after cleaning
    def is_valid_postal_code(postal_code):
        # Check if the postal code is exactly 3 characters long and in the valid set
        return postal_code in valid_postal_codes_set

    # Clean the postal codes by replacing special characters and stripping any extra spaces
    df['Cleaned_PostalCode'] = df['Q5_PostalCode'].apply(lambda x: replace_special_characters(str(x).strip()).upper())

    # Check if the cleaned postal code is valid (after special char replacement)
    df['Is_Valid'] = df['Cleaned_PostalCode'].apply(lambda x: is_valid_postal_code(x) if len(x) == 3 else False)

    # Filter rows where postal code is invalid (either too short or not matching valid list)
    valid_postal_codes = df[df['Is_Valid'] == True]
    invalid_postal_codes = df[df['Is_Valid'] == False]
    return valid_postal_codes

def get(df,code):
    codes = df[df['Cleaned_PostalCode'].isin(code)]
    return codes