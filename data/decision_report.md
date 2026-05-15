# Decision Report

- generated_at: 2026-05-15T07:53:10.732736+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4326**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.44% / filled 20/20。**
- 全期間 MARKET基準: n=4326, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=+3.44%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.44% | **+3.44%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +3.50% | **+3.50%** |
| MARKET | 20/20 | 100.0% | +3.44% | **+3.44%** |
| LIMIT_1PCT | 16/20 | 80.0% | +3.62% | **+2.89%** |
| LIMIT_2PCT | 13/20 | 65.0% | +3.71% | **+2.41%** |
| LIMIT_ATR | 11/20 | 55.0% | +3.02% | **+1.66%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +1.36% | **+0.75%** |
| LIMIT_BB3S_LONG | 5/5 | 100.0% | +0.45% | **+0.45%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.89% | **+0.40%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +0.42% | **+0.25%** |
| LIMIT_FIB1272_LONG | 14/20 | 70.0% | +0.33% | **+0.23%** |

## 2. $100 Live Portfolio

- 残高: **$96.72** / 初期 $100.00 (-3.28%)
- 確定トレード: 45件 (TP 11 / SL 31 / EXP 3)
- 最新: SNDKSTOCK/USDT:USDT SL_HIT PnL -3.19% 残高後 $96.72
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.42** / 初期 $100.00 (+20.42%)
- 確定: 378件 (Win 97 / Loss 131 / Flat 150) / skip 509件
- 成長率目線: 平均log +0.000491 / 幾何平均 +0.049% per trade / maxDD +4.21%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SNDKSTOCK/USDT:USDT `LIMIT_BB3S` EXPIRED account +0.00% 残高後 $120.42

## 4. Latest Market Context

- 更新: 2026-05-15T07:53:07.219655+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.36% price=80830.3
- Funnel: target 763 → liquid 162 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PEAQ/USDT:USDT | +27.20% | $3,669,953.87 |
| GWEI/USDT:USDT | +25.77% | $1,370,443.00 |
| UP/USDT:USDT | +21.79% | $4,278,290.94 |
| FIGSTOCK/USDT:USDT | +14.30% | $3,207,845.75 |
| BILL/USDT:USDT | +14.17% | $20,455,613.22 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +4.40% | +4.04% |
| CHIP/USDT:USDT | below_1h_threshold | +2.92% | +2.56% |
| STAR/USDT:USDT | below_1h_threshold | +2.84% | +2.48% |
| PENDLE/USDT:USDT | below_1h_threshold | +2.51% | +2.15% |
| RAVE/USDT:USDT | below_1h_threshold | +2.21% | +1.85% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
