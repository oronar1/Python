import csv

def delete_users(o_fnm,o_lsnm):
    
    with open("users.csv","r+") as file:
        csv_reader=csv.reader(file)
        rows=list(csv_reader)
        
    count=0    
    with open("users.csv","w") as csfile:    
        csv_writer=csv.writer(csfile)
        for row in rows:
            if o_fnm == row[0] and o_lsnm == row[1]:
            
                count+=1
            else:
                csv_writer.writerow(row)
        return "Users deleted: {}.".format(count)
