#include "hal_spi.h"
#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[])   // <-- Entry point for Windows/MSVC
{
    char rx_buf[64];

    HAL_SPI_Init("127.0.0.1", 65432); //Initialize mock SPI (host/port are ignored)

    const char *cmd = (argc > 1) ? argv[1] : "READ_TEMP";
    printf("Sending command to SPI: %s\n", cmd);

    HAL_SPI_Transfer(cmd, rx_buf, sizeof(rx_buf));
    printf("Received from SPI: %s\n", rx_buf);

    if (strstr(rx_buf, "CRC_ERROR"))
        printf("Sensor CRC error detected!\n");
    else
        printf("Valid temperature frame: %s\n", rx_buf);

    HAL_SPI_DeInit();
    return 0;
}
