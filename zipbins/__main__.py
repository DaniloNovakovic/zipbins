
from zipbins.csproj import zip_bins
from zipbins.argparser import get_args


def main():
    args = get_args()
    zip_bins(args.root_path, args.output_dest)
    print(f"\nFinished zipping to '{args.output_dest}'")


if __name__ == "__main__":
    main()
