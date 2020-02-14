--------------------------------------------------------------------------------
-- Description:   
-- 
-- Banc de test de la partie opérative
--------------------------------------------------------------------------------
LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
use IEEE.NUMERIC_STD.ALL;
 
 
ENTITY tb_PO IS
END tb_PO;
 
ARCHITECTURE behavior OF tb_PO IS 
     
    COMPONENT PO
    PORT(
         clk : IN  std_logic;
         reset : IN  std_logic;
         getA : IN  std_logic;
         getB : IN  std_logic;
         subBA : IN  std_logic;
         ldA : IN  std_logic;
         ldB : IN  std_logic;
         A0 : IN  unsigned(7 downto 0);
         B0 : IN  unsigned(7 downto 0);
         LT : OUT  std_logic;
         EQ : OUT  std_logic;
         Res : OUT  unsigned(7 downto 0)
        );
    END COMPONENT;
    

   --Inputs
   signal clk : std_logic := '0';
   signal reset : std_logic := '1';
   signal getA : std_logic := '0';
   signal getB : std_logic := '0';
   signal subBA : std_logic := '0';
   signal ldA : std_logic := '0';
   signal ldB : std_logic := '0';
   signal A0 : unsigned(7 downto 0) := X"30";
   signal B0 : unsigned(7 downto 0) := X"20";

 	--Outputs
   signal LT : std_logic;
   signal EQ : std_logic;
   signal Res : unsigned(7 downto 0);

   -- Clock period definitions
   constant clk_period : time := 8 ns;
 
BEGIN
 
	-- Instantiate the Unit Under Test (UUT)
   uut: PO PORT MAP (
          clk => clk,
          reset => reset,
          getA => getA,
          getB => getB,
          subBA => subBA,
          ldA => ldA,
          ldB => ldB,
          A0 => A0,
          B0 => B0,
          LT => LT,
          EQ => EQ,
          Res => Res
        );

   -- Clock process definitions
        process
        begin
                clk <= not clk;
                wait for clk_period/2 ;
        end process;

   -- Stimulus process
   stim_proc: process
   begin		
		reset <= '0';
		wait for clk_period/4;
		-- chargement du registre A
		lda <= '1' ;
		geta <= '1' ;
		
		-- ici A=0, B =0
		assert ( EQ = '1') report "==== ERREUR : Sortie EQ fausse" severity error;
		assert ( LT = '0') report "==== ERREUR : Sortie LT fausse" severity error;		
		assert ( RES = X"00" ) report "==== ERREUR : Sortie RES fausse" severity error;		
		
		wait for clk_period;
		-- chargement du registre B
		lda <= '0' ;
		geta <= '0' ;
		ldb <= '1' ;
		getb <= '1' ;
		
		-- ici A=x30, B =0
		assert ( EQ = '0') report "==== ERREUR : Sortie EQ fausse" severity error;
		assert ( LT = '0') report "==== ERREUR : Sortie LT fausse" severity error;		
		assert ( RES = X"00" ) report "==== ERREUR : Sortie RES fausse" severity error;		
				
		wait for clk_period;
		-- MAJ du registre A 
		lda <= '1';
		ldb <= '0' ;
		getb <= '0' ;
		
		-- ici A=x30, B = x20
		assert ( EQ = '0') report "==== ERREUR : Sortie EQ fausse" severity error;
		assert ( LT = '0') report "==== ERREUR : Sortie LT fausse" severity error;		
		assert ( RES = X"20" ) report "==== ERREUR : Sortie RES fausse" severity error;		
				
		wait for clk_period;
		-- MAJ du registre B
		lda <= '0';
		ldb <= '1' ;
		subba <= '1' ;
		
		-- ici A=x10, B = x20
		assert ( EQ = '0') report "==== ERREUR : Sortie EQ fausse" severity error;
		assert ( LT = '1') report "==== ERREUR : Sortie LT fausse" severity error;		
		assert ( RES = X"20" ) report "==== ERREUR : Sortie RES fausse" severity error;		
				
		wait for clk_period;
		-- MAJ du registre B
          -- ici A=x10, B = x10
          subba <= '0';
		assert ( EQ = '1') report "==== ERREUR : Sortie EQ fausse" severity error;
		assert ( LT = '0') report "==== ERREUR : Sortie LT fausse" severity error;		
		assert ( RES = X"10" ) report "==== ERREUR : Sortie RES fausse" severity error;		
				
		wait for clk_period;
		-- Tests finaux
		ldb <= '0' ;
		-- ici A=x10, B = x0
		assert ( EQ = '0') report "==== ERREUR : Sortie EQ fausse" severity error;
		assert ( LT = '0') report "==== ERREUR : Sortie LT fausse" severity error;		
		assert ( RES = X"00" ) report "==== ERREUR : Sortie RES fausse" severity error;		
		
		wait for clk_period;
		report "Simulation terminée" severity failure;
     
   end process;

END;
