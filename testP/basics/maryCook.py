def ex2ques():
    people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]

    height_total = 0
    height_count = 0
    for person in people:
        if 'height' in person:
            height_total += person['height']
            height_count += 1

    if height_count > 0:
        average_height = height_total / height_count

    print average_height

def ex2myans():
    people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]

    print reduce(lambda a,x:a+x['height'],filter(lambda p: 'height' in p, people),0)/len(filter(lambda p: 'height' in p, people))


def ex2bookans():
    people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]

    heights = map(lambda x: x['height'],
              filter(lambda x: 'height' in x, people))

    if len(heights) > 0:
        from operator import add
        average_height = reduce(add, heights) / len(heights)

    print average_height


def zero(s):
    if s[0] == "0":
        return s[1:]

def one(s):
    if s[0] == "1":
        return s[1:]

def rule_sequence(s, rules):
    for rule in rules:
        s = rule(s)
        if s == None:
            break

    return s

# def recRuleSeq(s, rules):
#     if(n==len(rules)-1):
#         return rules[n](s)
#         return rule(c)

# def my_rule_seq(s,rules):
#     return recRuleSeq(0)

def ex3ques():
    bands = [{'name': 'sunset rubdown', 'country': 'UK', 'active': False},
         {'name': 'women', 'country': 'Germany', 'active': False},
         {'name': 'a silver mt. zion', 'country': 'Spain', 'active': True}]

    def format_bands(bands):
        for band in bands:
            band['country'] = 'Canada'
            band['name'] = band['name'].replace('.', '')
            band['name'] = band['name'].title()

    format_bands(bands)

    print bands


# ex2ques()
# ex2myans()
# ex2bookans()

# print rule_sequence('0101', [zero, one, zero])
#
# print rule_sequence('0101', [zero, zero])



def assoc(_d, key, value):
    from copy import deepcopy
    d = deepcopy(_d)
    d[key] = value
    return d

def set_canada_as_country(band):
    return assoc(band, 'country', "Canada")

def strip_punctuation_from_name(band):
    return assoc(band, 'name', band['name'].replace('.', ''))

def capitalize_names(band):
    return assoc(band, 'name', band['name'].title())


def pipeline_each(bands, oprs):

    bands = reduce(lambda a, x: map(x, a), oprs, bands)

    # for opr in oprs: bands = map(opr,bands)

    return bands


def ex3myans():
    bands = [{'name': 'sunset rubdown', 'country': 'UK', 'active': False},
         {'name': 'women', 'country': 'Germany', 'active': False},
         {'name': 'a silver mt. zion', 'country': 'Spain', 'active': True}]

    print pipeline_each(bands, [set_canada_as_country,
                            strip_punctuation_from_name,
                            capitalize_names])

ex3ques()
ex3myans()


