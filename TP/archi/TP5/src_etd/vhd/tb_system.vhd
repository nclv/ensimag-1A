
LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
USE ieee.numeric_std.ALL;
LIBRARY UNISIM;
USE UNISIM.Vcomponents.ALL;


ENTITY tb_system IS
END tb_system;


ARCHITECTURE behavioral OF tb_system IS 

        COMPONENT system
        port ( clk:     in  std_logic;
               rst: in std_logic; 
               switch : in unsigned(3 downto 0);	
               pushbutton: in unsigned(2 downto 0);	
               LED : out unsigned(3 downto 0));
        end component;

       SIGNAL RST	:	STD_LOGIC;
       signal clk:     std_logic := '0';
       SIGNAL LED	:	unsigned (3 DOWNTO 0);
       SIGNAL switch	:	unsigned (3 DOWNTO 0);
       SIGNAL pb	:	unsigned (2 DOWNTO 0);

BEGIN
        UUT: system PORT MAP( CLK => CLK,
                              RST => RST, 
                              switch => switch, 
                              pushbutton => pb,
                              LED => LED);

        -- définition de l'horloge à 125MHz
        process
        begin
                clk <= not clk;
                wait for 4 ns;
        end process;

   -- définition du reset

        tb : PROCESS
        BEGIN
                pb <= "000";
                switch <= X"C";

                rst <= '1';
                WAIT for 20 ns; 	
                rst <= '0';
                WAIT for 500 ns; 	
                switch <= X"3";
                wait;
        END PROCESS;

END;
