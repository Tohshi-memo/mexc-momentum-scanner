# Decision Report

- generated_at: 2026-05-08T18:17:31.469440+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3815**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.98% / filled 20/20。**
- 全期間 MARKET基準: n=3815, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=+0.98%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.98% | **+0.98%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.98% | **+0.98%** |
| ASK | 20/20 | 100.0% | +0.97% | **+0.97%** |
| LIMIT_BB3S | 4/16 | 25.0% | +1.91% | **+0.48%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.48% | **+0.44%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.74% | **+0.37%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.49% | **+0.24%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.00% | **+0.00%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | -0.10% | **-0.05%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -1.17% | **-0.12%** |

## 2. $100 Live Portfolio

- 残高: **$98.33** / 初期 $100.00 (-1.67%)
- 確定トレード: 28件 (TP 7 / SL 19 / EXP 2)
- 最新: IO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.33
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 192件 (Win 48 / Loss 64 / Flat 80) / skip 184件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FILECOIN/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-08T18:17:28.281471+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.21% price=80187.1
- Funnel: target 768 → liquid 180 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CHIP/USDT:USDT | +11.08% | $50,610,413.92 |
| COLLECT/USDT:USDT | +9.97% | $1,657,639.78 |
| AKT/USDT:USDT | +8.64% | $1,099,035.73 |
| OP/USDT:USDT | +7.96% | $19,648,901.98 |
| IO/USDT:USDT | +6.78% | $1,345,610.52 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CHIP/USDT:USDT | below_1h_threshold | +3.79% | +3.58% |
| B3/USDT:USDT | below_1h_threshold | +3.20% | +3.00% |
| OP/USDT:USDT | below_1h_threshold | +3.01% | +2.81% |
| SNX/USDT:USDT | below_1h_threshold | +2.06% | +1.86% |
| PYTH/USDT:USDT | below_1h_threshold | +1.79% | +1.58% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
