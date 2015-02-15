"""
Which state contains the most USPS codes within its name?
"""

state_data = \
"""AL Alabama
AK Alaska
AZ Arizona
AR Arkansas
CA California
CO Colorado
CT Connecticut
DE Delaware
FL Florida
GA Georgia
HI Hawaii
ID Idaho
IL Illinois
IN Indiana
IA Iowa
KS Kansas
KY Kentucky
LA Louisiana
ME Maine
MD Maryland
MA Massachusetts
MI Michigan
MN Minnesota
MS Mississippi
MO Missouri
MT Montana
NE Nebraska
NV Nevada
NH New Hampshire
NJ New Jersey
NM New Mexico
NY New York
NC North Carolina
ND North Dakota
OH Ohio
OK Oklahoma
OR Oregon
PA Pennsylvania
RI Rhode Island
SC South Carolina
SD South Dakota
TN Tennessee
TX Texas
UT Utah
VT Vermont
VA Virginia
WA Washington
WV West Virginia
WI Wisconsin
WY Wyoming"""

states = {}
for line in state_data.split('\n'):
    code, name = line.split(' ', 1)
    states[code] = name

def codes_in_name(name):
    converted = ''.join(name.split()).upper()
    length = len(converted)
    i = 0
    codes_found = []
    while i < length:
        potential_code = converted[i : i + 2]
        if potential_code in states and potential_code not in codes_found:
            i += 2
            codes_found.append(potential_code)
        else:
            i += 1
    return codes_found

n, state = max((len(codes_in_name(state)), state) for state in states.values())
print '{} has the most USPS codes in its name ({}) of any state.'.format(state, n)
