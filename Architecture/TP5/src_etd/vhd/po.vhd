library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;
library work;
use work.CPU_pkg.all;

entity PO is
        port ( clk:     in  std_logic;
               ctrl:   in  CPU_CTRL;
               CR : out CPU_COMPTE_RENDU;
               mem_addr    : out  w16;
               mem_dataout : out  w8;
               mem_datain  : in   w8
);

end PO;

architecture RTL of PO is
        signal x,y,res,resALU : w8;
        signal PC_q,PC_d,AD_q,AD_d: w16 := (others => '0');
        signal R0_q,R0_d,R1_q,R1_d,R2_q,R2_d,R3_q,R3_d,IR_q,IR_d: w8:= (others => '0');
        signal z_d,z_q: std_logic;

begin
        synchrone : process (CLK)
        begin
                if clk'event and clk='1' then 
                        if ctrl.rst then 
                                PC_q <= x"4000";
                                R0_q <= (others=>'0');
                                R1_q <= (others=>'0');
                                R2_q <= (others=>'0');
                                R3_q <= (others=>'0');
                                AD_q <= (others=>'0');
                                IR_q <= (others=>'0');
                                z_q <= '0';
                        else
                                PC_q <= PC_d;
                                R0_q <= R0_d;
                                R1_q <= R1_d;
                                R2_q <= R2_d;
                                R3_q <= R3_d;
                                AD_q <= AD_d;
                                IR_q <= IR_d;
                                z_q <= z_d;
                        end if;
                end if;
        end process synchrone;

        -- sélection des opérandes
        with ctrl.selA select x <= R0_q when "00", R1_q when "01", R2_q when "10", R3_q when others;
        with ctrl.selB select y <= R0_q when "00", R1_q when "01", R2_q when "10", R3_q when others;

        -- Description de l'UAL
        with ctrl.op select resALU <=
        x or y  when "000",
        x xor y  when "001",
        x and y  when "010",
        not x  when "011",
        x + y  when "100",
        x - y  when "101",
        (x(6 downto 0) & '0')  when "110",
        ('0' & x(7 downto 1))  when "111",
        (others => '0') when others;

        -- Description du compte-rendu
        z_d <= z_q when ctrl.ldz = false else '1' when resALU = 0 else '0';
        CR.z <= z_q;
        CR.IR <= IR_q;

        -- Sélection de res
        res <= resALU when ctrl.selR = from_ALU else mem_datain;

        -- mise a jour des registres par leur nouvelle valeur selon les LD
        PC_d <= PC_q when ctrl.ldPC = false else               
                PC_q + 1 when ctrl.selPC = from_INCR else AD_q ;
        AD_d(15 downto 8) <= mem_datain when ctrl.ldADH else AD_q(15 downto 8) ;
        AD_d(7 downto 0) <= mem_datain when ctrl.ldADL else AD_q(7 downto 0) ;
        IR_d  <= mem_datain when ctrl.ldIR else IR_q;
        R0_d  <= res when ctrl.ldR0 else R0_q;
        R1_d  <= res when ctrl.ldR1 else R1_q;
        R2_d  <= res when ctrl.ldR2 else R2_q;
        R3_d  <= res when ctrl.ldR3 else R3_q;

        -- Sortie vers la mémoire 
        mem_addr <= AD_q when from_AD = ctrl.selAD  else PC_q;
        mem_dataout <= x;
end RTL;
