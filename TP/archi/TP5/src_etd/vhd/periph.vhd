library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.numeric_std.all;
library work;
use work.CPU_pkg.all;

entity periph is
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
end periph ;

architecture Behavioral of periph  is

        component RAM8 is
                generic (
                        -- Memory initialization
                        FILE_NAME   : string := "none"
                );
                port (
                        -- Clock/Reset
                        clk  : in  std_logic ;
                        rst  : in  std_logic ;

                        -- Memory slave interface
                        ad  : in  std_logic_vector ( 15 downto 0 ) ;
                        do  : out std_logic_vector (  7 downto 0 ) ;
                        di  : in  std_logic_vector (  7 downto 0 ) ;
                        ceb : in  std_logic ;
                        web : in  std_logic
                );
        end component;

        signal sLED,timer,sTimerwidth,sTimerfreq: unsigned(7 downto 0 ):=(others => '0');
        signal mem_out: std_logic_vector(7 downto 0 ):=(others => '0');
        signal sCounter: unsigned(27 downto 0):=(others => '0');

begin
        iRAM : RAM8
                generic map (
                        -- Memory initialization
                        FILE_NAME   => "boot_defaut.mem"
                )
                port map (
                        -- Clock/Reset
                        clk => clk,
                        rst => '0', -- no memory reset

                        -- Memory slave interface
                        ad  => std_logic_vector(AD),
                        di  => std_logic_vector(DI),
                        do  => mem_out,
                        web => WEb,
                        ceb => CEb
                );

                ---------------------------------------------------
        Acces_lecture:
        process (AD,mem_out,switch,timer,pushbutton, CEb, WEb)
        begin
                if (not CEb and WEb and (AD(15) nor AD(13)) and (AD(14) nand AD(12)))= '1' then
                        if (AD(14) or AD(12)) = '0' then
                                case AD is
                                        when x"0010" => DO<=timer;  
                                        when x"0100" => DO<=x"0"&switch; 
                                        when x"0200" => DO<="00000"&pushbutton;  
                                        when others => DO<=(others =>'0');
                                end case;
                        else
                                DO <= unsigned(mem_out);
                        end if;
                else
                        DO<=(others =>'0');
                end if;
        end PROCESS Acces_lecture;

                ---------------------------------------------------
        Acces_ecriture:
        process (clk)
        begin
                if clk'event and clk='1' then -- clk à 80 MHz
                        if RST='1' then 
                                sLED<= (others => '0');
                                sTimerwidth <= X"11";
                                sTimerfreq <= X"26"; -- correspond à une fréquence de 2Hz

                        elsif  CEb = '0' and web='0' then
                                case AD is
                                        when x"0001" => sLED<=DI; 
                                        when x"0020" => 
                                                if (DI = X"00") then sTimerfreq<=x"01"; else sTimerfreq<=DI; end if;
                                        when x"0040" => sTimerwidth<=DI;
                                        when others => null;
                                end case;
                        end if;
                end if;
        end PROCESS acces_ecriture;
                ---------------------------------------------------

        LED<=sLED(7 downto 4) when pushbutton(0) = '1' else sLED(3 downto 0);

                ---------------------------------------------------
                i_timer: process (clk)
                begin
                        if clk'event and clk='1' then
                                if RST='1' or sCounter(27 downto 20)=sTimerfreq then 
                                        sCounter<= (others => '0');
                                else
                                        sCounter<= sCounter+1;					
                                end if;
                        end if;
                end PROCESS i_timer;

                ---------------------------------------------------
                -- actif à 0 durant sTimerwidth cycles en début de chaque boucle d'attente
                timer <= (others => '0') when sCounter < (X"00000"&sTimerwidth) else (others => '1');

end Behavioral;
