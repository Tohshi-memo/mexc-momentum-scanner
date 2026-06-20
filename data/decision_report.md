# Decision Report

- generated_at: 2026-06-20T16:07:39.377795+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7249**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.76% / filled 20/20。**
- 全期間 MARKET基準: n=7249, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.76%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.76% | **+0.76%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 17/20 | 85.0% | +2.17% | **+1.84%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.31% | **+1.18%** |
| ASK | 20/20 | 100.0% | +0.79% | **+0.79%** |
| MARKET | 20/20 | 100.0% | +0.76% | **+0.76%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.87% | **+0.65%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +0.60% | **+0.27%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.27% | **+0.12%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.22% | **+0.09%** |
| MARKET_LONG | 20/20 | 100.0% | +0.05% | **+0.05%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$101.96** / 初期 $100.00 (+1.96%)
- 確定トレード: 23件 (TP 9 / SL 14 / EXP 0)
- 最新: BLESS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.96
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$228.21** / 初期 $100.00 (+128.21%)
- 確定: 1978件 (Win 576 / Loss 644 / Flat 758) / skip 1832件
- 成長率目線: 平均log +0.000417 / 幾何平均 +0.042% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SLX/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $228.21

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 310件 (Win 89 / Loss 87 / Flat 134) / skip 350件
- 成長率目線: 平均log +0.000189 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-20T16:07:35.055889+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.20% price=63999.3
- Funnel: target 796 → liquid 141 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +2.92% | $50,070,477.77 |
| PIPPIN/USDT:USDT | +2.68% | $1,680,107.98 |
| BICO/USDT:USDT | +2.62% | $33,246,108.78 |
| SYN/USDT:USDT | +2.50% | $7,883,930.12 |
| GUA/USDT:USDT | +1.78% | $8,077,363.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BICO/USDT:USDT | below_1h_threshold | +3.42% | +3.62% |
| BTW/USDT:USDT | below_1h_threshold | +2.91% | +3.12% |
| PIPPIN/USDT:USDT | below_1h_threshold | +2.86% | +3.06% |
| SYN/USDT:USDT | below_1h_threshold | +2.80% | +3.00% |
| GUA/USDT:USDT | below_1h_threshold | +1.79% | +1.99% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
