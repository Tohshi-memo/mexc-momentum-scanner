# Decision Report

- generated_at: 2026-05-15T09:58:21.764398+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4330**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.54% / filled 20/20。**
- 全期間 MARKET基準: n=4330, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+2.54%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.54% | **+2.54%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.59% | **+2.59%** |
| MARKET | 20/20 | 100.0% | +2.54% | **+2.54%** |
| LIMIT_1PCT | 17/20 | 85.0% | +2.62% | **+2.23%** |
| LIMIT_2PCT | 14/20 | 70.0% | +2.56% | **+1.79%** |
| LIMIT_ATR | 13/20 | 65.0% | +2.25% | **+1.46%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +2.19% | **+1.20%** |
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +1.02% | **+1.02%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +1.41% | **+0.78%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.89% | **+0.40%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +0.61% | **+0.39%** |

## 2. $100 Live Portfolio

- 残高: **$96.72** / 初期 $100.00 (-3.28%)
- 確定トレード: 45件 (TP 11 / SL 31 / EXP 3)
- 最新: SNDKSTOCK/USDT:USDT SL_HIT PnL -3.19% 残高後 $96.72
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.42** / 初期 $100.00 (+20.42%)
- 確定: 382件 (Win 97 / Loss 131 / Flat 154) / skip 509件
- 成長率目線: 平均log +0.000486 / 幾何平均 +0.049% per trade / maxDD +4.21%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PEAQ/USDT:USDT `LIMIT_BB3S` EXPIRED account +0.00% 残高後 $120.42

## 4. Latest Market Context

- 更新: 2026-05-15T09:58:18.544330+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.23% price=80418.5
- Funnel: target 763 → liquid 162 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PEAQ/USDT:USDT | +26.87% | $3,943,911.49 |
| GWEI/USDT:USDT | +24.39% | $1,483,425.58 |
| UP/USDT:USDT | +23.27% | $4,606,555.66 |
| IRYS/USDT:USDT | +11.85% | $2,578,631.46 |
| BILL/USDT:USDT | +11.13% | $23,090,139.87 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IRYS/USDT:USDT | below_1h_threshold | +2.89% | +3.13% |
| GUA/USDT:USDT | below_1h_threshold | +2.89% | +3.12% |
| RIVER/USDT:USDT | below_1h_threshold | +2.50% | +2.73% |
| PEAQ/USDT:USDT | below_1h_threshold | +2.30% | +2.53% |
| CGPT/USDT:USDT | below_1h_threshold | +2.28% | +2.51% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
