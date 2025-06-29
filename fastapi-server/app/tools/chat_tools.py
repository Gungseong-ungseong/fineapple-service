from mcp.server.fastmcp import FastMCP
from typing import Optional
from dotenv import load_dotenv
from app.models.chat import ChatRequest, ChatState
from app.services.LLMService import LLMService
from app.utills.crc_chain import crc_chain, memory
from app.nodes.cart import cart_node
from app.nodes.delivery import delivery_node, delivery_node_rag
from app.nodes.refund import refund_node
from app.nodes.recommendation import recommendation_node
from app.nodes.product_inquiry import product_inquiry_node
from app.nodes.event import event_node
from app.nodes.fallback_node import fallback_node
from app.nodes.payment import payment_node
from app.nodes.user_info import user_info_node

load_dotenv()

mcp = FastMCP("SolarCustomerSupport")

llm_service = LLMService()

@mcp.tool()
async def class_intent_tool(question: str) -> str:
    """
    사용자의 의도를 LLM이 1차로 분류하는 툴
    """
    return await llm_service.classify_intent(question)

@mcp.tool()
async def retrieve_relevant_docs(state: ChatState) -> str:
    """
    과거이력과 crc체인을 통해 문서를 검색해서 하나의 응답을 반환하는 툴
    """
    chat_history = []
    for i in range(len(state.history) - 1):
        msg = state.history[i]
        next_msg = state.history[i + 1]
        if msg["role"] == "user" and next_msg["role"] == "assistant":
            chat_history.append((msg["content"], next_msg["content"]))

    result = await crc_chain.ainvoke({
        "question": state.question,
        "chat_history": chat_history
    })

    answer = result.get("answer", "관련 문서를 찾을 수 없습니다.")
    return answer


@mcp.tool()
async def generate_response_tool(state: ChatState) -> str:
    """
    응답 생성 툴
    """
    return await llm_service.generate_response(state)

@mcp.tool()
async def process_chat_tool(question: str, user_id: Optional[int] = None) -> dict:
    """
    프로세스 채팅 흐름 테스트용 툴
    """
    from app.controllers.chat_controller import ChatController
    from app.models.chat import ChatRequest

    controller = ChatController()
    request = ChatRequest(query=question, user_id=user_id)
    response = await controller.process_chat(request)
    return response.model_dump()


@mcp.tool()
async def cart_tool(state: ChatState) -> ChatState:
    return await cart_node(state)

@mcp.tool()
async def delivery_tool(state: ChatState) -> ChatState:
    return await delivery_node_rag(state)

@mcp.tool()
async def delivery_tool_rag(state: ChatState) -> ChatState:
    return await delivery_node(state)

@mcp.tool()
async def event_tool(state: ChatState) -> ChatState:
    return await event_node(state)

@mcp.tool()
async def refund_tool(state: ChatState) -> ChatState:
    return await refund_node(state)

@mcp.tool()
async def recommendation_tool(state: ChatState) -> ChatState:
    return await recommendation_node(state)

@mcp.tool()
async def product_inquiry_tool(state: ChatState) -> ChatState:
    return await product_inquiry_node(state)

@mcp.tool()
async def fallback_tool(state: ChatState) -> ChatState:
    return await fallback_node(state)

@mcp.tool()
async def payment_tool(state: ChatState) -> ChatState:
    return await payment_node(state)

@mcp.tool()
async def user_info_tool(state: ChatState) -> ChatState:
    return await user_info_node(state)