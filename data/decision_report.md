# Decision Report

- generated_at: 2026-06-12T19:42:48.113505+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6541**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +4.22% / filled 20/20。**
- 全期間 MARKET基準: n=6541, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+4.22%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +4.22% | **+4.22%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +4.22% | **+4.22%** |
| ASK | 20/20 | 100.0% | +3.35% | **+3.35%** |
| LIMIT_1PCT | 15/20 | 75.0% | +3.27% | **+2.45%** |
| LIMIT_2PCT | 12/20 | 60.0% | +3.68% | **+2.21%** |
| LIMIT_ATR | 8/20 | 40.0% | +4.40% | **+1.76%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +4.53% | **+1.13%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +2.69% | **+0.54%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.40% | **+0.42%** |
| LIMIT_8PCT_LONG | 13/20 | 65.0% | -0.31% | **-0.20%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | -1.76% | **-1.06%** |

## 2. $100 Live Portfolio

- 残高: **$97.07** / 初期 $100.00 (-2.93%)
- 確定トレード: 25件 (TP 6 / SL 18 / EXP 1)
- 最新: SPCXSTOCK/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.07
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$164.64** / 初期 $100.00 (+64.64%)
- 確定: 1414件 (Win 388 / Loss 461 / Flat 565) / skip 1688件
- 成長率目線: 平均log +0.000353 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SPCXSTOCK/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $164.64

## 4. Latest Market Context

- 更新: 2026-06-12T19:42:45.324011+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=63664.6
- Funnel: target 774 → liquid 154 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PLAY/USDT:USDT | +20.68% | $9,748,532.05 |
| ESPORTS/USDT:USDT | +16.25% | $66,601,158.67 |
| AIN/USDT:USDT | +9.32% | $1,809,077.33 |
| HOME/USDT:USDT | +5.58% | $3,028,575.07 |
| COAI/USDT:USDT | +5.32% | $5,033,213.93 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLAY/USDT:USDT | below_1h_threshold | +4.74% | +4.74% |
| AIN/USDT:USDT | below_1h_threshold | +3.34% | +3.34% |
| COAI/USDT:USDT | below_1h_threshold | +2.90% | +2.89% |
| PLSTOCK/USDT:USDT | below_1h_threshold | +2.09% | +2.09% |
| ORCLSTOCK/USDT:USDT | below_1h_threshold | +1.79% | +1.78% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
