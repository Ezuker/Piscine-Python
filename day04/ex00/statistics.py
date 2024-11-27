from math import sqrt


def ft_statistics(*args: any, **kwargs: any) -> None:
    for item, value in kwargs.items():
        if len(args) != 0:
            match value:
                case "mean":
                    print(f"mean : {sum(args) / len(args)}")
                case "median":
                    print(f"median : {sorted(args)[int(len(args) / 2)]}")
                case "quartile":
                    tmp = sorted(args)
                    lastQ = float(tmp[int(len(args) / 4 * 3)])
                    lst = [float(tmp[int(len(args) / 4)]), lastQ]
                    print(f"quartile : {lst}")
                case "std":
                    mean = sum(args) / len(args)
                    lst = [pow((x - mean), 2) for x in args]
                    print(f"std: {sqrt(sum(lst) / len(args))}")
                    pass
                case "var":
                    mean = sum(args) / len(args)
                    lst = [pow((x - mean), 2) for x in args]
                    print(f"variance: {sum(lst) / len(args)}")
                    pass
        else:
            print("ERROR")
