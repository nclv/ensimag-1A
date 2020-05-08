#ifndef __CEP_PLATFORM_H__
#define __CEP_PLATFORM_H__ 

#if __ASSEMBLER__ == 0
#include <stdint.h>
#endif

// Peripherals Addresses
#define PERIPHS_BASE_ADDRESS            0x30000000
#define REG_LEDS_ADDR                   (PERIPHS_BASE_ADDRESS + 0x0)
#define REG_LEDS_CTRL                   (PERIPHS_BASE_ADDRESS + 0x4)
#define REG_PINS_ADDR                   (PERIPHS_BASE_ADDRESS + 0x8)
#define REG_PUSHBUTTON_CTL_ADDR         (PERIPHS_BASE_ADDRESS + 0xc)

// VRAM addresses
#define FRAME_BUFFER_CTRL_BASE_ADDRESS  0x70000000
#define FRAME_BUFFER_CTRL_MODE_REG      (FRAME_BUFFER_CTRL_BASE_ADDRESS + 0x0)
#define FRAME_BUFFER_CTRL_ADDR_REG      (FRAME_BUFFER_CTRL_BASE_ADDRESS + 0x4)
#define VRAM_OFFSET                     0x80000000

// PLIC registers addresses
#define PLIC_PENDING                    0x0c001000
#define PLIC_SOURCE                     0x0c000000
#define PLIC_ENABLE                     0x0c002000
#define PLIC_TARGET                     0x0c200000
#define PLIC_IRQ_CLAIM                  0x0c200004

// PLIC pushbutton irq
#define PLIC_IRQ_2                      0x2

// CLINT registers addresses
#define CLINT_MSIP                      0x02000000
#define CLINT_TIMER_CMP                 0x02004000
#define CLINT_TIMER_CMP_LO              0x02004000
#define CLINT_TIMER_CMP_HI              0x02004004
#define CLINT_TIMER                     0x0200bff8
#define CLINT_TIMER_LOW                 0x0200bff8
#define CLINT_TIMER_HI                  0x0200bffc

// Display: choose 720p by default
#if 1
#define DISPLAY_WIDTH                   1280
#define DISPLAY_HEIGHT                  720
#else
#define DISPLAY_WIDTH                   1920
#define DISPLAY_HEIGHT                  1080
#endif
#define DISPLAY_SIZE                    (DISPLAY_WIDTH * DISPLAY_HEIGHT)  // Taille en nombre de pixels
#define PIXEL_SIZE                      4

// Push button modes
#define REG_PUSHBUTTON_MODE_POLL        0x0
#define REG_PUSHBUTTON_MODE_INT         0x1

// HDMI Modes
#define HDMI_MODE_720p_60Hz             4
#define HDMI_MODE_1080p_60Hz            19
#define HDMI_MODE_1080p_30Hz_blk_0      32
#define HDMI_MODE_1080p_30Hz_blk_1      33
#define HDMI_MODE_1080p_30Hz_blk_2      34

// Timer options
#define TIMER_FREQ 10000000 // 10MHz
#define TIMER_RATIO 500  

// Bit in mstatus
#define MSTATUS_MIE  0x00000008
// Bit in mie/mip
#define IRQ_M_TMR    7
#define IRQ_M_EXT   11

#if __ASSEMBLER__ == 0
void timer_set(uint32_t period, uint32_t start_value);
void timer_wait(void);
void timer_set_and_wait(uint32_t period, uint32_t time);
void led_set(uint32_t value);
uint32_t push_button_get();
#endif

#endif // __CEP_PLATFORM_H__
