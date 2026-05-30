# Decision Report

- generated_at: 2026-05-30T00:05:36.404258+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5079**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.47% / filled 20/20。**
- 全期間 MARKET基準: n=5079, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+1.47%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.47% | **+1.47%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.48% | **+1.48%** |
| MARKET | 20/20 | 100.0% | +1.47% | **+1.47%** |
| LIMIT_BB3S | 9/18 | 50.0% | +1.43% | **+0.71%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.77% | **+0.61%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +0.56% | **+0.11%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +0.44% | **+0.11%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | -0.63% | **-0.28%** |
| ASK_LONG | 20/20 | 100.0% | -0.30% | **-0.30%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | -0.40% | **-0.34%** |

## 2. $100 Live Portfolio

- 残高: **$98.60** / 初期 $100.00 (-1.40%)
- 確定トレード: 74件 (TP 22 / SL 49 / EXP 3)
- 最新: LIT/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.60
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.68** / 初期 $100.00 (+25.68%)
- 確定: 740件 (Win 175 / Loss 226 / Flat 339) / skip 900件
- 成長率目線: 平均log +0.000309 / 幾何平均 +0.031% per trade / maxDD +4.72%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CTR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $125.68

## 4. Latest Market Context

- 更新: 2026-05-30T00:05:33.679957+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=73393.5
- Funnel: target 773 → liquid 147 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| XLM/USDT:USDT | +20.39% | $395,325,701.35 |
| OL/USDT:USDT | +15.70% | $1,450,730.49 |
| BASED/USDT:USDT | +14.59% | $2,445,390.01 |
| LAB/USDT:USDT | +13.59% | $128,196,427.73 |
| HBAR/USDT:USDT | +8.07% | $30,524,793.17 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +1.29% | +1.33% |
| HBAR/USDT:USDT | below_1h_threshold | +0.74% | +0.78% |
| QNTSTOCK/USDT:USDT | below_1h_threshold | +0.47% | +0.52% |
| BEAT/USDT:USDT | below_1h_threshold | +0.41% | +0.46% |
| BAT/USDT:USDT | below_1h_threshold | +0.33% | +0.38% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
