# Decision Report

- generated_at: 2026-07-29T00:27:09.449238+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9741**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.54% / filled 20/20。**
- 全期間 MARKET基準: n=9741, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.54%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.54% | **+0.54%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.54% | **+0.54%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.40% | **+0.36%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +1.67% | **+0.33%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.01% | **+0.00%** |
| LIMIT_ATR | 12/20 | 60.0% | -0.03% | **-0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.06% | **+0.79%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.71% | **+0.57%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| MARKET_LONG | 20/20 | 100.0% | +0.40% | **+0.40%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |

## 2. $100 Live Portfolio

- 残高: **$107.44** / 初期 $100.00 (+7.44%)
- 確定トレード: 150件 (TP 52 / SL 93 / EXP 5)
- 最新: DEXE/USDT:USDT TP_HIT PnL +8.00% 残高後 $107.44
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$508.48** / 初期 $100.00 (+408.48%)
- 確定: 3511件 (Win 1112 / Loss 1140 / Flat 1259) / skip 2791件
- 成長率目線: 平均log +0.000463 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MUU/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $508.48

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1226件 (Win 338 / Loss 275 / Flat 613) / skip 1926件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1056 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SPCXSTOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$110.26** / 初期 $100.00 (+10.26%)
- 確定: 757件 (Win 245 / Loss 289 / Flat 223) / pending 3件 / skip 462件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000405 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MUU/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $110.26

## 6. Latest Market Context

- 更新: 2026-07-29T00:26:44.205956+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=63973.9
- Funnel: target 904 → liquid 169 → pre 50 → checked 50 → surge 8 → strict 8
- Surge前reject: below_1h_threshold=42, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ON/USDT:USDT | +22.80% | $48,863,039.47 |
| BTW/USDT:USDT | +18.49% | $6,384,303.18 |
| JIMOTHY/USDT:USDT | +17.05% | $1,307,876.73 |
| ZIL/USDT:USDT | +12.77% | $8,251,409.12 |
| BULLA/USDT:USDT | +10.45% | $3,324,951.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +4.67% | +4.56% |
| EUL/USDT:USDT | below_1h_threshold | +3.74% | +3.63% |
| CXMTSTOCK/USDT:USDT | below_1h_threshold | +3.41% | +3.30% |
| O/USDT:USDT | below_1h_threshold | +3.24% | +3.13% |
| DELLSTOCK/USDT:USDT | below_1h_threshold | +2.57% | +2.46% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
