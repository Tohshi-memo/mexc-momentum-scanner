# Decision Report

- generated_at: 2026-05-20T16:25:26.455058+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4555**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.52% / filled 20/20。**
- 全期間 MARKET基準: n=4555, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.52%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.52% | **+0.52%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.60% | **+1.52%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.82% | **+0.61%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.73% | **+0.55%** |
| MARKET | 20/20 | 100.0% | +0.52% | **+0.52%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.25% | **+0.44%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.81% | **+0.90%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.72% | **+0.36%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.48% | **+0.29%** |

## 2. $100 Live Portfolio

- 残高: **$96.69** / 初期 $100.00 (-3.31%)
- 確定トレード: 57件 (TP 15 / SL 39 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.69
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$124.34** / 初期 $100.00 (+24.34%)
- 確定: 517件 (Win 136 / Loss 176 / Flat 205) / skip 599件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +4.21%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EDEN/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $124.34

## 4. Latest Market Context

- 更新: 2026-05-20T16:25:23.773006+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.38% price=77131.3
- Funnel: target 763 → liquid 129 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.1 >= 65=1, 4h RSI 71.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +9.57% | $37,624,575.42 |
| EDEN/USDT:USDT | +5.24% | $26,098,976.91 |
| NAORIS/USDT:USDT | +2.98% | $1,070,410.17 |
| LYN/USDT:USDT | +2.95% | $1,072,716.27 |
| PLAY/USDT:USDT | +2.42% | $16,657,006.99 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NAORIS/USDT:USDT | below_1h_threshold | +2.98% | +3.36% |
| LYN/USDT:USDT | below_1h_threshold | +2.95% | +3.33% |
| PLAY/USDT:USDT | below_1h_threshold | +2.09% | +2.47% |
| TONCOIN/USDT:USDT | below_1h_threshold | +1.58% | +1.96% |
| WLD/USDT:USDT | below_1h_threshold | +0.98% | +1.35% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
