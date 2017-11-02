from transform_quadrilateral import AreaMapping

real1 = [[479700.0, 5732100], [503100.0, 5739600.0], [510000.0, 5731200.0], [491800.0, 5720600.0]]
real2 = [[491800.0, 5720600.0], [510000.0, 5731200.0], [506700.0, 5715050.0], [502400.0, 5711000.0]]
transf1 = [[0, 0], [0, 1.0], [0.5, 1.0], [0.5, 0]]
transf2 = [[0.5, 0], [0.5, 1.0], [1.0, 1.0], [1.0, 0]]

borssele_mapping1 = AreaMapping(real1, transf1)
borssele_mapping2 = AreaMapping(real2, transf2)

bx = []
by = []
bz = []
m = (real2[0][1] - real2[1][1]) / (real2[0][0] - real2[1][0])
y = real2[0][1]
x = real2[0][0]
b = y - m * x
with open("bathymetry_table.dat", "r") as inp:
    with open("borssele_transformed.dat", "w") as out:
        for line in inp:
            cols = line.split()
            if cols:
                bx.append(float(cols[0]))
                by.append(float(cols[1]))
                bz.append(float(cols[2]))
                if by[-1] >= m * bx[-1] + b:
                    nx, ny = borssele_mapping1.transform_to_rectangle(bx[-1], by[-1])
                else:
                    nx, ny = borssele_mapping2.transform_to_rectangle(bx[-1], by[-1])
                out.write("{} {} {}\n".format(nx, ny, bz[-1]))
            else:
                out.write("\n")
