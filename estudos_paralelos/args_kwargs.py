def teste_args_kwargs(arg1, arg2, arg3, *args):
    print('Arg1:', arg1)
    print('Arg2:', arg2)
    print('Arg3:', arg3)
    for arg in args:
        print('Arg Other:', arg)
    print('=' * 20)


args = ('um', 2, 3)
kwargs = {'arg3': 3, 'arg2': 'dois', 'arg1': 'um'}
teste = (1, 2, 3, True)
teste_args_kwargs(*args)
teste_args_kwargs(**kwargs)
teste_args_kwargs(*teste)