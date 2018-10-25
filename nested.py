class Solution():
    def __init__(self):
        self.answer = None
        self.current_offset = 0
    def answer(self):
        return self.answer

    def whitespace(self, n):
        retval = ""
        if n is None:
            n = self.current_offset
        for s in list(xrange(n)):
            retval += " "
        return retval

    def execute(self, remaining_input, acc):
        if len(remaining_input.keys()) == 0:
            return acc
        else:
            for key in remaining_input:
                remaining_input[key]

    def allowed_item(self,item):
        chrs = []
        for n in range(ord('a'), ord('z')):
            chrs.append(chr(n))
        return(item in chrs)

    def execute(self, nested_input):
        # nested_input is an arbitrarily nested dict of dicts
        sref = ""
        retval = execute(self, nested_input, sref)
        return retval


    def test_cases(self):
        testcases=[]
        testcases.append(())
        testcases.append(('a',()))
        testcases.append(('a',('b',)))
        testcases.append(('a',('b',(),'c',())))
        testcases.append(('a',('b',(),'c',(),'d',()), 'e',(), 'f',()))

        test_case_map = {}
        test_case_map[testcases[0]] = ""
        test_case_map[testcases[1]] = "a"
        test_case_map[testcases[2]] = "a\n b"
        test_case_map[testcases[3]]="a\n b\n c"
        test_case_map[testcases[4]]="a\n b\n c\n d\ne\nf\n"

        for tc in testcases:
            print("----------------input:")
            print(tc)
            print("------expected result: ")
            print(test_case_map[tc])
        return test_case_map


def main():
    sol = Solution()
    # sol.test_cases()
    sol.chars('g')

if __name__ == "__main__":
    main()

