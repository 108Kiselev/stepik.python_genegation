def build_query_string (d):
    sk = sorted(d)
    q = ''
    if len(sk) == 1:
        q = str(sk[0])+'='+str(d.get(sk[0]))
        return q
    else:
        for i in sk:
            q += str(i)+'='+str(d.get(i))+'&'
        q = q[:-1]
        return q

print(build_query_string({'name': 'timur'}))