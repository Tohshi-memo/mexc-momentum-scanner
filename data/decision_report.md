# Decision Report

- generated_at: 2026-07-24T00:41:14.048570+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9406**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9406, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.37%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.37% | **-0.37%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 3/20 | 15.0% | +0.95% | **+0.14%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.00% | **+0.00%** |
| LIMIT_ATR | 15/20 | 75.0% | -0.08% | **-0.06%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | -0.90% | **-0.27%** |
| MARKET | 20/20 | 100.0% | -0.37% | **-0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.04% | **+1.63%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.78% | **+1.61%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.97% | **+1.18%** |
| LIMIT_8PCT_LONG | 4/20 | 20.0% | +4.00% | **+0.80%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.71% | **+0.68%** |

## 2. $100 Live Portfolio

- 残高: **$103.79** / 初期 $100.00 (+3.79%)
- 確定トレード: 136件 (TP 45 / SL 86 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -2.63% 残高後 $103.79
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$425.48** / 初期 $100.00 (+325.48%)
- 確定: 3322件 (Win 1048 / Loss 1076 / Flat 1198) / skip 2645件
- 成長率目線: 平均log +0.000436 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.13% 残高後 $425.48

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.36** / 初期 $100.00 (+30.36%)
- 確定: 1163件 (Win 312 / Loss 254 / Flat 597) / skip 1654件
- 成長率目線: 平均log +0.000228 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BILL/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $130.36

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.73** / 初期 $100.00 (+1.73%)
- 確定: 467件 (Win 155 / Loss 186 / Flat 126) / pending 1件 / skip 406件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000389 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $101.73

## 6. Latest Market Context

- 更新: 2026-07-24T00:41:07.383571+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.51% price=64737.8
- Funnel: target 897 → liquid 175 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +31.92% | $7,757,667.86 |
| BILL/USDT:USDT | +15.72% | $8,053,311.69 |
| AKE/USDT:USDT | +12.74% | $24,854,980.60 |
| ON/USDT:USDT | +12.30% | $6,963,810.64 |
| RIF/USDT:USDT | +12.26% | $17,889,966.39 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RIF/USDT:USDT | below_1h_threshold | +4.65% | +5.16% |
| RE/USDT:USDT | below_1h_threshold | +3.47% | +3.98% |
| ESPORTS/USDT:USDT | below_1h_threshold | +2.63% | +3.14% |
| ACE/USDT:USDT | below_1h_threshold | +2.61% | +3.12% |
| ZAMA/USDT:USDT | below_1h_threshold | +2.43% | +2.94% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
