import re       # to find characters


class DocumentSplitter:

    # splits a legislation into pieces of text
    def split_core_legislation(self, full_legislation):

        full_leg_list = full_legislation.split("\n")

        total_lines = 0

        for line in full_leg_list:

            if total_lines == 0:
                leg_name = line     # first line is the name of the legislation

            total_lines += 1

        content_list = []
        piece_titles = []
        content = ""
        count = 0
        title_count = 0

        for line in full_leg_list:

            count += 1
            x = re.findall("CHAPTER", line)   # finds the set of characters by which each piece should be split

            if len(x) > 0:

                title_number = line.split("CHAPTER", 1)[1].strip()

                # checks for roman numerals in titles of a piece
                if bool(re.search(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$", title_number)):
                    title_count += 1
                    piece_title = str(title_count) + "-" + line
                    piece_titles.append(piece_title)    # title of a piece is taken separately
                    content_list.append(content)        # content within a piece is taken separately
                    content = ""
                    continue

            else:
                content = content + line
                if count == total_lines:
                    content_list.append(content)
                else:
                    continue

        # all pieces(titles and content) are appended to a list
        split_core_legislation = []
        i = 0
        for title in piece_titles:
            piece = {"pieceTitle": title, "content": content_list[i]}
            split_core_legislation.append(piece)
            i += 1

        return leg_name, split_core_legislation    # returned to be stored in the database
