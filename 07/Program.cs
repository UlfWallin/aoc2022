var cmds = File.ReadAllLines(@"input.txt");
var root = new Dir("/", null);
var currentDir = root;

var totalSpace = 70000000;
var spaceNeeded = 30000000;

foreach(var cmd in cmds) {
    if (cmd.StartsWith("$ cd")) {
        var p = cmd.Split(' ');
        if (p[2] == "..") {
           currentDir = currentDir?.Parent;
        }
        else if (p[2] != "/") {
            var tmp = new Dir(p[2], currentDir);
            currentDir?.Dirs.Add(tmp);
            currentDir = tmp;
        }
    }
    else if(!cmd.StartsWith('$') && !cmd.StartsWith("dir")) {
        currentDir?.Files.Add(new DirFile(cmd));
    }
}
var spaceAvailable = totalSpace - root.CalcSize();
Console.WriteLine($"Space available: {spaceAvailable}. Free up: {spaceNeeded - spaceAvailable}");

var dirSizes = new List<int>();
var delCandidates = new List<int>();
foreach(var d in root.GetTree()) {
    var sz = d.CalcSize();
    if (sz <= 100000) {
        Console.WriteLine(d.Name + " " + sz);
        dirSizes.Add(sz);
    }
    if (sz >= spaceNeeded - spaceAvailable) {
        delCandidates.Add(sz);
    }
}
delCandidates.Sort();
var total = dirSizes.Sum();
Console.WriteLine($"Total: {total}");
Console.WriteLine($"Delete: {delCandidates[0]}");

class Dir {
    public Dir? Parent {get; set;}
    public string Name {get; set;} = "";
    public List<Dir> Dirs {get; set;} = new List<Dir>();
    public List<DirFile> Files {get; set; } = new List<DirFile>();
    
    public Dir (string name, Dir? parent) {
        Name = name;
        Parent = parent;
    } 
    public int CalcSize() {
        var size = 0;
        foreach(var f in Files) {
            size += f.Size;
        }
        foreach(var child in Dirs) {
            size += child.CalcSize();
        }
        return size;
    }

    public IList<Dir> GetTree() {
        var treeItems = new List<Dir>();
        var visited = new HashSet<Dir>();
        var stack = new Stack<Dir>();

        stack.Push(this);

        while(stack.Count > 0) {
            var current = stack.Pop();
            if (!visited.Add(current)) {
                continue;
            }
            treeItems.Add(current);

            foreach(var dir in current.Dirs) {
                stack.Push(dir);
            }
        }
        return treeItems;
    }
}

class DirFile {
    public string Name {get; set;} = "";
    public int Size {get; set;}

    public DirFile(string line) {
        var parts = line.Split(' ');
        Size = Convert.ToInt32(parts[0]);
        Name = parts[1];
    }

    public DirFile(string name, int size) {
        Name = name;
        Size = size;       
    }
}