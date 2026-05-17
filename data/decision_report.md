# Decision Report

- generated_at: 2026-05-17T01:58:27.401383+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4374**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.86% / filled 20/20。**
- 全期間 MARKET基準: n=4374, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=+1.86%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.86% | **+1.86%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.86% | **+1.86%** |
| ASK | 20/20 | 100.0% | +1.47% | **+1.47%** |
| LIMIT_1PCT | 13/20 | 65.0% | +1.14% | **+0.74%** |
| LIMIT_ATR | 10/20 | 50.0% | +1.09% | **+0.55%** |
| LIMIT_3PCT | 9/20 | 45.0% | +1.07% | **+0.48%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +0.82% | **+0.45%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +0.69% | **+0.45%** |
| LIMIT_FIB1618_LONG | 7/20 | 35.0% | +1.12% | **+0.39%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.82% | **+0.33%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$98.17** / 初期 $100.00 (-1.83%)
- 確定トレード: 48件 (TP 13 / SL 32 / EXP 3)
- 最新: UB/USDT:USDT TP_HIT PnL +8.00% 残高後 $98.17
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$117.68** / 初期 $100.00 (+17.68%)
- 確定: 393件 (Win 97 / Loss 137 / Flat 159) / skip 542件
- 成長率目線: 平均log +0.000414 / 幾何平均 +0.041% per trade / maxDD +4.21%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CGPT/USDT:USDT `LIMIT_6PCT_LONG` EXPIRED account -0.27% 残高後 $117.68

## 4. Latest Market Context

- 更新: 2026-05-17T01:58:23.722741+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.18% price=77775.7
- Funnel: target 760 → liquid 130 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIA/USDT:USDT | +23.95% | $1,739,473.09 |
| LYN/USDT:USDT | +17.55% | $3,662,688.45 |
| UP/USDT:USDT | +11.15% | $1,668,715.13 |
| BSB/USDT:USDT | +8.90% | $3,857,676.90 |
| NMR/USDT:USDT | +8.58% | $1,203,869.34 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UP/USDT:USDT | below_1h_threshold | +3.04% | +3.22% |
| NMR/USDT:USDT | below_1h_threshold | +1.95% | +2.13% |
| MYX/USDT:USDT | below_1h_threshold | +0.81% | +0.99% |
| RUNE/USDT:USDT | below_1h_threshold | +0.64% | +0.81% |
| LYN/USDT:USDT | below_1h_threshold | +0.17% | +0.35% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
