# Decision Report

- generated_at: 2026-05-12T01:59:16.739645+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4087**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=4087, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.60% | **+0.65%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.63% | **+0.47%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.51% | **+0.41%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.97% | **+0.68%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.00% | **+0.60%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +1.09% | **+0.60%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.00% | **+0.40%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.72% | **+0.36%** |

## 2. $100 Live Portfolio

- 残高: **$99.19** / 初期 $100.00 (-0.81%)
- 確定トレード: 34件 (TP 9 / SL 22 / EXP 3)
- 最新: DOGS/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.19
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$109.51** / 初期 $100.00 (+9.51%)
- 確定: 224件 (Win 57 / Loss 78 / Flat 89) / skip 424件
- 成長率目線: 平均log +0.000406 / 幾何平均 +0.041% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GIGA/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $109.51

## 4. Latest Market Context

- 更新: 2026-05-12T01:59:07.578845+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.45% price=81143.5
- Funnel: target 762 → liquid 190 → pre 50 → checked 50 → surge 4 → strict 2
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.1 >= 65=1, 4h RSI 81.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| GIGA/USDT:USDT | +50.07% | $1,477,409.32 |
| SKYAI/USDT:USDT | +24.51% | $38,239,121.50 |
| USELESS/USDT:USDT | +21.12% | $4,012,880.61 |
| SAGA/USDT:USDT | +18.83% | $7,236,555.05 |
| H/USDT:USDT | +16.89% | $15,856,768.58 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| USELESS/USDT:USDT | below_1h_threshold | +4.34% | +4.79% |
| SAHARA/USDT:USDT | below_1h_threshold | +2.72% | +3.16% |
| RIF/USDT:USDT | below_1h_threshold | +2.38% | +2.83% |
| TRUTH/USDT:USDT | below_1h_threshold | +1.65% | +2.09% |
| COLLECT/USDT:USDT | below_1h_threshold | +1.63% | +2.08% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
