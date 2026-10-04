def postcode_area(postcode):
        code = ""
        for c in postcode:

            if c.isdigit():
                return code
            else:
                code = code + c