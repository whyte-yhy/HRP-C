package test;

import org.jetbrains.annotations.NotNull;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.*;

public class FPGAPlacing {

    List<LinkedList<Integer>> cnf = new LinkedList<>();
    Map<String, Integer> vars = new HashMap<>();  // 变量名称，具体变量
    int v;  // var从1开始，记录当前应该是第几个var
    int logic_unit_num;  // 逻辑单元数量，从1开始
    int row;  // 行数，从1开始
    int col;  // 列数，从1开始

    int hard_c_num;
    int soft_c_num;
    int c_num;
    int var_num;
    int hard_weight;  // 可能需要改成 long

    // 构造函数，控制输入
    public FPGAPlacing() {
        v = 1;
        hard_c_num = 0;
        soft_c_num = 0;
        c_num = 0;
        var_num = 0;
        Scanner sc = new Scanner(System.in);
        System.out.println("输入逻辑单元数量...");
        logic_unit_num = sc.nextInt();
        System.out.println("输入阵列行数...");
        row = sc.nextInt();
        System.out.println("输入阵列列数...");
        col = sc.nextInt();
    }

    public void mainProcess() throws IOException {

        // 软子句，尽可能紧凑，如果Vxy上有东西，那么它的四周最好也有东西
        for (int x=1; x<=row; x++) {
            for (int y=1; y<=col; y++) {
                String var_name = "v_" + x + y;
                int var = getVar(var_name);
                LinkedList<Integer> surround_vars = get_surround_vars(var_name);
                for (int surround_var : surround_vars) {
                    LinkedList<Integer> clause = new LinkedList<>();
                    clause.add(1);  // 软子句
                    clause.add(-var);
                    clause.add(surround_var);
                    cnf.add(new LinkedList<>(clause));
                    soft_c_num++;
                }
            }
        }

        hard_weight = soft_c_num + 1;  // 因为软子句的权重都设为1

        // 硬子句，每个逻辑单元必须放在物理单元上
        for (int m = 1; m <= logic_unit_num; m++) {
            LinkedList<Integer> clause = new LinkedList<>();
            clause.add(hard_weight);  // 硬子句
            for (int x=1; x<=row; x++) {
                for (int y = 1; y <= col; y++) {
                    String var_name = "v_" + m + x + y;
                    int var = getVar(var_name);
                    clause.add(var);
                }
            }
            cnf.add(new LinkedList<>(clause));
            hard_c_num++;
        }

        // 硬子句，每个逻辑单元只能放在一个物理单元上（每种逻辑单元的数量为1）
        for (int m=1; m<=logic_unit_num; m++) {
            for (int x=1; x<=row; x++) {
                for (int y=1; y<=col; y++) {
                    String var_name = "v_" + m + x + y;
                    int var1 = getVar(var_name);

                    for (int x1=1; x1<=row; x1++) {
                        for (int y1=1; y1<=col; y1++) {
                            if (x1==x && y1==y) continue;
                            var_name = "v_" + m + x1 + y1;
                            int var = getVar(var_name);
                            LinkedList<Integer> clause = new LinkedList<>();
                            clause.add(hard_weight);
                            clause.add(-var1);
                            clause.add(-var);
                            cnf.add(new LinkedList<>(clause));
                            hard_c_num++;
                        }
                    }

                }
            }
        }

        // 硬子句，两个逻辑单元不能在同一个物理单元上
        for (int x=1; x<=row; x++) {
            for (int y=1; y<=col; y++) {
                String var_name;
                for (int m=1; m<=logic_unit_num; m++) {
                    // 创建第一个变量
                    var_name = "v_" + m + x + y;
                    int var1 = getVar(var_name);

                    for (int n=m+1; n<=logic_unit_num; n++) {
                        // 创建新的子句
                        LinkedList<Integer> clause = new LinkedList<>();
                        clause.add(hard_weight);  // 硬子句
                        clause.add(-var1);  // 添加第一个文字

                        // 创建第二个变量
                        var_name = "v_" + n + x + y;
                        int var = getVar(var_name);
                        clause.add(-var);  // 添加第二个文字
                        cnf.add(new LinkedList<>(clause));
                        hard_c_num++;
                    }
                }
            }
        }

        // 硬子句，如果逻辑单元i放在了坐标为(x,y)的物理单元上，则(x,y)上一定有东西
        for (int x=1; x<=row; x++) {
            for (int y = 1; y <= col; y++) {
                String var_name;
                var_name = "v_" + x + y;
                int var1 = getVar(var_name);
                for (int m = 1; m <= logic_unit_num; m++) {
                    // 创建新的子句
                    LinkedList<Integer> clause = new LinkedList<>();
                    clause.add(hard_weight);  // 硬子句

                    var_name = "v_" + m + x + y;
                    int var = getVar(var_name);

                    clause.add(-var);
                    clause.add(var1);
                    cnf.add(new LinkedList<>(clause));
                    hard_c_num++;
                }
            }
        }

        // 硬子句，如果坐标为(x,y)的物理单元上放了东西，那么一定是逻辑单元的其中一个
        for (int x=1; x<=row; x++) {
            for (int y = 1; y <= col; y++) {
                String var_name;
                var_name = "v_" + x + y;
                int var1 = getVar(var_name);
                LinkedList<Integer> clause = new LinkedList<>();
                clause.add(hard_weight);  // 硬子句
                clause.add(-var1);
                for (int m = 1; m <= logic_unit_num; m++) {
                    var_name = "v_" + m + x + y;
                    int var = getVar(var_name);
                    clause.add(var);
                }
                cnf.add(new LinkedList<>(clause));
                hard_c_num++;
            }
        }

        c_num = hard_c_num + soft_c_num;
        var_num = v - 1;

        write2File("src/main/resources/fpga_placing.wcnf");
    }

