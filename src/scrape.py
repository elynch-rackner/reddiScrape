import argparse
from reddi_scrape import scrape_reddit

def main():
    # Create the parser
    parser = argparse.ArgumentParser()
    # Add the arguments
    parser.add_argument('--subreddit', type=str, 
                        required=True, help='Target subreddit')
    parser.add_argument('--query', type=str, 
                        required=True, help='Desired query')
    parser.add_argument('--after', type=str, 
                        required=True, help='After Date filter.')
    parser.add_argument('--before', type=str, 
                        required=True, help='Before Date filter.')
    parser.add_argument('--size', type=str, 
                        required=True, help='Quantity of Posts to Attempt to Scrape.')
    # Namespace object
    args =parser.parse_args()
    # You can also access the attributes of the Namespace object directly using the vars() 
    # function, which returns a dictionary of the object's attributes and their values.
    kwargs = vars(args)

    # scrape data
    scrape_reddit(**kwargs)


if __name__=='__main__':
    main()
