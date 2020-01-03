def convert(img_file, label_file, out_file, n):
    input_file = open(img_file, 'rb')
    output_file = open(out_file, 'w')
    label_file = open(label_file, 'rb')

    input_file.read(16)
    label_file.read(8)
    images = []

    for i in range(n):
        image = [ord(label_file.read(1))]
        for j in range(28 * 28):
            image.append(ord(input_file.read(1)))
        images.append(image)

    for image in images:
        output_file.write(",".join(str(pix) for pix in image) + "\n")

    input_file.close()
    output_file.close()
    label_file.close()


#convert("data/train-images.idx3-ubyte", "data/train-labels.idx1-ubyte", "data/train_data.csv", 60000)
convert("data/t10k-images.idx3-ubyte", "data/t10k-labels.idx1-ubyte", "data/test_data.csv", 10000)
