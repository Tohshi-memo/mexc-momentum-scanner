# Decision Report

- generated_at: 2026-06-18T07:55:54.444126+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7022**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.39% / filled 20/20。**
- 全期間 MARKET基準: n=7022, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.39%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.39% | **+1.39%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.39% | **+1.39%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.79% | **+0.98%** |
| LIMIT_10PCT | 3/20 | 15.0% | +6.30% | **+0.95%** |
| LIMIT_9PCT | 3/20 | 15.0% | +5.72% | **+0.86%** |
| ASK | 20/20 | 100.0% | +0.66% | **+0.66%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.08% | **+0.07%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | -0.18% | **-0.04%** |
| MARKET_LONG | 20/20 | 100.0% | -0.20% | **-0.20%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | -0.75% | **-0.22%** |

## 2. $100 Live Portfolio

- 残高: **$100.97** / 初期 $100.00 (+0.97%)
- 確定トレード: 13件 (TP 5 / SL 8 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.97
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$215.05** / 初期 $100.00 (+115.05%)
- 確定: 1868件 (Win 523 / Loss 594 / Flat 751) / skip 1715件
- 成長率目線: 平均log +0.000410 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GUA/USDT:USDT `MARKET_LONG` TP_HIT account +1.00% 残高後 $215.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.77** / 初期 $100.00 (+5.77%)
- 確定: 295件 (Win 83 / Loss 80 / Flat 132) / skip 138件
- 成長率目線: 平均log +0.000190 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0644 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: GUA/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $105.77

## 5. Latest Market Context

- 更新: 2026-06-18T07:55:42.459501+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.55% price=64403.0
- Funnel: target 793 → liquid 175 → pre 50 → checked 50 → surge 5 → strict 2
- Surge前reject: below_1h_threshold=44, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.1 >= 65=1, 4h RSI 66.8 >= 65=1, 4h RSI 85.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +112.49% | $40,632,125.34 |
| O/USDT:USDT | +68.24% | $3,705,552.21 |
| SYN/USDT:USDT | +62.94% | $5,466,767.95 |
| HOME/USDT:USDT | +34.80% | $2,166,034.87 |
| H/USDT:USDT | +26.48% | $32,663,003.19 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ALLO/USDT:USDT | below_relative_strength | +5.54% | +4.99% |
| FOLKS/USDT:USDT | below_1h_threshold | +2.90% | +2.35% |
| RUNE/USDT:USDT | below_1h_threshold | +2.50% | +1.95% |
| O/USDT:USDT | below_1h_threshold | +2.45% | +1.90% |
| LAB/USDT:USDT | below_1h_threshold | +2.31% | +1.76% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
