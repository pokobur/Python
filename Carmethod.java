class Carmethod{
    
    int num;
    double gas;

    void setNumGas(int n, double g){ //戻り値がない場合　void
        
        num = n;
        gas = g;
        System.out.println("車のナンバーを" + num + "にガソリン量を" + gas + "にしました。");
    
    }
    void show(){
        System.out.println("車のナンバーは" + num + "です。");
        System.out.println("ガソリン量は" + gas + "です。");

    }
}
class Hikisu{
    public static void main (String[]args){

        Carmethod car1 = new Carmethod();

        int number = 1234;
        double gasoline = 20.5;

        car1.setNumGas(number,gasoline);
    }
}