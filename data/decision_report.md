# Decision Report

- generated_at: 2026-05-15T08:48:37.018373+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4328**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.84% / filled 20/20。**
- 全期間 MARKET基準: n=4328, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+2.84%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.84% | **+2.84%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.90% | **+2.90%** |
| MARKET | 20/20 | 100.0% | +2.84% | **+2.84%** |
| LIMIT_1PCT | 17/20 | 85.0% | +3.23% | **+2.74%** |
| LIMIT_2PCT | 14/20 | 70.0% | +3.30% | **+2.31%** |
| LIMIT_ATR | 13/20 | 65.0% | +3.05% | **+1.98%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +2.52% | **+1.26%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +1.57% | **+0.87%** |
| LIMIT_BB3S_LONG | 5/5 | 100.0% | +0.45% | **+0.45%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.00% | **+0.40%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +0.55% | **+0.36%** |

## 2. $100 Live Portfolio

- 残高: **$96.72** / 初期 $100.00 (-3.28%)
- 確定トレード: 45件 (TP 11 / SL 31 / EXP 3)
- 最新: SNDKSTOCK/USDT:USDT SL_HIT PnL -3.19% 残高後 $96.72
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.42** / 初期 $100.00 (+20.42%)
- 確定: 380件 (Win 97 / Loss 131 / Flat 152) / skip 509件
- 成長率目線: 平均log +0.000489 / 幾何平均 +0.049% per trade / maxDD +4.21%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BILL/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $120.42

## 4. Latest Market Context

- 更新: 2026-05-15T08:48:33.453000+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.22% price=80601.5
- Funnel: target 763 → liquid 161 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| GWEI/USDT:USDT | +25.85% | $1,420,578.04 |
| PEAQ/USDT:USDT | +25.00% | $3,766,801.50 |
| UP/USDT:USDT | +22.33% | $4,351,906.23 |
| BILL/USDT:USDT | +18.25% | $21,883,195.37 |
| TAC/USDT:USDT | +14.27% | $2,276,779.01 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| COLLECT/USDT:USDT | below_1h_threshold | +3.67% | +3.89% |
| BILL/USDT:USDT | below_1h_threshold | +3.46% | +3.69% |
| TAC/USDT:USDT | below_1h_threshold | +2.75% | +2.97% |
| UP/USDT:USDT | below_1h_threshold | +1.79% | +2.01% |
| BEAT/USDT:USDT | below_1h_threshold | +1.75% | +1.98% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
