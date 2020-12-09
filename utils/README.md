
# Utilities and useful scripts for working with the FIRE project

### TODO
- [ ] Create a CSV of all FIRE variables and possible values (if applicable). The CSV should look something like:

| schema | property | type | possible value (if finite) | description |
|--------|----------|------|----------------------------|-------------|
|        |          |      |                            |             |

to achieve this, create a script in this folder that loops through the various json schemas found in `v1-dev` and extracts the information you want in the table into a python dictionary which can then be written to a CSV file.

Create some useful tests to test it is working
- [ ] what if there are no schemas in the folder?
- [ ] what if schemas have no properties?
- [ ] what if a schema says it is an enum but has no list of values?
- [ ] write an actual harcoded result for a sample schema
