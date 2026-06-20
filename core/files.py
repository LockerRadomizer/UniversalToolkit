import os

def clean_temp():
    count = 0

    for root, dirs, files in os.walk("/tmp"):
        for f in files:
            try:
                os.remove(os.path.join(root, f))
                count += 1
            except:
                pass

    return count

def large_files(path="/home", size_mb=100):

    results = []

    for root, dirs, files in os.walk(path):

        for f in files:

            try:
                full = os.path.join(root, f)

                size = os.path.getsize(full) / 1024 / 1024

                if size > size_mb:
                    results.append(
                        (full, round(size, 1))
                    )

            except:
                pass

    results.sort(key=lambda x: x[1], reverse=True)

    return results[:100]