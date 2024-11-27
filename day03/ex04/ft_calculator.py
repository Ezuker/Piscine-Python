from abc import abstractmethod


class calculator:
    @abstractmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        print(f"Dot product is: {sum([x * y for x, y in zip(V1, V2)])}")
        return

    @abstractmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        print(f"Add Vector is : {[float(x + y) for x, y in zip(V1, V2)]}")

    @abstractmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        print(f"Sous Vector is: {[float(x - y) for x, y in zip(V1, V2)]}")
