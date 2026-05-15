# Decision Report

- generated_at: 2026-05-15T12:53:17.802105+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4337**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.19% / filled 20/20。**
- 全期間 MARKET基準: n=4337, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+2.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.19% | **+2.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.31% | **+2.31%** |
| MARKET | 20/20 | 100.0% | +2.19% | **+2.19%** |
| LIMIT_1PCT | 17/20 | 85.0% | +2.03% | **+1.73%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.64% | **+1.23%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.73% | **+1.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 13/20 | 65.0% | +1.59% | **+1.04%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +1.10% | **+0.60%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +1.20% | **+0.60%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_5PCT_LONG | 14/20 | 70.0% | +0.62% | **+0.43%** |

## 2. $100 Live Portfolio

- 残高: **$96.72** / 初期 $100.00 (-3.28%)
- 確定トレード: 45件 (TP 11 / SL 31 / EXP 3)
- 最新: SNDKSTOCK/USDT:USDT SL_HIT PnL -3.19% 残高後 $96.72
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$118.90** / 初期 $100.00 (+18.90%)
- 確定: 387件 (Win 97 / Loss 134 / Flat 156) / skip 511件
- 成長率目線: 平均log +0.000447 / 幾何平均 +0.045% per trade / maxDD +4.21%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IRYS/USDT:USDT `LIMIT_6PCT_LONG` EXPIRED account +0.00% 残高後 $118.90

## 4. Latest Market Context

- 更新: 2026-05-15T12:53:11.976258+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.24% price=80391.8
- Funnel: target 764 → liquid 167 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IRYS/USDT:USDT | +37.13% | $6,911,426.66 |
| GWEI/USDT:USDT | +24.27% | $1,754,615.40 |
| UP/USDT:USDT | +24.17% | $5,421,941.23 |
| PEAQ/USDT:USDT | +23.92% | $4,469,954.92 |
| GUA/USDT:USDT | +16.74% | $1,451,109.51 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XAN/USDT:USDT | below_1h_threshold | +4.22% | +4.46% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +2.55% | +2.78% |
| IRYS/USDT:USDT | below_1h_threshold | +1.56% | +1.80% |
| RAVE/USDT:USDT | below_1h_threshold | +0.92% | +1.15% |
| QNT/USDT:USDT | below_1h_threshold | +0.28% | +0.52% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
