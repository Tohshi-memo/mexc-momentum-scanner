# Decision Report

- generated_at: 2026-05-08T16:29:00.844185+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3803**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.37% / filled 20/20。**
- 全期間 MARKET基準: n=3803, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+1.37%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.37% | **+1.37%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.37% | **+1.37%** |
| ASK | 20/20 | 100.0% | +1.35% | **+1.35%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.96% | **+0.81%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.12% | **+0.79%** |
| LIMIT_5PCT | 2/20 | 10.0% | +0.95% | **+0.10%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.49% | **+0.22%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.29% | **+0.18%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.17% | **+0.06%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | -0.16% | **-0.10%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -0.95% | **-0.19%** |

## 2. $100 Live Portfolio

- 残高: **$98.82** / 初期 $100.00 (-1.18%)
- 確定トレード: 27件 (TP 7 / SL 18 / EXP 2)
- 最新: RKLBSTOCK/USDT:USDT SL_HIT PnL -2.88% 残高後 $98.82
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 192件 (Win 48 / Loss 64 / Flat 80) / skip 172件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FILECOIN/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-08T16:28:57.410347+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.23% price=79929.6
- Funnel: target 772 → liquid 178 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CHIP/USDT:USDT | +8.93% | $44,351,514.23 |
| PENGUIN/USDT:USDT | +5.80% | $1,021,213.82 |
| SATO/USDT:USDT | +4.89% | $7,886,412.35 |
| SKYAI/USDT:USDT | +3.44% | $17,956,438.08 |
| COLLECT/USDT:USDT | +2.85% | $1,364,277.45 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SATO/USDT:USDT | below_1h_threshold | +4.79% | +5.02% |
| SKYAI/USDT:USDT | below_1h_threshold | +3.51% | +3.74% |
| COLLECT/USDT:USDT | below_1h_threshold | +2.93% | +3.16% |
| JUP/USDT:USDT | below_1h_threshold | +2.82% | +3.05% |
| AKT/USDT:USDT | below_1h_threshold | +2.72% | +2.95% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
