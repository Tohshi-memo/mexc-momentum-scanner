# Decision Report

- generated_at: 2026-07-22T22:11:17.343487+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9330**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9330, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.67%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.67% | **-0.67%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 5/20 | 25.0% | +5.60% | **+1.40%** |
| LIMIT_9PCT | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_8PCT | 6/20 | 30.0% | +2.00% | **+0.60%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.81% | **+0.56%** |
| LIMIT_7PCT | 7/20 | 35.0% | +1.37% | **+0.48%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +2.51% | **+2.13%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.91% | **+1.89%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +2.90% | **+1.74%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +1.64% | **+1.64%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +1.52% | **+1.52%** |

## 2. $100 Live Portfolio

- 残高: **$103.79** / 初期 $100.00 (+3.79%)
- 確定トレード: 136件 (TP 45 / SL 86 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -2.63% 残高後 $103.79
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$439.06** / 初期 $100.00 (+339.06%)
- 確定: 3314件 (Win 1048 / Loss 1069 / Flat 1197) / skip 2577件
- 成長率目線: 平均log +0.000446 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKHYSTOCK/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.30% 残高後 $439.06

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.36** / 初期 $100.00 (+30.36%)
- 確定: 1161件 (Win 312 / Loss 254 / Flat 595) / skip 1580件
- 成長率目線: 平均log +0.000228 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1255 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $130.36

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.44** / 初期 $100.00 (+1.44%)
- 確定: 427件 (Win 143 / Loss 177 / Flat 107) / pending 1件 / skip 375件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000458 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: RE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.07% 残高後 $101.44

## 6. Latest Market Context

- 更新: 2026-07-22T22:11:10.638228+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=65989.5
- Funnel: target 890 → liquid 179 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +82.34% | $5,392,301.74 |
| BANK/USDT:USDT | +21.23% | $106,292,553.63 |
| BROCCOLIF3B/USDT:USDT | +17.68% | $1,793,112.25 |
| RIF/USDT:USDT | +13.22% | $4,383,621.89 |
| ON/USDT:USDT | +11.72% | $1,931,028.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KORU/USDT:USDT | below_1h_threshold | +2.69% | +2.76% |
| NIGHT/USDT:USDT | below_1h_threshold | +1.84% | +1.91% |
| BANK/USDT:USDT | below_1h_threshold | +1.26% | +1.32% |
| EVAA/USDT:USDT | below_1h_threshold | +1.21% | +1.27% |
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +1.05% | +1.11% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
