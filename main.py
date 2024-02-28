# Function to sort items based on their count
def sort_on(item):
    return item[1]

# Open the file 'frankenstein.txt' in read mode ('r')
with open('books/frankenstein.txt', 'r') as file:
    # Read the contents of the file
    contents = file.read()


    words = contents.split()



    output_dict = dict()

    

    for w in words:
        for ch in w:
            if ch.isalpha():
                if ch.lower() in output_dict:
                    output_dict[ch.lower()] += 1
                else:
                    output_dict[ch.lower()] = 1

    sorted_characters = sorted(output_dict.items(), key=sort_on, reverse=True)

    # Print the contents
    # print(contents)
    # for i in output_dict:
    #     print(f"The '{i}' character was found {output_dict[i]} times.")
    # Print the report
    print("--- Begin report of books/frankenstein.txt ---") 

    print(len(words), "words found in the document")
    for char, count in sorted_characters:
        print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")
