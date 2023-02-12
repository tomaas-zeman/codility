# inputs: [ [ input_1_param_1, input_1_param_2, ... , input_1_param_N ], [ ... input_2 ...] ]
def test(inputs, results, test_function):
    all_ok = True

    for i in range(0, len(inputs)):
        args = len(inputs[i])
        if args == 1:
            result = test_function(inputs[i][0])
        elif args == 2:
            result = test_function(inputs[i][0], inputs[i][1])
        elif args == 3:
            result = test_function(inputs[i][0], inputs[i][1], inputs[i][2])
        else:
            raise Exception("Unsupported number of test function parameters. Maximum is 3")

        print("Testing for input ...", inputs[i])
        if result == results[i]:
            print("Result ... OK")
        else:
            all_ok = False
            print("Result:", result, ", expected result:", results[i])
        print("-----------------")

    if not all_ok:
        print("At least one test failed")
