import os
def main():
    id = 1
    with open("./rec_results.txt","r") as f:
        lines = f.readlines()
        for line in lines:
            line_list = line.split(",")
            Uid = line_list[0]
            Aid1 = line_list[1]
            Aid2 = line_list[2]
            Aid3 = line_list[3]
            Aid4 = line_list[4]
            store_path = "./_posts/2021-06-19-item-{}.md".format(id)
            open(store_path,"w").close()
            with open(store_path,"a") as fw:
                fw.write("---\n")
                fw.write("layout: entry\n")
                fw.write("Uid: {}\n".format(Uid))
                fw.write("Aid1: {}\n".format(Aid1))
                fw.write("Aid2: {}\n".format(Aid2))
                fw.write("Aid3: {}\n".format(Aid3))
                fw.write("Aid4: {}\n".format(Aid4))
                fw.write("---\n\n")
            id = id + 1

if __name__ == '__main__':
    main()