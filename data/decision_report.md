# Decision Report

- generated_at: 2026-05-31T00:34:43.585264+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5155**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.79% / filled 20/20。**
- 全期間 MARKET基準: n=5155, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.79%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.79% | **+0.79%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | +4.78% | **+0.96%** |
| ASK | 20/20 | 100.0% | +0.93% | **+0.93%** |
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| MARKET | 20/20 | 100.0% | +0.79% | **+0.79%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +4.11% | **+0.41%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 16/20 | 80.0% | +1.46% | **+1.16%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.98% | **+0.83%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.85% | **+0.76%** |
| ASK_LONG | 20/20 | 100.0% | +0.55% | **+0.55%** |
| MARKET_LONG | 20/20 | 100.0% | +0.39% | **+0.39%** |

## 2. $100 Live Portfolio

- 残高: **$98.10** / 初期 $100.00 (-1.90%)
- 確定トレード: 78件 (TP 23 / SL 52 / EXP 3)
- 最新: NFP/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$123.19** / 初期 $100.00 (+23.19%)
- 確定: 793件 (Win 183 / Loss 242 / Flat 368) / skip 923件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +6.10%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PORTAL/USDT:USDT `LIMIT_BB3S` EXPIRED account +0.00% 残高後 $123.19

## 4. Latest Market Context

- 更新: 2026-05-31T00:34:41.034139+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.17% price=73980.5
- Funnel: target 773 → liquid 121 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +34.36% | $6,391,324.43 |
| TA/USDT:USDT | +20.63% | $2,020,044.00 |
| ONDO/USDT:USDT | +12.55% | $33,510,490.20 |
| BIANRENSHENG/USDT:USDT | +12.27% | $1,345,884.94 |
| STG/USDT:USDT | +9.67% | $3,416,666.97 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AXS/USDT:USDT | below_1h_threshold | +4.11% | +3.95% |
| ASTER/USDT:USDT | below_1h_threshold | +3.92% | +3.75% |
| ONDO/USDT:USDT | below_1h_threshold | +2.69% | +2.52% |
| PENDLE/USDT:USDT | below_1h_threshold | +2.25% | +2.08% |
| LAB/USDT:USDT | below_1h_threshold | +1.85% | +1.68% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
