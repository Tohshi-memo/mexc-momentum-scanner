# Decision Report

- generated_at: 2026-07-22T10:01:21.227216+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9271**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9271, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.23% | **-0.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +6.57% | **+0.99%** |
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.40% | **+0.77%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.90% | **+1.42%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.33% | **+0.80%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +0.97% | **+0.48%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.82% | **+0.45%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.47% | **+0.45%** |

## 2. $100 Live Portfolio

- 残高: **$104.85** / 初期 $100.00 (+4.85%)
- 確定トレード: 131件 (TP 44 / SL 82 / EXP 5)
- 最新: NIGHT/USDT:USDT SL_HIT PnL -4.00% 残高後 $104.85
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$431.54** / 初期 $100.00 (+331.54%)
- 確定: 3269件 (Win 1031 / Loss 1048 / Flat 1190) / skip 2563件
- 成長率目線: 平均log +0.000447 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $431.54

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.82** / 初期 $100.00 (+30.82%)
- 確定: 1160件 (Win 312 / Loss 253 / Flat 595) / skip 1522件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1562 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $130.82

## 5. Causal Adaptive DryRun ($100)

- 残高: **$102.98** / 初期 $100.00 (+2.98%)
- 確定: 410件 (Win 142 / Loss 168 / Flat 100) / pending 5件 / skip 332件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000535 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $102.98

## 6. Latest Market Context

- 更新: 2026-07-22T10:01:13.382827+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=65919.0
- Funnel: target 888 → liquid 174 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +56.65% | $3,257,312.00 |
| RE/USDT:USDT | +24.27% | $6,616,825.15 |
| SMCISTOCK/USDT:USDT | +18.47% | $4,363,613.62 |
| BNCSTOCK/USDT:USDT | +12.35% | $2,921,094.17 |
| UB/USDT:USDT | +12.03% | $1,217,429.10 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SMCISTOCK/USDT:USDT | below_1h_threshold | +1.74% | +1.70% |
| USOIL/USDT:USDT | below_1h_threshold | +0.95% | +0.91% |
| BANK/USDT:USDT | below_1h_threshold | +0.65% | +0.62% |
| DELLSTOCK/USDT:USDT | below_1h_threshold | +0.54% | +0.51% |
| JIMOTHY/USDT:USDT | below_1h_threshold | +0.45% | +0.41% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
