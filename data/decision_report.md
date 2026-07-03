# Decision Report

- generated_at: 2026-07-03T12:45:59.053806+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8160**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.10% / filled 20/20。**
- 全期間 MARKET基準: n=8160, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.10% | **+2.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.10% | **+2.10%** |
| ASK | 20/20 | 100.0% | +2.03% | **+2.03%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.27% | **+1.02%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.96% | **+0.67%** |
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 11/20 | 55.0% | -0.14% | **-0.07%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | -0.41% | **-0.20%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | -0.46% | **-0.25%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -2.30% | **-0.35%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -1.86% | **-0.37%** |

## 2. $100 Live Portfolio

- 残高: **$102.11** / 初期 $100.00 (+2.11%)
- 確定トレード: 54件 (TP 19 / SL 34 / EXP 1)
- 最新: SKHYNIXSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.11
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$286.57** / 初期 $100.00 (+186.57%)
- 確定: 2481件 (Win 763 / Loss 828 / Flat 890) / skip 2240件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GUA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $286.57

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.08** / 初期 $100.00 (+6.08%)
- 確定: 606件 (Win 146 / Loss 144 / Flat 316) / skip 965件
- 成長率目線: 平均log +0.000097 / 幾何平均 +0.010% per trade / maxDD +3.57%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_robust_growth_score) / robust_score -0.0489 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: GUA/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.07% 残高後 $106.08

## 5. Latest Market Context

- 更新: 2026-07-03T12:45:53.050379+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=61923.1
- Funnel: target 834 → liquid 167 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NEX/USDT:USDT | +47.97% | $2,828,606.47 |
| ARPA/USDT:USDT | +43.96% | $4,871,789.11 |
| RIF/USDT:USDT | +36.19% | $9,124,154.45 |
| BLESS/USDT:USDT | +29.29% | $6,766,504.06 |
| ZKP/USDT:USDT | +28.30% | $5,335,671.72 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ALLO/USDT:USDT | below_1h_threshold | +3.63% | +3.74% |
| MANA/USDT:USDT | below_1h_threshold | +3.47% | +3.58% |
| XPL/USDT:USDT | below_1h_threshold | +3.20% | +3.32% |
| BLESS/USDT:USDT | below_1h_threshold | +2.94% | +3.06% |
| RIVER/USDT:USDT | below_1h_threshold | +2.72% | +2.83% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
