using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FileUtility
{
    public class RecursiveFileSearch
    {
        static System.Collections.Specialized.StringCollection log = new System.Collections.Specialized.StringCollection();

        public static void FileSearch()
        {
            System.IO.DirectoryInfo rootDir = new System.IO.DirectoryInfo(System.IO.Directory.GetCurrentDirectory());

            // get keyword to remove from subdirectories
            Console.Write("Remove all files and subdirectories with this keyword: ");
            string keyword = Console.ReadLine();

            WalkDirectoryTree(rootDir, keyword);

            Console.ReadKey();
        }

        public static void WalkDirectoryTree(System.IO.DirectoryInfo root, string keyword)
        {
            if (keyword == string.Empty)
                return;

            System.IO.FileInfo[] files = null;
            System.IO.DirectoryInfo[] subDirs = null;

            try
            {
                // Find all files in this folder
                files = root.GetFiles();

                // Now find all the subdirectories under this directory.
                subDirs = root.GetDirectories();

                if (files != null)
                {
                    foreach (System.IO.FileInfo fileInfo in files)
                    {
                        string fileName = keyword + fileInfo.Extension;

                        if (fileInfo.Name.EndsWith(fileName, StringComparison.InvariantCultureIgnoreCase) ||
                            fileInfo.Name.Contains(keyword))
                        {
                            fileInfo.Delete();
                            Console.WriteLine("Removed: " + fileInfo.FullName);
                        }
                    }
                }

                if (subDirs != null)
                {
                    foreach (System.IO.DirectoryInfo dirInfo in subDirs)
                    {
                        if (dirInfo.Name.Equals(keyword, StringComparison.InvariantCultureIgnoreCase))
                        {
                            dirInfo.Delete(true);
                            Console.WriteLine("Removed: " + dirInfo.FullName);
                        }

                        // Resursive call for each subdirectory.
                        WalkDirectoryTree(dirInfo, keyword);
                    }
                }
            }

            catch (Exception ex)
            { }
        }
    }
}
