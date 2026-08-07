# Decision Report

- generated_at: 2026-08-07T16:41:43.819680+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10733**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.44% / filled 20/20。**
- 全期間 MARKET基準: n=10733, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.44%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.44% | **+0.44%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 14/20 | 70.0% | +0.97% | **+0.68%** |
| LIMIT_BB3S | 7/20 | 35.0% | +1.27% | **+0.45%** |
| MARKET | 20/20 | 100.0% | +0.44% | **+0.44%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.91% | **+0.72%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.49% | **+0.32%** |
| MARKET_LONG | 20/20 | 100.0% | +0.02% | **+0.02%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +0.03% | **+0.01%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -0.60% | **-0.12%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$595.60** / 初期 $100.00 (+495.60%)
- 確定: 3799件 (Win 1203 / Loss 1250 / Flat 1346) / skip 3495件
- 成長率目線: 平均log +0.000470 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AXTISTOCK/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $595.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$144.70** / 初期 $100.00 (+44.70%)
- 確定: 1459件 (Win 409 / Loss 342 / Flat 708) / skip 2685件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0117 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CYS/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $144.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.24** / 初期 $100.00 (+18.24%)
- 確定: 1178件 (Win 380 / Loss 465 / Flat 333) / pending 4件 / skip 1030件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000158 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CYS/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $118.24

## 6. Latest Market Context

- 更新: 2026-08-07T16:41:25.646694+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=64943.4
- Funnel: target 961 → liquid 194 → pre 50 → checked 50 → surge 5 → strict 2
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.3 >= 65=1, 4h RSI 77.9 >= 65=1, 4h RSI 92.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EPIC/USDT:USDT | +14.35% | $1,666,027.17 |
| HEI/USDT:USDT | +10.51% | $26,359,640.15 |
| CYS/USDT:USDT | +9.32% | $13,776,181.01 |
| BICO/USDT:USDT | +5.22% | $34,768,089.92 |
| KGEN/USDT:USDT | +4.50% | $3,481,193.14 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KGEN/USDT:USDT | below_1h_threshold | +4.50% | +4.41% |
| SNXX/USDT:USDT | below_1h_threshold | +4.46% | +4.37% |
| MMT/USDT:USDT | below_1h_threshold | +4.31% | +4.22% |
| BLESS/USDT:USDT | below_1h_threshold | +4.26% | +4.17% |
| TUT/USDT:USDT | below_1h_threshold | +3.75% | +3.66% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
