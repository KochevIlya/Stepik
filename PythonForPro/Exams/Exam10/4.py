def build_query_string(params):
    strg = [str(i) + "=" + str(k) + "&" for i, k in params.items()]
    strg.sort()
    strg[len(strg) - 1] = strg[len(strg) - 1][:-1]
    strg = "".join(strg)
    return strg
#print(build_query_string(input()))





