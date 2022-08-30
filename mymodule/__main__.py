
if __name__ == '__main__':
    import mymodule
    print(f"mymodule version {mymodule.__version__}")
else:
    print(__name__)
