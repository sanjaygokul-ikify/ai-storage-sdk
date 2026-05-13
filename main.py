import argparse
from ai_storage_sdk import StorageSDK

def main():
    parser = argparse.ArgumentParser(description='AI-Powered Storage SDK')
    parser.add_argument('--store', help='Store data')
    parser.add_argument('--retrieve', help='Retrieve data')
    args = parser.parse_args()

    sdk = StorageSDK()

    if args.store:
        sdk.store('data', args.store)
    elif args.retrieve:
        data = sdk.retrieve('data')
        print(data)

if __name__ == '__main__':
    main()