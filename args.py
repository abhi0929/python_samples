l=[2,31,40,44,62,11,13]
def cel(x):
    list(map( ))

company_budget=500000
def company_tracker():
    total_projects=100
    def update_projects():
        nonlocal total_projects
        global company_budget
        total_projects+=20
        company_budget+=100000
    update_projects()
    print(total_projects)
    print(company_budget)
company_tracker()

l=[lambda x:x*2,lambda x:x*3,lambda x:x*4]
def apply_all(fun,value):
    for i in fun: