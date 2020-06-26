def camel_to_snake(txt):
        import re
        d = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', txt)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', d).lower()

print(camel_to_snake('ASDFGHJcffd'))