from parameters.basic_data import Dict_Brack, Brackets


class Stack(list):
    # проверка стека на пустоту
    def isEmpty(self):
        return len(self) == 0

    # добавляет новый элемент на вершину стека
    def push(self, new_element):
        self.append(new_element)

    # возвращает верхний элемент стека, но не удаляет его
    def peek(self):
        if not self.isEmpty():
            return self[-1]

    # возвращает количество элементов в стеке
    def size(self):
        return len(self)


def top_element(element):
    stack = Stack()
    for top in element:
        if top in Dict_Brack:
            stack.push(top)
        elif top == Dict_Brack.get(stack.peek()):
            stack.pop()

        else:
            return " - Несбалансированно"
    return " - Сбалансированно"


if __name__ == '__main__':
    for seq in Brackets:
        print(f'{seq}{top_element(seq)}')
