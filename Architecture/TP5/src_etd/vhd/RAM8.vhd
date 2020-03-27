library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

library xpm;
use xpm.vcomponents.all;


-- RAM 8 bits
entity RAM8 is
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
end entity;


architecture behavioral of RAM8 is
    -- Utils
    function log2ceil (x:positive) return natural is
        variable i : natural := x-1 ;
        variable n : natural := 0 ;
    begin
        while i > 0 loop
            n := n + 1; i := i / 2;
        end loop;
        return n;
    end function;

    -- Constants
    constant MEMORY_SIZE : positive := 8 * 1024 ; -- 8 Ko
    constant N_BIT : natural := log2ceil( MEMORY_SIZE ) ;

    -- Signals
    signal s_we           : std_logic_vector (  0 downto 0 ) ;
    signal s_internal_ad  : std_logic_vector ( 12 downto 0 ) ;
    signal s_internal_en  : std_logic ;
    signal s_internal_clk : std_logic ;

begin


    -- Address translation
    process (ceb, ad)
        variable en_tmp : std_logic;
        variable en_0   : std_logic; -- Enable intern addr from 0x0000 to 0x0FFF (=> extern addr 0x1000 to 0x1FFF)
        variable en_1   : std_logic; -- Enable intern addr from 0x1000 to 0x1FFF (=> extern addr 0x4000 to 0x4FFF)
    begin
        en_tmp := not(ceb or ad(15) or ad(13));
        en_0 := en_tmp and not ad(14) and     ad(12);
        en_1 := en_tmp and     ad(14) and not ad(12);
    
        s_internal_en <= en_0 or en_1;
        s_internal_ad <= en_1 & ad(11 downto 0) ;
    end process;

    -- Write enable
    s_we(0) <= not web;

    s_internal_clk <= not clk ;

    -- Memory
    XPM_RAM : XPM_MEMORY_SPRAM
        generic map (
            -- Memory configuration
            MEMORY_SIZE         => MEMORY_SIZE * 8, -- byte size -> bit size
            MEMORY_PRIMITIVE    => "block",
            MEMORY_OPTIMIZATION => "true",
            MEMORY_INIT_FILE    => FILE_NAME,
            USE_MEM_INIT        => 1,
            ECC_MODE            => "no_ecc",

            -- Ports configuration
            ADDR_WIDTH_A        => N_BIT,
            BYTE_WRITE_WIDTH_A  => 8,
            WRITE_DATA_WIDTH_A  => 8,
            READ_DATA_WIDTH_A   => 8,
            WRITE_MODE_A        => "read_first",
            READ_LATENCY_A      => 1
        )
        port map (
            -- Clock/Reset
            clkA   => s_internal_clk,
            rstA   => rst,
            sleep  => '0',

            -- Memory slave interface
            addrA  => s_internal_ad ,
            enA    => s_internal_en,
            weA    => s_we,
            dinA   => di, 
            doutA  => do,
            regceA => '0',

            -- Error injection : off
            sbiterrA       => open,
            dbiterrA       => open,
            injectsbiterrA => '0',
            injectdbiterrA => '0'
        );


end architecture;
