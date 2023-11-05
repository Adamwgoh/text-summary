from unstructured.partition.pdf import partition_pdf

elements = partition_pdf(filename="Upward and Downward scaffolds.pdf")

texts = [x.text for x in elements]
print("\n\n".join([str(el) for el in elements])) 

import pdb; pdb.set_trace()