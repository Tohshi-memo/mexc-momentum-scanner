# Decision Report

- generated_at: 2026-08-07T16:46:42.738973+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10734**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.61% / filled 20/20。**
- 全期間 MARKET基準: n=10734, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.61%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.61% | **+0.61%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.61% | **+0.61%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.68% | **+0.44%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.80% | **+0.64%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.37% | **+0.24%** |
| MARKET_LONG | 20/20 | 100.0% | -0.06% | **-0.06%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -0.90% | **-0.13%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | -1.45% | **-0.15%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$595.60** / 初期 $100.00 (+495.60%)
- 確定: 3799件 (Win 1203 / Loss 1250 / Flat 1346) / skip 3496件
- 成長率目線: 平均log +0.000470 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AXTISTOCK/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $595.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$144.70** / 初期 $100.00 (+44.70%)
- 確定: 1460件 (Win 409 / Loss 342 / Flat 709) / skip 2685件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0115 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CYS/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $144.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.24** / 初期 $100.00 (+18.24%)
- 確定: 1178件 (Win 380 / Loss 465 / Flat 333) / pending 4件 / skip 1030件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000158 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CYS/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $118.24

## 6. Latest Market Context

- 更新: 2026-08-07T16:46:28.189069+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=64912.7
- Funnel: target 961 → liquid 195 → pre 50 → checked 50 → surge 4 → strict 2
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.5 >= 65=1, 4h RSI 92.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EPIC/USDT:USDT | +15.94% | $1,688,030.81 |
| HEI/USDT:USDT | +11.88% | $26,453,799.62 |
| BICO/USDT:USDT | +5.24% | $34,915,444.89 |
| KGEN/USDT:USDT | +4.45% | $3,488,211.55 |
| UB/USDT:USDT | +4.29% | $5,895,594.56 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KGEN/USDT:USDT | below_1h_threshold | +4.50% | +4.46% |
| UB/USDT:USDT | below_1h_threshold | +4.28% | +4.23% |
| TUT/USDT:USDT | below_1h_threshold | +4.11% | +4.06% |
| BLESS/USDT:USDT | below_1h_threshold | +3.99% | +3.95% |
| MMT/USDT:USDT | below_1h_threshold | +3.96% | +3.92% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
