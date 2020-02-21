library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;
library work;
use work.CPU_pkg.all;
Library UNISIM;
use UNISIM.vcomponents.all;

entity system is
        port ( clk:     in  std_logic;
               rst: in std_logic; 
               switch : in unsigned(3 downto 0);	
               pushbutton: in unsigned(2 downto 0);	
               led : out unsigned(3 downto 0)
       );
end system;

architecture struct of system is

        component PO is
                port ( clk:     in  std_logic;
                       ctrl:   in  CPU_CTRL;
                       CR : out CPU_COMPTE_RENDU;
                       mem_addr    : out  w16;
                       mem_dataout : out  w8;
                       mem_datain  : in   w8
        );
        end component;

        component PC is
                Port ( CLK : in  STD_LOGIC;
                       RESET : in  STD_LOGIC;
                       ctrl:   out  CPU_CTRL;
                       CR : in CPU_COMPTE_RENDU;
                       WEb : out  STD_LOGIC;
                       CEb : out  STD_LOGIC
               );
        end component;

        component periph is
        Port ( clk : in std_logic;
               WEb : in std_logic;
               CEb : in std_logic;
               rst: in std_logic; 
               AD : in w16;
               DI : in w8;
               switch : in unsigned(3 downto 0);	
               pushbutton: in unsigned(2 downto 0);	
               LED : out unsigned(3 downto 0);
               DO : out w8);
        end component;

        signal ctrl : CPU_ctrl;
        signal CR : CPU_COMPTE_RENDU;
        signal we,ce,clk80,locked,reset,clk_fb: std_logic;
        signal D_to_mem, D_from_mem : w8;
        signal AD : w16;

begin


MMCME2_BASE_inst : MMCME2_BASE
generic map (
    CLKFBOUT_MULT_F => 8.0, -- facteur multiplicatif horloge
CLKIN1_PERIOD => 8.0, -- horloge entrante à 125MHz
CLKOUT0_DIVIDE_F => 12.50, --facteur de division horloge
    REF_JITTER1 => 0.010)
  port map (
     CLKOUT0 => clk80,
     LOCKED => locked,
     CLKFBOUT => clk_fb,
     CLKFBIN => clk_fb,
     CLKIN1 => clk,
     PWRDWN => '0',
     RST => '0'
  );

    reset <= rst or not locked;

        i_PO : PO port map ( clk => clk80,
                             ctrl => ctrl,
                             CR => CR,
                             mem_addr => AD,
                             mem_dataout => D_to_mem,
                             mem_datain => D_from_mem);

        i_PC : PC port map ( CLK => clk80,
                             RESET => reset,
                             ctrl => ctrl,
                             CR => CR,
                             WEb => WE,
                             CEb => CE);

        i_periph : periph port map ( clk => clk80 ,
                                     WEb => we,
                                     CEb => ce,
                                     rst=> reset,
                                     AD => AD,
                                     DI => D_to_mem,
                                     switch => switch,
                                     pushbutton=> pushbutton,
                                     LED => LED,
                                     DO => D_from_mem);

end struct;
