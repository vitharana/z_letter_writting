import cv2
import numpy as np
import os

class Z_Scanner:
    def __init__(self):
        self.img_height = 0
        self.img_width = 0
        self.image_name = 'output_image7.jpg'
        self.original_image_gray = 'output_image7.jpg'
        self.original_image_color = 'output_image7.jpg'
        #picture num
        self.num = 0

    def read_image_grayscale_vertically(self, image_name):
        self.image_name = image_name
        self.original_image_color = cv2.imread(self.image_name)
        image = cv2.imread(image_name, cv2.IMREAD_GRAYSCALE)
        self.original_image_gray = image
        height, width = image.shape
        self.img_width = width
        self.img_height = height

        pixel_readings = []
        for y in range(self.img_height):
            for x in range(self.img_width):
                # Access the pixel value at (x, y)
                pixel_value = image[y, x]
                if pixel_value < 200:
                    pixel_readings.append(((y, x), pixel_value))
        return pixel_readings

    def read_image_grayscale_horizontally(self, image_name):
        self.image_name = image_name
        self.original_image_color = cv2.imread(self.image_name)
        image = cv2.imread(image_name, cv2.IMREAD_GRAYSCALE)
        self.original_image_gray = image
        height, width = image.shape
        self.img_width = width
        self.img_height = height
        self.image_name = image_name

        pixel_readings = []
        for y in range(self.img_width):
            for x in range(self.img_height):
                # Access the pixel value at (x, y)
                pixel_value = image[y, x]
                if pixel_value < 200:
                    pixel_readings.append(((y, x), pixel_value))
        return pixel_readings

    def create_blank_img(self):
        highlight_image = np.ones((self.img_height, self.img_width, 1), dtype=np.uint8) * 255
        return highlight_image

    def find_line_thickness(self):
        pixel_locations = self.read_image_grayscale_vertically(self.image_name)
        (y, x), pix_val = pixel_locations[0]

        # get thickness
        x_min = x + 10
        x_max = x + 10
        y_min = y - 10
        y_max = y + 10

        # add test circle
        center = (x, y)  # Center coordinates of the circle
        radius = 3  # Radius of the circle
        color = (0, 255, 0)  # Green color in BGR format
        thickness = 1  # Thickness of the circle outline

        # Draw a circle
        blank = self.original_image_color
        cv2.circle(blank, center, radius, color, thickness)
        center = (x, y + 5)  # Center coordinates of the circle
        cv2.circle(blank, center, radius, color, thickness)

        # Define line parameters
        start_point = (x_min, y_min)  # Starting point of the line
        end_point = (x_max, y_max)  # Ending point of the line
        color = (0, 0, 255)  # Green color in BGR format
        thickness = 1  # Thickness of the line

        # Draw a line
        cv2.line(blank, start_point, end_point, color, thickness)

        image = self.original_image_gray
        n = 0
        for y in range(y_min, y_max):

            pixel_value = image[y, x_min]
            print(y, pixel_value)

            if pixel_value < 200:
                n += 1
        print(n)
        cv2.imshow("first_point", blank)

        print("hhii")

        return n

    def find_line_thickness_2(self):
        pixel_locations = self.read_image_grayscale_vertically(self.image_name)
        (y, x), pix_val = pixel_locations[0]

        # get thickness
        x_min = x + 10
        x_max = x + 10
        y_min = y - 10
        y_max = y + 10

        # add test circle
        center = (x, y)  # Center coordinates of the circle
        radius = 3  # Radius of the circle
        color = (0, 255, 0)  # Green color in BGR format
        thickness = 1  # Thickness of the circle outline

        # Draw a circle
        blank = self.original_image_color
        cv2.circle(blank, center, radius, color, thickness)
        center = (x, y + 5)  # Center coordinates of the circle
        cv2.circle(blank, center, radius, color, thickness)

        # Define line parameters
        start_point = (x_min, y_min)  # Starting point of the line
        end_point = (x_max, y_max)  # Ending point of the line
        color = (0, 0, 255)  # Green color in BGR format
        thickness = 1  # Thickness of the line

        # Draw a line
        cv2.line(blank, start_point, end_point, color, thickness)

        image = self.original_image_gray
        n = 0
        for y in range(y_min, y_max):

            pixel_value = image[y, x_min]
            # print(y,pixel_value)

            if pixel_value < 200:
                n += 1
        # print(n)
        # cv2.imshow("first_point",blank)

        # print("hhii")

        return n

    def draw_top_line(self):

        total_z = []

        line_thickness = self.find_line_thickness()
        pixel_locations = self.read_image_grayscale_horizontally(self.image_name)
        (y, x), pix_val = pixel_locations[0]
        # print(line_thickness, pixel_locations)
        b_image = self.create_blank_img()
        for col in range(x - 5, self.img_width):
            for row in range(y, y + line_thickness):
                # print(col,row)
                pixel_value = self.original_image_gray[row, col]
                if pixel_value < 200:
                    total_z.append(((row, col), pixel_value))

                b_image[row, col] = pixel_value
                cv2.imshow("test", b_image)
                # cv2.waitKey(1)

        pixel_readings = []
        (yy, xx), pix_vall = pixel_locations[-1]

        for row in range(y + line_thickness, yy - line_thickness + 1):
            for col in range(self.img_width):
                pixel_value = self.original_image_gray[row, col]
                # b_image[row,col]= pixel_value

                if pixel_value < 200:
                    pixel_readings.append(((row, col), pixel_value))

                    total_z.append(((row, col), pixel_value))

        b_image = self.create_blank_img()
        for loc in pixel_readings:
            (row, col), pix_val = loc
            b_image[row, col] = pix_val
            # cv2.waitKey(1)
            cv2.imshow("tes3t", b_image)

        # last pixel coordinates

        line_thickness = self.find_line_thickness()
        pixel_locations = self.read_image_grayscale_horizontally(self.image_name)
        (y, x), pix_val = pixel_locations[-1]
        # print(line_thickness, pixel_locations)
        b_image = self.create_blank_img()
        for col in range(0, self.img_width):
            for row in range(y - line_thickness + 1, y + 3):
                # print(col, row)
                pixel_value = self.original_image_gray[row, col]
                b_image[row, col] = pixel_value
                if pixel_value < 200:
                    total_z.append(((row, col), pixel_value))
                cv2.imshow("tessst", b_image)
                # cv2.waitKey(1)

        b_image = self.create_blank_img()
        for loc in total_z:
            (row, col), pix_val = loc
            b_image[row, col] = pix_val
            cv2.waitKey(1)
            cv2.imshow("total_z", b_image)

    def get_total_z_coordinates(self):

        total_z = []

        line_thickness = self.find_line_thickness_2()
        pixel_locations = self.read_image_grayscale_horizontally(self.image_name)
        (y, x), pix_val = pixel_locations[0]
        # print(line_thickness, pixel_locations)
        b_image = self.create_blank_img()
        for col in range(x - 5, self.img_width):
            for row in range(y, y + line_thickness):
                # print(col,row)
                pixel_value = self.original_image_gray[row, col]
                if pixel_value < 200:
                    total_z.append(((row, col), pixel_value))

                b_image[row, col] = pixel_value
                # cv2.imshow("test",b_image)
                # cv2.waitKey(1)

        pixel_readings = []
        (yy, xx), pix_vall = pixel_locations[-1]

        for row in range(y + line_thickness, yy - line_thickness + 1):
            for col in range(self.img_width):
                pixel_value = self.original_image_gray[row, col]
                # b_image[row,col]= pixel_value

                if pixel_value < 200:
                    pixel_readings.append(((row, col), pixel_value))

                    total_z.append(((row, col), pixel_value))

        b_image = self.create_blank_img()
        for loc in pixel_readings:
            (row, col), pix_val = loc
            b_image[row, col] = pix_val
            # cv2.waitKey(1)
            # cv2.imshow("tes3t", b_image)

        # last pixel coordinates

        line_thickness = self.find_line_thickness_2()
        pixel_locations = self.read_image_grayscale_horizontally(self.image_name)
        (y, x), pix_val = pixel_locations[-1]
        # print(line_thickness, pixel_locations)
        b_image = self.create_blank_img()
        for col in range(0, self.img_width):
            for row in range(y - line_thickness + 1, y + 3):
                # print(col, row)
                pixel_value = self.original_image_gray[row, col]
                b_image[row, col] = pixel_value
                if pixel_value < 200:
                    total_z.append(((row, col), pixel_value))
                # cv2.imshow("tessst", b_image)
                # cv2.waitKey(1)

        b_image = self.create_blank_img()
        for loc in total_z:
            (row, col), pix_val = loc
            b_image[row, col] = pix_val
            # cv2.waitKey(1)
            # cv2.imshow("total_z", b_image)

        return total_z

    def draw_shape(self, list, a="default", time_out=0):

        b_image = self.create_blank_img()
        for loc in list:
            (row, col), pix_val = loc
            b_image[row, col] = pix_val
            if time_out > 0:
                cv2.waitKey(time_out)
            cv2.imshow(a, b_image)
    def draw_shape_save(self, list, a="default", time_out=0):

        b_image = self.create_blank_img()
        for loc in list:
            (row, col), pix_val = loc
            b_image[row, col] = pix_val
            if time_out > 0:
                cv2.waitKey(time_out)
            cv2.imshow(a, b_image)
        return b_image

    def add_defects(self, list, div=10, time_out=0, defect_pos=0):

        no_of_pixels = len(list)
        total_pixels = no_of_pixels
        no_of_pixels /= div
        # no_of_pixels = int(no_of_pixels)
        #print(no_of_pixels)

        start = defect_pos * no_of_pixels
        end = start + no_of_pixels
        if end > total_pixels:
            end = total_pixels

        new_list = []
        n = 0
        pixel_locations = list
        for location in pixel_locations:
            (y, x), pix_val = location
            if (n > start and n < end):
                pix_val = np.random.randint(0, 256)
                # cv2.waitKey(10)
                # cv2.imshow("Saved Pixel Locations", highlight_image)

            n += 1
            new_list.append(((y, x), pix_val))

        return new_list

    def generate_list_of_random_locations(self,no_of_div):

        pass

    def generate_defects(self, list, allowed_defected_pixels=500, allowed_defected_divisions=5, time_out=0):
        print(f"list {list}")
        new_list_values = []
        pixel_locations = list
        for location in pixel_locations:
            (y, x), pix_val = location
            new_list_values.append(pix_val)

        no_of_pixels = len(list)
        no_of_divisions = no_of_pixels / allowed_defected_pixels

        no_of_divisions = int(no_of_divisions)
        print(f"no of div {no_of_divisions} , total pixels {no_of_pixels} ")

        selected_defect_locations = []

        for loc in range(np.random.randint(allowed_defected_divisions+1)):
            selected_defect_locations.append(np.random.randint(no_of_divisions))

        print(selected_defect_locations)

        for loc in selected_defect_locations:

            start = loc * allowed_defected_pixels
            end = start + allowed_defected_divisions
            if end > no_of_pixels:
                end = no_of_pixels

            for j in range(start,end):
                new_list_values[j] = np.random.randint(0, 256)

        print(len(list),len(new_list_values))

        new_defected_list = []
        for t in range(len(list)):
            (y, x), pix_val = list[t]
            pixel_value_of_defected = new_list_values[t]
            #print(pix_val,pixel_value_of_defected)
            new_defected_list.append(((y, x), pixel_value_of_defected))

        print(new_defected_list)
        print(list)
        return new_defected_list


    def add_defect_on_location(self,list,allowed_d_pixs=5,allowed_d_loc=5):
        no_of_pixels = len(list)
        no_of_div = no_of_pixels/allowed_d_pixs

        selected_defect_locations = []

        #for loc in range(np.random.randint(allowed_d_loc + 1)):
        for loc in range(allowed_d_loc):
            selected_defect_locations.append(np.random.randint(no_of_div))

        return no_of_div , selected_defect_locations


    def save_img(self,image):

        output_folder = 'generated'

        # Create the folder if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)

        print(self.num)

        output_path = os.path.join(output_folder, f'output_image{self.num}.jpg')
        self.num += 1
        cv2.imwrite(output_path, image)






        """


        start = defect_pos*no_of_pixels
        end = start + no_of_pixels
        if end > total_pixels:
            end = total_pixels


        new_list = []
        n = 0
        pixel_locations = list
        for location in pixel_locations:
            (y, x), pix_val = location
            if (n > start and n < end):
                pix_val = np.random.randint(0, 256)
                #cv2.waitKey(10)
                #cv2.imshow("Saved Pixel Locations", highlight_image)

            n += 1
            new_list.append(((y, x), pix_val))

        return new_list

        """

