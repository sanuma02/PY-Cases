def group_by_owners(files):
    d = {}
    for k,v in files.items():
         d.setdefault(v,[]).append(k)
    return d

            

files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}