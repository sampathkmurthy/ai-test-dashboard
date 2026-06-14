#ifndef HAL_SPI_H
#define HAL_SPI_H

#include <stddef.h>

// Initialize the mock SPI interface
int HAL_SPI_Init(const char *host, int port);

// Transfer data over mock SPI
int HAL_SPI_Transfer(const char *tx_buf, char *rx_buf, size_t len);

// Deinitialize the mock SPI interface
void HAL_SPI_DeInit(void);

#endif // HAL_SPI_H

