# Decision Report

- generated_at: 2026-07-22T22:21:11.296566+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9333**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9333, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.23% | **-0.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 5/20 | 25.0% | +5.60% | **+1.40%** |
| LIMIT_8PCT | 6/20 | 30.0% | +4.00% | **+1.20%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.51% | **+0.98%** |
| LIMIT_9PCT | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.65% | **+0.52%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 15/20 | 75.0% | +3.34% | **+2.51%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +2.09% | **+1.56%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +2.46% | **+1.23%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +0.81% | **+0.73%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.05% | **+0.68%** |

## 2. $100 Live Portfolio

- 残高: **$103.79** / 初期 $100.00 (+3.79%)
- 確定トレード: 136件 (TP 45 / SL 86 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -2.63% 残高後 $103.79
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$432.51** / 初期 $100.00 (+332.51%)
- 確定: 3317件 (Win 1048 / Loss 1072 / Flat 1197) / skip 2577件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CBRSSTOCK/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $432.51

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.36** / 初期 $100.00 (+30.36%)
- 確定: 1161件 (Win 312 / Loss 254 / Flat 595) / skip 1583件
- 成長率目線: 平均log +0.000228 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1133 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $130.36

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.27** / 初期 $100.00 (+1.27%)
- 確定: 428件 (Win 143 / Loss 178 / Flat 107) / pending 0件 / skip 376件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000379 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CBRSSTOCK/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $101.27

## 6. Latest Market Context

- 更新: 2026-07-22T22:21:05.197765+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=65952.7
- Funnel: target 890 → liquid 179 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +82.73% | $5,617,296.86 |
| BANK/USDT:USDT | +22.47% | $106,902,614.81 |
| BROCCOLIF3B/USDT:USDT | +17.50% | $1,797,045.37 |
| ON/USDT:USDT | +12.74% | $1,957,876.61 |
| RIF/USDT:USDT | +9.37% | $4,418,842.90 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ERA/USDT:USDT | below_1h_threshold | +2.97% | +3.10% |
| KORU/USDT:USDT | below_1h_threshold | +2.69% | +2.81% |
| BANK/USDT:USDT | below_1h_threshold | +2.38% | +2.51% |
| NIGHT/USDT:USDT | below_1h_threshold | +1.60% | +1.73% |
| EVAA/USDT:USDT | below_1h_threshold | +1.36% | +1.48% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
