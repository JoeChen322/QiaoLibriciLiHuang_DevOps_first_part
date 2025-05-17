#    Copyright 2025 Simone Reale

#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

import sys
import random
import os

index = int(sys.argv[1])
output_dir = "random_images"
width, height = 100, 100

os.makedirs(output_dir, exist_ok=True)
filename = os.path.join(output_dir, f"random_image_{index+1}.ppm")

with open(filename, "w") as f:
    f.write("P3\n")
    f.write(f"{width} {height}\n")
    f.write("255\n")
    for _ in range(height):
        row = []
        for _ in range(width):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            row.extend([str(r), str(g), str(b)])
        f.write(" ".join(row) + "\n")
