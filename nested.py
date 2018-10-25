class Solution():
    def __init__(self):
        self.answer = None
        self.current_offset = 0
    def answer(self):
        return self.answer

    def whitespace(self, n=None):
        retval = ""
        if n is None:
            n = self.current_offset
        for s in list(xrange(n)):
            retval += " "
        return retval

    def allowed_item(self,item):
        chrs = []
        for n in range(ord('a'), ord('z')):
            chrs.append(chr(n))
        return(item in chrs)

    # If the item is a char, you immediately add character to the accumulator as a string, and increment
    # the current_offset by 1, and add a newline to the accumulator

    def execute_internal(self, remaining_input, acc):
        if len(remaining_input) > 0:
            for i,x in enumerate(remaining_input):
                if x == ():
                    continue
                else:
                    if self.allowed_item(x):
                        acc += (self.whitespace()+x+"\n")
                    else:
                        self.current_offset += 1
                        return self.execute_internal(x,acc)
        return acc

    def execute(self, nested_input):
        # nested_input is an arbitrarily nested tuple
        sref = ""
        retval = self.execute_internal(nested_input, sref)
        return retval


    def test_cases(self,show=False, inputsOnly=False):
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

        if show:
            for tc in testcases:
                print("----------------input:")
                print(tc)
                print("------expected result: ")
                print(test_case_map[tc])

        if inputsOnly:
            return testcases
        else:
            return {'testcases':testcases, 'testcasemap': test_case_map}



def main():
    testcasedata = Solution().test_cases(show=False, inputsOnly=False)
    cases = testcasedata['testcases']
    tcmap = testcasedata['testcasemap']

    for index, case in enumerate(cases[0:6]):
        print("\n\nTest {0}...".format(index))
        print("Input:\n{0}\n".format(case))
        print("Your output:\n{0}\n".format(Solution().execute(case)))
        print("Desired output:\n{0}\n".format(tcmap[case]))
if __name__ == "__main__":
    main()

