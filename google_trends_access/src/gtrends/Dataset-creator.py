import sys
from gtrends_access import GTrendsAccessor



def main():
    try:
                kwd = sys.argv[1]
    except:
                kwd = 'Vote'
            
    try:
                region = sys.argv[2]
    except:
                region = None
                
    try:
                tf = sys.argv[3]
    except:
                tf = 'today 5-y'
            
    try:
                graph = sys.argv[4]
    except:
                graph = None
        
    df = GTrendsAccessor().api_result(kwd, region, tf, graph)

    print (df)
    
# This if-condition is True if this file was executed directly.
# It's False if this file was executed indirectly, e.g. as part
# of an import statement.
if __name__ == "__main__":
    main()
