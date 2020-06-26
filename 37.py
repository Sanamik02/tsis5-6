def snake_to_camel(text):
        import re
        d = re.sub("([a-z0-9])([A-Z])", r'\1_\2', text)
        return  re.sub("(.)([A-Z][a-z]+)", r'\1_\2',d).upper()

print(snake_to_camel("sdfghjkk;l"))