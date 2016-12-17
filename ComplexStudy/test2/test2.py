a_list=[[1,2,3],[4,5],[6,7]]
# print a_list[1][1]
a_dic={1:{'name':'lisa'},2:'python',3:'java',4:'c++'}
# print a_dic
# print a_dic[1]['name']
# print a_dic.values()
# print a_dic.keys()
# print a_dic.items()
# for key in a_dic.keys():
#     print "the key is %d : and key's value is %s"%(key,a_dic[key])
# #     print key,a_dic[key]
# for value in a_dic.values():
#     print value
# 
# for k,v in a_dic.items():
#     print str(k)+":"+str(v)
    
print len(a_dic)
new_a_dic=a_dic.copy()
print new_a_dic
new_a_dic.pop(4)
print new_a_dic
del new_a_dic[3]
print new_a_dic
a_dic.update(new_a_dic)
print a_dic






