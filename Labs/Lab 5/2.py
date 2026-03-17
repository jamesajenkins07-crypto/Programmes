def hello_world():
    print("Hello World")

def hello_world_n_times(n):
    for i in range(n):
        hello_world()

def main():
    hello_world_n_times(2)
    hello_world_n_times(1)
    hello_world_n_times(3)
    hello_world_n_times(2)

main()
