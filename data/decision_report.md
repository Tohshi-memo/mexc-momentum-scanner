# Decision Report

- generated_at: 2026-06-22T12:28:48.051547+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7364**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.48% / filled 20/20。**
- 全期間 MARKET基準: n=7364, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.48%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.48% | **+0.48%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.49% | **+0.52%** |
| ASK | 20/20 | 100.0% | +0.52% | **+0.52%** |
| LIMIT_7PCT | 6/20 | 30.0% | +1.67% | **+0.50%** |
| LIMIT_BB3S | 6/18 | 33.3% | +1.48% | **+0.49%** |
| MARKET | 20/20 | 100.0% | +0.48% | **+0.48%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.44% | **+1.44%** |
| MARKET_LONG | 20/20 | 100.0% | +1.32% | **+1.32%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +0.68% | **+0.48%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.49% | **+0.32%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.36% | **+0.21%** |

## 2. $100 Live Portfolio

- 残高: **$102.97** / 初期 $100.00 (+2.97%)
- 確定トレード: 27件 (TP 11 / SL 16 / EXP 0)
- 最新: BEAT/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.97
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$229.45** / 初期 $100.00 (+129.45%)
- 確定: 2033件 (Win 599 / Loss 669 / Flat 765) / skip 1892件
- 成長率目線: 平均log +0.000409 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ALLO/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $229.45

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 312件 (Win 89 / Loss 87 / Flat 136) / skip 463件
- 成長率目線: 平均log +0.000188 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0521 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-22T12:28:43.337082+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.43% price=64900.0
- Funnel: target 806 → liquid 149 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +87.92% | $16,645,928.59 |
| CLO/USDT:USDT | +30.08% | $3,175,439.53 |
| LAYER/USDT:USDT | +25.12% | $2,959,580.68 |
| BTW/USDT:USDT | +18.58% | $41,322,606.09 |
| NAORIS/USDT:USDT | +14.37% | $5,721,957.35 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEL/USDT:USDT | below_1h_threshold | +3.19% | +2.76% |
| AMCSTOCK/USDT:USDT | below_1h_threshold | +2.96% | +2.53% |
| CLO/USDT:USDT | below_1h_threshold | +2.59% | +2.16% |
| UB/USDT:USDT | below_1h_threshold | +1.93% | +1.50% |
| TIA/USDT:USDT | below_1h_threshold | +1.69% | +1.27% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
