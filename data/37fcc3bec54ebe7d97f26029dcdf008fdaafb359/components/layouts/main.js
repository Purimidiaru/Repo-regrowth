import Head from "next/head"
import { Box, Container } from "@chakra-ui/react"

const Main = ({ children, router }) => {
    return (
        <Box as="main" pb={8}>
            <Head>
                <meta name="viewport" contents="device-width, initial-scale=1">
                    <title>
                        Paul Dam Quang Thanh - Homepage
                    </title>
                </meta>
            </Head>
            <Container maxW="container.md" pt={14}>
                {children}
            </Container>
        </Box>
    )
}

export default Main