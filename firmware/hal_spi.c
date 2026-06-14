#include "hal_spi.h"
#include <stdio.h>
#include <string.h>

static int spi_initialized = 0;

int HAL_SPI_Init(const char *host, int port) {
    // In the mock version, host/port are ignored
    spi_initialized = 1;
    printf("HAL_SPI_Init: Mock SPI initialized (host=%s, port=%d)\n", host, port);
    return 0;
}

int HAL_SPI_Transfer(const char *tx_buf, char *rx_buf, size_t len) {
    if (!spi_initialized) {
        snprintf(rx_buf, len, "ERROR: SPI not initialized");
        return -1;
    }

    if (strcmp(tx_buf, "READ_TEMP") == 0) {
        snprintf(rx_buf, len, "TEMP:25.13|CRC_OK");
    } else if (strcmp(tx_buf, "READ_FAULT") == 0) {
        snprintf(rx_buf, len, "TEMP:xx.xx|CRC_ERROR");
    } else {
        snprintf(rx_buf, len, "UNKNOWN_COMMAND");
    }

    return (int)strlen(rx_buf);
}

void HAL_SPI_DeInit(void) {
    spi_initialized = 0;
    printf("HAL_SPI_DeInit: Mock SPI deinitialized\n");
}