    /*
     * 输入varname，如果存在则返回真实的var编号（从1开始），否则新建后返回
     * */
    private int getVar(String var_name) {
        int var;
        if (vars.containsKey(var_name)) var = vars.get(var_name);
        else {
            var = v;
            vars.put(var_name, var);
            v++;
        }
        return var;
    }

    // 输入是v_xy
    private LinkedList<Integer> get_surround_vars(@NotNull String var_name) {
        LinkedList<Integer> surround_vars = new LinkedList<>();
        char base = '0';
        int x = var_name.charAt(2) - base;
        int y = var_name.charAt(3) - base;
        // 判断x位置
        if (x > 1) {
            surround_vars.add(getVar("v_" + (x-1) + y));
        }
        if (x < row) {
            surround_vars.add(getVar("v_" + (x+1) + y));
        }
        if (y > 1) {
            surround_vars.add(getVar("v_" + x + (y-1)));
        }
        if (y < col) {
            surround_vars.add(getVar("v_" + x + (y+1)));
        }
        return surround_vars;
    }

    // 写入文件
    private void write2File(String targetFilename) throws IOException {
        File file = new File(targetFilename);
        // 创建文件
        boolean create_res = file.createNewFile();
        if (!create_res) System.out.println("文件已存在。");
        // creates a FileWriter Object
        FileWriter writer = new FileWriter(file);
        // 向文件写入内容
        writer.write("p wcnf " + var_num + " " + c_num + " " + hard_weight + "\n");
        for (LinkedList<Integer> clause : cnf) {
            for (Integer item : clause) {
                writer.write(item + " ");
            }
            writer.write(0 + "\n");
        }
        writer.flush();
        writer.close();
    }

    public void printPlacingResult() {
        for (Map.Entry<String, Integer> entry : vars.entrySet()){
            // 找到"v_xy"
            //if (entry.getKey().length() == 4) {
                System.out.println(entry.getKey() + ":" + entry.getValue());
            //}
        }
    }

    public static void main(String[] args) throws IOException {
        FPGAPlacing fpgaPlacing = new FPGAPlacing();
        fpgaPlacing.mainProcess();
        fpgaPlacing.printPlacingResult();
    }
}
