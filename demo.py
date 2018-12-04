import pyspark

def main():
    with pyspark.SparkContext("local", "gupi") as sc:
        
        print("hellow world from gopi")

if __name__ == "__main__":
    main()