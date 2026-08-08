# Decision Report

- generated_at: 2026-08-08T10:51:28.071227+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10837**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10837, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 10/20 | 50.0% | +1.66% | **+0.83%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.63% | **+0.41%** |
| LIMIT_BB3S | 7/18 | 38.9% | +0.84% | **+0.33%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +6.50% | **+6.50%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.67% | **+1.42%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.46% | **+1.02%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +3.29% | **+0.82%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$628.01** / 初期 $100.00 (+528.01%)
- 確定: 3838件 (Win 1212 / Loss 1253 / Flat 1373) / skip 3560件
- 成長率目線: 平均log +0.000479 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLUAI/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $628.01

## 4. Robust Adaptive DryRun ($100)

- 残高: **$142.00** / 初期 $100.00 (+42.00%)
- 確定: 1510件 (Win 424 / Loss 360 / Flat 726) / skip 2738件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1334 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $142.00

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.42** / 初期 $100.00 (+18.42%)
- 確定: 1206件 (Win 385 / Loss 469 / Flat 352) / pending 5件 / skip 1099件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000342 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BLUAI/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $118.42

## 6. Latest Market Context

- 更新: 2026-08-08T10:51:17.037081+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=64980.6
- Funnel: target 961 → liquid 176 → pre 50 → checked 50 → surge 4 → strict 0
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.4 >= 65=1, 4h RSI 91.1 >= 65=1, 4h RSI 90.3 >= 65=1, 4h RSI 67.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +244.60% | $9,465,318.88 |
| BLUAI/USDT:USDT | +59.49% | $2,905,258.17 |
| TUT/USDT:USDT | +58.15% | $4,864,248.96 |
| MMT/USDT:USDT | +33.87% | $5,734,354.73 |
| CYS/USDT:USDT | +28.96% | $23,607,130.34 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KGEN/USDT:USDT | below_1h_threshold | +3.21% | +3.18% |
| SLX/USDT:USDT | below_1h_threshold | +3.20% | +3.17% |
| BLESS/USDT:USDT | below_1h_threshold | +1.91% | +1.88% |
| RAVE/USDT:USDT | below_1h_threshold | +1.81% | +1.78% |
| BEAT/USDT:USDT | below_1h_threshold | +1.67% | +1.64% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
