def launch_acolite():
    from multiprocessing import freeze_support
    freeze_support()

    import sys
    import os
    import datetime
    import argparse

    try:
        import acolite as ac
    except ImportError:
        print('Could not import ACOLITE source')
        print("Error:", sys.exc_info())
        return

    try:
        from osgeo import ogr, osr, gdal
    except ImportError:
        print('Could not import osgeo')
        print("Error:", sys.exc_info())
        return

    import matplotlib
    matplotlib.use("Agg")

    parser = argparse.ArgumentParser(description='ACOLITE')
    parser.add_argument('--settings', help='settings file', default=None)
    parser.add_argument('--settings_agh', help='settings file for agh', default=None)
    parser.add_argument('--inputfile', help='list of images', default=None)
    parser.add_argument('--output', help='output directory', default=None)
    parser.add_argument('--sensor', help='comma separated sensor list for LUT retrieval', default=None)
    args, unknown = parser.parse_known_args()

    if '--retrieve_luts' in sys.argv:
        ac.acolite.acolite_luts(sensor=args.sensor)
        return

    if args.settings_agh is not None:
        import acolite.gee
        acolite.gee.agh_run(settings=args.settings_agh, acolite_settings=args.settings)
        return

    if '--cli' in sys.argv:
        time_start = datetime.datetime.now()

        inputfile, output = None, None
        if args.inputfile is not None:
            inputfile = args.inputfile.split(',')
        if args.output is not None:
            output = args.output

        if args.settings is None:
            print('No settings file given')
            return
        if not os.path.exists(args.settings):
            print(f'Settings file {args.settings} does not exist.')
            return

        ac.acolite.acolite_run(args.settings, inputfile=inputfile, output=output)
    else:
        print("ACOLITE CLI requires the --cli argument.")

if __name__ == '__main__':
    launch_acolite()