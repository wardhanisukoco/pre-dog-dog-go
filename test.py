
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels

# Main program function defined below
def main():
    in_arg = get_input_args()
    results = get_pet_labels(in_arg.dir)
    
    
if __name__ == "__main__":
    main()