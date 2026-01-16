import dflex.sim

builder = dflex.sim.ModelBuilder()

builder.add_particle((0,1,0), (0,0,0,0), 0.0)

for i in range(1,10):
    builder.add_particle((i,1,0), (0,0,0,0), 1.0)
    builder.add_spring(i-1, i, 1000.0, 0.0, 0)

builder.add_shape_plane((0,1,0,0),0)

model = builder.finalize('cuda')

print(model.__dict__)