output "target_group_arn" {
  value = aws_lb_target_group.ollama_tg.arn
}

output "alb_dns_name" {
  value = aws_lb.ollama_alb.dns_name
}