# Decision Report

- generated_at: 2026-09-05T15:16:17.822126+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13742**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13742, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.79%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.79% | **-0.79%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.19% | **+0.14%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.13% | **+0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.50% | **+1.50%** |
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +1.76% | **+1.32%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.85% | **+1.29%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +2.31% | **+1.27%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +2.21% | **+0.88%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 204件 (TP 76 / SL 123 / EXP 5)
- 最新: CP/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$857.40** / 初期 $100.00 (+757.40%)
- 確定: 5048件 (Win 1519 / Loss 1649 / Flat 1880) / skip 5255件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIULAI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $857.40

## 4. Robust Adaptive DryRun ($100)

- 残高: **$189.70** / 初期 $100.00 (+89.70%)
- 確定: 2487件 (Win 697 / Loss 587 / Flat 1203) / skip 4666件
- 成長率目線: 平均log +0.000257 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0879 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $189.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.33** / 初期 $100.00 (+19.33%)
- 確定: 2367件 (Win 704 / Loss 901 / Flat 762) / pending 4件 / skip 2844件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000204 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $119.33

## 6. Latest Market Context

- 更新: 2026-09-05T15:16:07.808925+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=79685.5
- Funnel: target 1050 → liquid 133 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BULLA/USDT:USDT | +121.29% | $17,242,692.61 |
| 4/USDT:USDT | +72.86% | $22,178,135.19 |
| ICX/USDT:USDT | +44.01% | $1,153,140.45 |
| MARSCOIN/USDT:USDT | +39.36% | $8,439,168.73 |
| AKE/USDT:USDT | +37.13% | $20,441,504.90 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| 4/USDT:USDT | below_1h_threshold | +4.14% | +4.12% |
| DASH/USDT:USDT | below_1h_threshold | +1.54% | +1.52% |
| NIULAI/USDT:USDT | below_1h_threshold | +1.39% | +1.37% |
| PONS/USDT:USDT | below_1h_threshold | +1.17% | +1.16% |
| ZEN/USDT:USDT | below_1h_threshold | +1.13% | +1.11% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
