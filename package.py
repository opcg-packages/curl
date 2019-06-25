name = 'curl'

version = '7.65.1'

variants = [
    ['platform-windows', 'arch-AMD64'],
    ['platform-osx', 'arch-x86_64'],
    ['platform-linux', 'arch-x86_64']
]


def commands():
    env.PATH.append('{root}')
