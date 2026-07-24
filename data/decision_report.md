# Decision Report

- generated_at: 2026-07-24T18:16:18.260168+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9456**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9456, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +1.89% | **+0.66%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.95% | **+0.43%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +1.17% | **+0.12%** |
| LIMIT_4PCT | 16/20 | 80.0% | -0.25% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +5.28% | **+3.96%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.74% | **+2.33%** |
| MARKET_LONG | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.84% | **+0.92%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +1.44% | **+0.72%** |

## 2. $100 Live Portfolio

- 残高: **$103.79** / 初期 $100.00 (+3.79%)
- 確定トレード: 136件 (TP 45 / SL 86 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -2.63% 残高後 $103.79
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$425.48** / 初期 $100.00 (+325.48%)
- 確定: 3325件 (Win 1048 / Loss 1076 / Flat 1201) / skip 2692件
- 成長率目線: 平均log +0.000436 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ACE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $425.48

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.36** / 初期 $100.00 (+30.36%)
- 確定: 1164件 (Win 312 / Loss 254 / Flat 598) / skip 1703件
- 成長率目線: 平均log +0.000228 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0976 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $130.36

## 5. Causal Adaptive DryRun ($100)

- 残高: **$104.10** / 初期 $100.00 (+4.10%)
- 確定: 513件 (Win 171 / Loss 199 / Flat 143) / pending 6件 / skip 414件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000386 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $104.10

## 6. Latest Market Context

- 更新: 2026-07-24T18:16:11.448620+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=64184.3
- Funnel: target 898 → liquid 164 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DEXE/USDT:USDT | +39.24% | $31,699,881.38 |
| AKE/USDT:USDT | +22.56% | $42,298,374.71 |
| ACE/USDT:USDT | +12.38% | $3,904,347.03 |
| PROM/USDT:USDT | +6.92% | $3,393,163.09 |
| PONS/USDT:USDT | +5.65% | $1,241,391.16 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| US/USDT:USDT | below_1h_threshold | +2.52% | +2.47% |
| AKE/USDT:USDT | below_1h_threshold | +2.17% | +2.12% |
| ALLO/USDT:USDT | below_1h_threshold | +1.55% | +1.51% |
| PROM/USDT:USDT | below_1h_threshold | +1.53% | +1.49% |
| VVV/USDT:USDT | below_1h_threshold | +1.21% | +1.17% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
