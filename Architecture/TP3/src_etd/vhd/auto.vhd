library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity auto is
    port ( clk:     in  std_logic;
           reset:   in  std_logic;
           e:       in  std_logic;
           s:       out std_logic);
end auto;

architecture structural of auto is

  component reggene
    generic (
      n: positive :=8
      );
    port (
      d   : in unsigned(n-1 downto 0);
      clk : in std_logic ;
      rst : in  std_logic;
      q   : out unsigned(n-1 downto 0)
      );
  end component;

    signal Etat_courant, Etat_futur: unsigned(2 downto 0);

begin

  REG: reggene
  generic map (
    n => 3
  )
  port map (
    d => Etat_futur,
    clk => clk,
    rst => reset,
    q => Etat_courant
  );

  Etat_futur(0) <= (e and not Etat_courant(0)) or (e and not Etat_courant(1));
  Etat_futur(1) <= (Etat_courant(1) and not Etat_courant(0)) or (Etat_courant(2) and not e) or (Etat_courant(0) and not e);
  Etat_futur(2) <= Etat_courant(1) and Etat_courant(0) and e;

  s <= Etat_courant(2);

end structural;


-- architecture structural of auto is
--   component bascule_D is
--     port (
--       clk: in std_logic;
--       d: in std_logic;
--       q: out std_logic;
--       reset: in std_logic
--       );
--
--   end component;
--
--   -- $$$ etd_strip_begin
--   signal q0, q1, q2 : std_logic;
--   signal d0, d1, d2 : std_logic;
--   -- $$$ etd_strip_end
--
--   begin
--     -- $$$ etd_strip_begin
--     FD0: bascule_D
--       port map (
--         clk => clk,
--         reset => reset,
--         d => d0,
--         q => q0
--         );
--
--     FD1: bascule_D
--       port map (
--         clk => clk,
--         reset => reset,
--         d => d1,
--         q => q1
--         );
--
--     FD2: bascule_D
--       port map (
--         clk => clk,
--         reset => reset,
--         d => d2,
--         q => q2
--         );
--
--     d0 <= (e and not q0) or (e and not q1);
--     d1 <= (q1 and not q0) or (q2 and not e) or (q0 and not e);
--     d2 <= q1 and q0 and e;
--     s <= q2;
--     -- $$$ etd_strip_end
-- end structural;
