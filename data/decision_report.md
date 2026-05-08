# Decision Report

- generated_at: 2026-05-08T10:47:36.355156+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3772**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.54% / filled 20/20。**
- 全期間 MARKET基準: n=3772, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=+2.54%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.54% | **+2.54%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.54% | **+2.54%** |
| ASK | 20/20 | 100.0% | +2.44% | **+2.44%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.88% | **+1.60%** |
| LIMIT_2PCT | 13/20 | 65.0% | +0.79% | **+0.51%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +1.69% | **+0.25%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/6 | 50.0% | +0.21% | **+0.10%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | -0.17% | **-0.14%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | -0.89% | **-0.18%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -1.03% | **-0.21%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | -0.31% | **-0.25%** |

## 2. $100 Live Portfolio

- 残高: **$99.32** / 初期 $100.00 (-0.68%)
- 確定トレード: 26件 (TP 7 / SL 17 / EXP 2)
- 最新: UB/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.32
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 191件 (Win 48 / Loss 64 / Flat 79) / skip 142件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PHAROS/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-08T10:47:33.289895+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.32% price=80084.2
- Funnel: target 773 → liquid 183 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=1, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PHAROS/USDT:USDT | +44.82% | $6,992,081.55 |
| PLAY/USDT:USDT | +42.71% | $9,583,525.95 |
| BSB/USDT:USDT | +40.03% | $9,441,696.56 |
| STRK/USDT:USDT | +33.15% | $19,001,831.19 |
| AGT/USDT:USDT | +25.33% | $5,563,769.43 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PHAROS/USDT:USDT | below_relative_strength | +5.03% | +4.71% |
| CHIP/USDT:USDT | below_1h_threshold | +4.96% | +4.63% |
| PLAY/USDT:USDT | below_1h_threshold | +4.90% | +4.57% |
| STRK/USDT:USDT | below_1h_threshold | +3.19% | +2.87% |
| ONDO/USDT:USDT | below_1h_threshold | +2.56% | +2.24% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
