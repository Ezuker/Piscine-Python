ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = "World!"

u, v = ft_tuple
v = "France!"
ft_tuple = (u, v)

ft_set.remove('tutu!')
ft_set.add("Angouleme")
ft_set = sorted(ft_set, reverse=True) #maybe forbidden

ft_dict['Hello'] = "42Angouleme"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)