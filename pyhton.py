studentdata={"id1": {"name": ["sara"],
            "class":[5],
            "subjectintegration":["english","math","science"]},
            "id2": {"name": ["David"],
            "class":[5],
            "subjectintegration":["english","math","science"]},
            "id3": {"name": ["David"],
            "class":[5],
            "subjectintegration":["english","math","science"]},
            "id4": {"name": ["Jack"],
            "class":[5],
            "subjectintegration":["english","math","science"]}}
result ={}
for key,value in studentdata.items():
    if value not in result.items():
        result[key]=value
print(result)