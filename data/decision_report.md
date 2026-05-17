# Decision Report

- generated_at: 2026-05-17T03:58:35.341242+00:00
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

- 更新: 2026-05-17T03:58:26.904873+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=77972.4
- Funnel: target 760 → liquid 129 → pre 50 → checked 50 → surge 4 → strict 3
- Surge前reject: below_1h_threshold=45, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIA/USDT:USDT | +42.76% | $3,536,800.42 |
| CGPT/USDT:USDT | +21.70% | $1,433,893.66 |
| BSB/USDT:USDT | +15.55% | $4,218,948.97 |
| LYN/USDT:USDT | +11.14% | $4,409,438.07 |
| UP/USDT:USDT | +7.67% | $1,698,970.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UB/USDT:USDT | below_relative_strength | +5.01% | +4.86% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +4.80% | +4.65% |
| PENDLE/USDT:USDT | below_1h_threshold | +4.52% | +4.37% |
| LAB/USDT:USDT | below_1h_threshold | +4.19% | +4.04% |
| ZBT/USDT:USDT | below_1h_threshold | +3.39% | +3.24% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
