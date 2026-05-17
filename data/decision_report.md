# Decision Report

- generated_at: 2026-05-17T03:53:43.677291+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4379**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.77% / filled 20/20。**
- 全期間 MARKET基準: n=4379, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.77%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.77% | **+0.77%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.77% | **+0.77%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.81% | **+0.57%** |
| ASK | 20/20 | 100.0% | +0.37% | **+0.37%** |
| LIMIT_3PCT | 12/20 | 60.0% | +0.56% | **+0.34%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.95% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +1.51% | **+0.38%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +0.00% | **+0.00%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | -0.06% | **-0.02%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | -0.11% | **-0.07%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | -0.58% | **-0.26%** |

## 2. $100 Live Portfolio

- 残高: **$97.68** / 初期 $100.00 (-2.32%)
- 確定トレード: 49件 (TP 13 / SL 33 / EXP 3)
- 最新: CGPT/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.68
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$117.68** / 初期 $100.00 (+17.68%)
- 確定: 393件 (Win 97 / Loss 137 / Flat 159) / skip 547件
- 成長率目線: 平均log +0.000414 / 幾何平均 +0.041% per trade / maxDD +4.21%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CGPT/USDT:USDT `LIMIT_6PCT_LONG` EXPIRED account -0.27% 残高後 $117.68

## 4. Latest Market Context

- 更新: 2026-05-17T03:53:30.459930+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.17% price=77991.1
- Funnel: target 760 → liquid 129 → pre 50 → checked 50 → surge 6 → strict 5
- Surge前reject: below_1h_threshold=44, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIA/USDT:USDT | +45.77% | $3,450,476.92 |
| CGPT/USDT:USDT | +22.09% | $1,422,581.82 |
| BSB/USDT:USDT | +15.42% | $4,207,363.59 |
| LYN/USDT:USDT | +9.15% | $4,402,934.79 |
| UP/USDT:USDT | +8.54% | $1,697,227.39 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PENDLE/USDT:USDT | below_1h_threshold | +4.64% | +4.47% |
| LAB/USDT:USDT | below_1h_threshold | +4.22% | +4.04% |
| SAGA/USDT:USDT | below_1h_threshold | +3.94% | +3.76% |
| ZBT/USDT:USDT | below_1h_threshold | +3.01% | +2.84% |
| HYPE/USDT:USDT | below_1h_threshold | +2.70% | +2.53% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
