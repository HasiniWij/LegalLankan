import re


class DocumentSplitter:

    def split_core_legislation(self, full_legislation):

        total_lines = 0
        for line in full_legislation:
            total_lines += 1

        content_list = []
        piece_titles = []
        content = ""
        count = 0
        title_count = 0

        for line in full_legislation:
            count += 1
            x = re.findall("CHAPTER", line)

            if len(x) > 0:

                title_number = line.split("CHAPTER", 1)[1].strip()

                if bool(re.search(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$", title_number)):
                    title_count += 1
                    piece_title = str(title_count) + "-" + line
                    piece_titles.append(piece_title)
                    content_list.append(content)
                    content = ""
                    continue

            else:
                content = content + line
                if count == total_lines:
                    content_list.append(content)
                else:
                    continue

        split_core_legislation = []
        i = 0
        for title in piece_titles:
            piece = {"pieceTitle": title, "content": content_list[i]}
            split_core_legislation.append(piece)
            i += 1

        return split_core_legislation
