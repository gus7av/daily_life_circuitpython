import build

while True:

    user_key = input("Hvilken toneart ønsker du?").upper()

    while not build.is_valid_key(user_key, build.chromatic):
        print("Dette er ikke en gyldig toneart")
        user_key = input("Hvilken toneart ønsker du?").upper()

    if build.is_valid_key(user_key, build.chromatic):
        new_chromatic = build.make_new_chrom(build.chromatic.index(user_key), build.chromatic)
        for step, mode_name in list(enumerate(build.modes)):
            scale_type = build.build_scales(new_chromatic, build.change_mode(step, build.base_mode))
            print(step, mode_name, scale_type)
