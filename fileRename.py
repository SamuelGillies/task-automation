import os

Source_Path = '/Users/samgillies/repos/task-automation/datain'
Destination = '/Users/samgillies/repos/task-automation/dataout'


def main():
    for filename in os.listdir(Source_Path):
        dst =  filename[0:3]    

        if dst == '047': 
            count = 0
            count = count + 1
            rename47 = '047' + '-' + count
            os.rename(os.path.join(Source_Path, filename),  os.path.join(Destination, rename47))
            print(filename + 'renamed to ' + rename47)
        
        elif dst == '181':
            count = 0
            count = count + 1
            rename181 = '181' + '-' + count
            os.rename(os.path.join(Source_Path, filename),  os.path.join(Destination, rename181)) 
            print(filename + 'renamed to ' + rename181)

        else:
            os.rename(os.path.join(Source_Path, filename),  os.path.join(Destination, dst))
            print(filename + 'renamed to ' + dst)


# Driver Code
if __name__ == '__main__':
    main()