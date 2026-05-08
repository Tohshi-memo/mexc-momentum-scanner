# Decision Report

- generated_at: 2026-05-08T16:47:28.529902+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3805**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.20% / filled 20/20。**
- 全期間 MARKET基準: n=3805, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+1.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.20% | **+1.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.20% | **+1.20%** |
| ASK | 20/20 | 100.0% | +1.15% | **+1.15%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.41% | **+0.29%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.30% | **+0.24%** |
| LIMIT_5PCT | 2/20 | 10.0% | +0.95% | **+0.10%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +1.24% | **+0.62%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.39% | **+0.20%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.17% | **+0.06%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.10% | **+0.06%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | -0.97% | **-0.24%** |

## 2. $100 Live Portfolio

- 残高: **$98.82** / 初期 $100.00 (-1.18%)
- 確定トレード: 27件 (TP 7 / SL 18 / EXP 2)
- 最新: RKLBSTOCK/USDT:USDT SL_HIT PnL -2.88% 残高後 $98.82
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 192件 (Win 48 / Loss 64 / Flat 80) / skip 174件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FILECOIN/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-08T16:47:25.000368+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.43% price=79769.5
- Funnel: target 772 → liquid 180 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.0 >= 65=1, 4h RSI 82.0 >= 65=1, 4h RSI 75.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CHIP/USDT:USDT | +9.74% | $46,641,148.29 |
| SPORTFUN/USDT:USDT | +5.82% | $1,309,537.35 |
| SIREN/USDT:USDT | +5.36% | $14,054,497.83 |
| JUP/USDT:USDT | +4.87% | $3,510,213.14 |
| PENGUIN/USDT:USDT | +4.44% | $1,039,312.70 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JUP/USDT:USDT | below_1h_threshold | +4.92% | +5.35% |
| PENGUIN/USDT:USDT | below_1h_threshold | +4.45% | +4.88% |
| ONDO/USDT:USDT | below_1h_threshold | +4.26% | +4.69% |
| COLLECT/USDT:USDT | below_1h_threshold | +3.68% | +4.12% |
| BSB/USDT:USDT | below_1h_threshold | +3.29% | +3.73% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
