import { Container, Box, Heading } from "@chakra-ui/react";

const Page = () => {
    return (
        <Container>
            <Box borderRadius="lg" bg="red" p={3} mb={6} align="center">
                Hello, I&apos;m a graduate computer science engineer
            </Box>
            <Box display={{md: "flex"}}>
                <Box flexGrow={1}>
                    <Heading as="h2" variant="page-title">
                        Paul Dam Quang Thanh
                    </Heading>
                    <p>
                        Software/DevOps/Cloud Engineer
                    </p>
                </Box>
            </Box>
        </Container>
    )
}

export default Page