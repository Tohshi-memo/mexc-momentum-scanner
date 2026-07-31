# Decision Report

- generated_at: 2026-07-31T10:36:19.607094+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9988**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9988, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.08%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.08% | **+0.08%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/14 | 42.9% | +0.76% | **+0.33%** |
| MARKET | 20/20 | 100.0% | +0.08% | **+0.08%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.16% | **+0.05%** |
| LIMIT_7PCT | 4/20 | 20.0% | -0.60% | **-0.12%** |
| LIMIT_5PCT | 6/20 | 30.0% | -0.70% | **-0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +3.34% | **+2.01%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.60% | **+1.20%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.21% | **+0.99%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +0.16% | **+0.09%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +0.20% | **+0.09%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$547.70** / 初期 $100.00 (+447.70%)
- 確定: 3573件 (Win 1141 / Loss 1168 / Flat 1264) / skip 2976件
- 成長率目線: 平均log +0.000476 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $547.70

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.81** / 初期 $100.00 (+40.81%)
- 確定: 1278件 (Win 359 / Loss 297 / Flat 622) / skip 2121件
- 成長率目線: 平均log +0.000268 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0995 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MMT/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $140.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$111.61** / 初期 $100.00 (+11.61%)
- 確定: 821件 (Win 268 / Loss 325 / Flat 228) / pending 5件 / skip 634件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000376 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MMT/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $111.61

## 6. Latest Market Context

- 更新: 2026-07-31T10:36:10.302080+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.18% price=63806.9
- Funnel: target 921 → liquid 177 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.9 >= 65=1, 4h RSI 97.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MMT/USDT:USDT | +84.43% | $16,886,244.44 |
| KOMA/USDT:USDT | +75.63% | $12,478,748.77 |
| GIGGLE/USDT:USDT | +36.74% | $8,969,902.49 |
| AXTISTOCK/USDT:USDT | +35.89% | $5,260,391.85 |
| AMZU/USDT:USDT | +23.49% | $1,666,054.84 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CAP/USDT:USDT | below_1h_threshold | +4.57% | +4.38% |
| ROBO/USDT:USDT | below_1h_threshold | +3.87% | +3.69% |
| GRVT/USDT:USDT | below_1h_threshold | +3.13% | +2.94% |
| GIGGLE/USDT:USDT | below_1h_threshold | +2.75% | +2.57% |
| UB/USDT:USDT | below_1h_threshold | +2.73% | +2.55% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
